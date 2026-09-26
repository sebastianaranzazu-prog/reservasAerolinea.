class CheckoutUseCase:

    def __init__(self, payment_strategy, shipping_strategy,
                 notification_service, order_repository):
        self.payment_strategy = payment_strategy
        self.shipping_strategy = shipping_strategy
        self.notification_service = notification_service
        self.order_repository = order_repository

    def execute(self, order):

        subtotal = order.calculate_total()
        shipping_cost = self.shipping_strategy.calculate(subtotal)
        total = subtotal + shipping_cost

        self.payment_strategy.pay(total)

        # Persistir orden
        order_id = self.order_repository.save(order)

        self.notification_service.notify(
            f"Compra realizada con éxito. ID Orden: {order_id}"
        )

        return total