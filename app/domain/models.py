import uuid

class Order:
    def __init__(self, id, user_id, items):
        self.id = id
        self.user_id = user_id
        self.items = items

    @staticmethod
    def create(user_id, items):
        return Order(str(uuid.uuid4()), user_id, items)