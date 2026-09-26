package domain;

/**
 * Representa el pago de una reserva.
 */

public class Payment {

    private final String paymentId;
    private final double amount;
    private boolean paid;

    public Payment(String paymentId, double amount) {
        this.paymentId = paymentId;
        this.amount = amount;
        this.paid = false;
    }

    /**
     * Simula la ejecución del pago.
     */
    public void processPayment() {
        this.paid = true;
        System.out.println("Pago procesado correctamente.");
    }

    public String getPaymentId() {
        return paymentId;
    }

    public double getAmount() {
        return amount;
    }

    public boolean isPaid() {
        return paid;
    }
    
}
