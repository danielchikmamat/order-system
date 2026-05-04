from fastapi import Depends

from app.services.order_service import OrderService
from app.deps.kafka import get_publisher


def get_repo():
    return None  # no DB yet


def get_order_service(
    repo=Depends(get_repo),
    publisher=Depends(get_publisher),
):
    return OrderService(repo, publisher)