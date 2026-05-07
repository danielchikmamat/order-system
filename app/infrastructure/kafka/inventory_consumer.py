from app.core.config import Settings
from app.infrastructure.kafka.producer import KafkaPublisher
from aiokafka import AIOKafkaConsumer
import json
from app.events.inventory_reserve_request import InventoryReserveRequestEvent
from app.events.inventory_reserved import InventoryReserved

class InventoryConsumer:
    def __init__(self, publisher: KafkaPublisher):
        settings = Settings()
        self.publisher = publisher

        self.consumer = AIOKafkaConsumer(
            "inventory.reserve.requested",
            bootstrap_servers=settings.KAFKA_BOOTSTRAP,
            group_id="inventory-processors",
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            auto_offset_reset="earliest",
        )


    async def start(self):
            await self.consumer.start()
            print("✅ InventoryConsumer started")

            try:
                async for message in self.consumer:
                    await self.handle_message(message.value)
            finally:
                await self.consumer.stop()

    async def handle_message(self, data: dict):
        try:
            event = InventoryReserveRequestEvent(**data)
        except Exception as e:
            print("❌ Invalid event:", e)
            return

        await self.process_order(event)

    async def process_order(self, event: InventoryReserveRequestEvent):
        print(f"📦 Processing inventory reserve request {event.reservation_id}")
        print(f"order_id: {event.order_id}")
        reservation_event = InventoryReserved(
            order_id =event.order_id,
            reservation_id =event.reservation_id,
            status="reserved"
        )
        await self.publisher.publish("inventory.updated", reservation_event.model_dump())
        print(f"📤 Published inventory.updated for order {event.order_id}")