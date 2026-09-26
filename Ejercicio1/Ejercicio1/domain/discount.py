from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount):
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, amount):
        return amount * (1 - self.percentage)

class FixedDiscount(DiscountStrategy):
    def __init__(self, value):
        self.value = value

    def apply(self, amount):
        return amount - self.value