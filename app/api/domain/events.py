class OrderCreatedEvent:
    def __init__(self, order_id, user_id, items):
        self.order_id = order_id
        self.user_id = user_id
        self.items = items

    @staticmethod
    def from_order(order):
        return OrderCreatedEvent(
            order.id,
            order.user_id,
            order.items
        )