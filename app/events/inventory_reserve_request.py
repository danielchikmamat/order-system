from typing import List
from pydantic import BaseModel
from app.schemas.order import OrderItem


class InventoryReserveRequestEvent(BaseModel):
    order_id: str
    reservation_id: str
    items: List[OrderItem]