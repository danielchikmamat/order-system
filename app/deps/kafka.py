
from app.infrastructure.kafka.order_producer import KafkaProducer

producer = KafkaProducer()

def get_publisher():
    return producer

def get_repo():
    return None  # or in-memory stub for now
