package domain;

import interfaces.PricingStrategy;
import interfaces.ReservationObserver;
import interfaces.ReservationState;

import java.util.ArrayList;
import java.util.List;

/**
 * Representa una reserva de avión.
 *
 * La clase utiliza:
 *
 * - Strategy para el cálculo del precio.
 * - State para controlar el comportamiento según el estado.
 * - Observer para notificar cambios.
 */

public class Reservation {

    private final String reservationCode;
    private Passenger passenger;
    private Flight flight;
    private Seat seat;
    private double basePrice;
    private double finalPrice;
    private int daysInAdvance;

    private final List<String> additionalServices;
    private final List<ReservationObserver> observers;

    private PricingStrategy pricingStrategy;
    private ReservationState state;
    private Payment payment;

    public Reservation(
            String reservationCode,
            Passenger passenger,
            Flight flight,
            Seat seat,
            double basePrice,
            int daysInAdvance,
            List<String> additionalServices,
            PricingStrategy pricingStrategy
    ) {
        this.reservationCode = reservationCode;
        this.passenger = passenger;
        this.flight = flight;
        this.seat = seat;
        this.basePrice = basePrice;
        this.daysInAdvance = daysInAdvance;
        this.additionalServices = additionalServices;
        this.pricingStrategy = pricingStrategy;

        this.finalPrice = basePrice;
        this.observers = new ArrayList<>();

        /*
         * Toda reserva inicia en estado pendiente.
         */
        this.state = new PendingState();
    }

    public void addObserver(ReservationObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(ReservationObserver observer) {
        observers.remove(observer);
    }

    /**
     * Notifica a todos los observadores registrados.
     */
    public void notifyObservers(String message) {
        for (ReservationObserver observer : observers) {
            observer.update(message);
        }
    }

    /**
     * Calcula el precio utilizando la estrategia seleccionada.
     */
    public void calculatePrice() {
        double servicesPrice = calculateAdditionalServicesPrice();

        this.finalPrice = pricingStrategy.calculatePrice(
                flight,
                daysInAdvance,
                servicesPrice
        );
    }

    /**
     * Para simplificar el ejemplo, cada servicio adicional cuesta 25.
     */
    private double calculateAdditionalServicesPrice() {
        return additionalServices.size() * 25.0;
    }

    public void confirm() {
        state.confirm(this);
    }

    public void cancel() {
        state.cancel(this);
    }

    public void modify() {
        state.modify(this);
    }

    public void checkIn() {
        state.checkIn(this);
    }

    public void board() {
        state.board(this);
    }

    public void changeState(ReservationState newState) {
        this.state = newState;

        notifyObservers(
                "La reserva " + reservationCode
                        + " cambió al estado: "
                        + newState.getName()
        );
    }

    public void processPayment() {
        this.payment = new Payment(
                "PAY-" + reservationCode,
                finalPrice
        );

        payment.processPayment();

        notifyObservers(
                "El pago de la reserva "
                        + reservationCode
                        + " fue procesado."
        );
    }

    /**
     * Permite actualizar la estrategia de precios.
     */
    public void setPricingStrategy(PricingStrategy pricingStrategy) {
        this.pricingStrategy = pricingStrategy;
    }

    /**
     * Permite realizar un upgrade de clase.
     */
    public void upgrade(PricingStrategy newPricingStrategy) {
        this.pricingStrategy = newPricingStrategy;
        calculatePrice();

        notifyObservers(
                "La reserva " + reservationCode
                        + " fue actualizada a una categoría superior. "
                        + "Nuevo precio: $" + finalPrice
        );
    }

    public String getReservationCode() {
        return reservationCode;
    }

    public Passenger getPassenger() {
        return passenger;
    }

    public Flight getFlight() {
        return flight;
    }

    public Seat getSeat() {
        return seat;
    }

    public double getBasePrice() {
        return basePrice;
    }

    public double getFinalPrice() {
        return finalPrice;
    }

    public ReservationState getState() {
        return state;
    }

    public Payment getPayment() {
        return payment;
    }

    @Override
    public String toString() {
        return "\nReserva: " + reservationCode
                + "\nPasajero: " + passenger
                + "\nVuelo: " + flight
                + "\nAsiento: " + seat
                + "\nPrecio base: $" + basePrice
                + "\nPrecio final: $" + finalPrice
                + "\nEstado: " + state.getName()
                + "\n";
    }
    
}
