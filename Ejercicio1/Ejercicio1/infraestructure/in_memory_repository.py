from interfaces.repositories import OrderRepository


class InMemoryOrderRepository(OrderRepository):

    def __init__(self):
        self.storage = {}

    def save(self, order):
        order_id = str(len(self.storage) + 1)
        self.storage[order_id] = order
        return order_id

    def get_by_id(self, order_id):
        return self.storage.get(order_id)