from domain.shipping import ShippingStrategy

class StandardShipping(ShippingStrategy):
    def calculate(self, amount):
        return 10

class ExpressShipping(ShippingStrategy):
    def calculate(self, amount):
        return 25