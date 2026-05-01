from fastapi import APIRouter, Depends
from app.schemas.order import CreateOrderRequest
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders")

@router.post("")
async def create_order(
    request: CreateOrderRequest,
    service: OrderService = Depends()
):
    return await service.create_order(request)