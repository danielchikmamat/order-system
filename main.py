from fastapi import FastAPI
from app.infrastructure.kafka.order_producer import KafkaProducer

app = FastAPI()
producer = KafkaProducer()


@app.on_event("startup")
async def startup():
    await producer.start()


@app.on_event("shutdown")
async def shutdown():
    await producer.stop()