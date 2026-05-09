import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, Float, Integer,DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.db.engine import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, index=True)
    status = Column(String, default="pending", nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    total_amount = Column(Float, default=0.0)

    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String(36), ForeignKey("orders.id"), nullable=False)
    product_id = Column(String, nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, default=0.0)

    order = relationship("Order", back_populates="items")