from fastapi import FastAPI
from app.api.orders import router as order_router
from app.infrastructure.kafka.order_producer import KafkaPublisher
from app.core.state import state

app = FastAPI()
app.include_router(order_router)


@app.on_event("startup")
async def startup():
    state.kafka_publisher = KafkaPublisher()
    await state.kafka_publisher.start()


@app.on_event("shutdown")
async def shutdown():
    await state.kafka_publisher.stop()