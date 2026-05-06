from typing import List
from pydantic import BaseModel
from app.schemas.order import OrderItem


class OrderCreatedEvent(BaseModel):
    order_id: str
    user_id: str
    items: List[OrderItem]