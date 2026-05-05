from fastapi import FastAPI
#from app.infrastructure.kafka.order_producer import KafkaProducer
from app.api.orders import router as order_router

app = FastAPI()
app.include_router(order_router)
'''
producer = KafkaProducer()

app.include_router(order_router)

@app.on_event("startup")
async def startup():
    await producer.start()


@app.on_event("shutdown")
async def shutdown():
    await producer.stop()

'''