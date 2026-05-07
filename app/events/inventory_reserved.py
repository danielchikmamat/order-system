from pydantic import BaseModel



class InventoryReserved(BaseModel):
    order_id: str
    reservation_id: str
    status: str = "reserved"