from domain.entities import Order
from domain.discount import PercentageDiscount, FixedDiscount
from infrastructure.payment_gateway import PayPalPayment
from infrastructure.shipping_service import ExpressShipping
from infrastructure.notification_service import NotificationService
from infrastructure.in_memory_repository import InMemoryOrderRepository
from use_cases.checkout_use_case import CheckoutUseCase


def main():

    order = Order(100)
    order.add_discount(PercentageDiscount(0.10))
    order.add_discount(FixedDiscount(5))

    payment = PayPalPayment()
    shipping = ExpressShipping()
    notification = NotificationService()
    repository = InMemoryOrderRepository()

    checkout = CheckoutUseCase(
        payment,
        shipping,
        notification,
        repository
    )

    total = checkout.execute(order)

    print("Total final:", total)


if __name__ == "__main__":
    main()