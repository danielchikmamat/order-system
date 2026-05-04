from aiokafka import AIOKafkaConsumer
import json
from app.core.config import Settings
from app.events.order_created import OrderCreatedEvent


class OrderConsumer:
    def __init__(self):
        settings = Settings()

        self.consumer = AIOKafkaConsumer(
            "order.created",
            bootstrap_servers=settings.KAFKA_BOOTSTRAP,
            group_id="order-processors",
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            auto_offset_reset="earliest",
        )

    async def start(self):
        await self.consumer.start()
        print("✅ Consumer started")

        try:
            async for message in self.consumer:
                await self.handle_message(message.value)
        finally:
            await self.consumer.stop()

    async def handle_message(self, data: dict):
        try:
            event = OrderCreatedEvent(**data)
        except Exception as e:
            print("❌ Invalid event:", e)
            return

        await self.process_order(event)

    async def process_order(self, event: OrderCreatedEvent):
        print(f"📦 Processing order {event.order_id}")
        print(f"👤 User: {event.user_id}")