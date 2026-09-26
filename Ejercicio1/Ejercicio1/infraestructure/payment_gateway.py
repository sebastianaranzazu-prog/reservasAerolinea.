from domain.payment import PaymentStrategy

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"[PayPal] Pago procesado por {amount}")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"[CreditCard] Pago procesado por {amount}")