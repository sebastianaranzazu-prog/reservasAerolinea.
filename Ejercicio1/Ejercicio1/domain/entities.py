from abc import ABC, abstractmethod

class Order:
    def __init__(self, base_amount):
        self.base_amount = base_amount
        self.discounts = []

    def add_discount(self, discount):
        self.discounts.append(discount)

    def calculate_total(self):
        total = self.base_amount
        for discount in self.discounts:
            total = discount.apply(total)
        return total