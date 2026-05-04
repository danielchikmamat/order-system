from pydantic import BaseModel

class OrderCreatedEvent(BaseModel):
    order_id: str
    user_id: str
    total_items: int