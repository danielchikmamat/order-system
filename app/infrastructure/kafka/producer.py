import json
from aiokafka import AIOKafkaProducer
from app.core.config import Settings


class KafkaPublisher:
    def __init__(self):
        settings = Settings()
        self.bootstrap_servers = settings.KAFKA_BOOTSTRAP
        self.producer = None

    async def start(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        await self.producer.start()

    async def stop(self):
        if self.producer:
            await self.producer.stop()

    async def publish(self, topic: str, event: dict):
        await self.producer.send_and_wait(topic, event)