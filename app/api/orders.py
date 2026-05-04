from fastapi import APIRouter, Depends
from app.schemas.order import CreateOrderRequest
from app.services.order_service import OrderService
from app.deps.order import get_order_service

router = APIRouter(prefix="/orders")

@router.post("")
async def create_order(
    request: CreateOrderRequest,
    service: OrderService = Depends(get_order_service)
):
    return await service.create_order(request)