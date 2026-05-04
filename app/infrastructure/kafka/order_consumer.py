from aiokafka import AIOKafkaConsumer
import json
from app.core.config import settings


class OrderConsumer:
    def __init__(self):
        self.consumer = AIOKafkaConsumer(
            "order.created",
            bootstrap_servers=settings.KAFKA_BOOTSTRAP,
            group_id="order-service",
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )

    async def start(self):
        await self.consumer.start()
        try:
            async for message in self.consumer:
                await self.process(message.value)
        finally:
            await self.consumer.stop()

    async def process(self, event: dict):
        print("Processing order:", event)

        # Example logic:
        # - charge payment
        # - reserve stock
        # - call other services