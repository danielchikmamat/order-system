import asyncio
from app.infrastructure.kafka.inventory_consumer import InventoryConsumer
from app.infrastructure.kafka.producer import KafkaPublisher  # Add this import

async def main():
    publisher = KafkaPublisher()  # Create the publisher
    await publisher.start()  # Start it

    consumer = InventoryConsumer(publisher)  # Pass it to the consumer
    await consumer.start()

    await publisher.stop()  # Clean up when done

if __name__ == "__main__":
    asyncio.run(main())