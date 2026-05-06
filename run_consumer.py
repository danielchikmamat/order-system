import asyncio
from app.infrastructure.kafka.order_consumer import OrderConsumer
from app.infrastructure.kafka.producer import KafkaPublisher  # Add this import

async def main():
    publisher = KafkaPublisher()  # Create the publisher
    await publisher.start()  # Start it

    consumer = OrderConsumer(publisher)  # Pass it to the consumer
    await consumer.start()

    await publisher.stop()  # Clean up when done

if __name__ == "__main__":
    asyncio.run(main())