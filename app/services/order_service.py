from app.domain.models import Order
from app.domain.events import OrderCreatedEvent

class OrderService:
    def __init__(self, repo, publisher):
        self.repo = repo
        self.publisher = publisher

    async def create_order(self, request):
        order = Order.create(request.user_id, request.items)

        await self.repo.save(order)

        event = OrderCreatedEvent.from_order(order)
        await self.publisher.publish(event)

        return {"order_id": order.id}