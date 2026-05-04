from aiokafka import AIOKafkaProducer
import json

class KafkaProducer:
    def __init__(self, bootstrap_servers):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode()
        )

    async def start(self):
        await self.producer.start()

    async def publish(self, topic, event):
        await self.producer.send(topic, event.__dict__)