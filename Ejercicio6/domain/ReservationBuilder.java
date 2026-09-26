package domain;

import interfaces.PricingStrategy;

import java.util.ArrayList;
import java.util.List;

/**
 * Builder encargado de construir objetos Reservation
 * de forma clara y controlada.
 */

public class ReservationBuilder {

    private String reservationCode;
    private Passenger passenger;
    private Flight flight;
    private Seat seat;
    private double basePrice;
    private int daysInAdvance;
    private PricingStrategy pricingStrategy;
    private final List<String> additionalServices;

    public ReservationBuilder() {
        this.additionalServices = new ArrayList<>();
    }

    public ReservationBuilder withReservationCode(String reservationCode) {
        this.reservationCode = reservationCode;
        return this;
    }

    public ReservationBuilder withPassenger(Passenger passenger) {
        this.passenger = passenger;
        return this;
    }

    public ReservationBuilder withFlight(Flight flight) {
        this.flight = flight;
        return this;
    }

    public ReservationBuilder withSeat(Seat seat) {
        this.seat = seat;
        return this;
    }

    public ReservationBuilder withBasePrice(double basePrice) {
        this.basePrice = basePrice;
        return this;
    }

    public ReservationBuilder withDaysInAdvance(int daysInAdvance) {
        this.daysInAdvance = daysInAdvance;
        return this;
    }

    public ReservationBuilder withPricingStrategy(
            PricingStrategy pricingStrategy
    ) {
        this.pricingStrategy = pricingStrategy;
        return this;
    }

    public ReservationBuilder addService(String service) {
        this.additionalServices.add(service);
        return this;
    }

    /**
     * Construye la reserva después de validar
     * que los datos obligatorios existan.
     */
    public Reservation build() {
        validate();

        Reservation reservation = new Reservation(
                reservationCode,
                passenger,
                flight,
                seat,
                basePrice,
                daysInAdvance,
                new ArrayList<>(additionalServices),
                pricingStrategy
        );

        reservation.calculatePrice();

        return reservation;
    }

    private void validate() {
        if (reservationCode == null || reservationCode.isBlank()) {
            throw new IllegalStateException(
                    "El código de reserva es obligatorio."
            );
        }

        if (passenger == null) {
            throw new IllegalStateException(
                    "El pasajero es obligatorio."
            );
        }

        if (flight == null) {
            throw new IllegalStateException(
                    "El vuelo es obligatorio."
            );
        }

        if (seat == null) {
            throw new IllegalStateException(
                    "El asiento es obligatorio."
            );
        }

        if (pricingStrategy == null) {
            throw new IllegalStateException(
                    "La estrategia de precio es obligatoria."
            );
        }

        if (basePrice <= 0) {
            throw new IllegalStateException(
                    "El precio base debe ser mayor que cero."
            );
        }
    }
    
}
