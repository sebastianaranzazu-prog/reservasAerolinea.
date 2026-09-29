package domain;

import interfaces.PricingStrategy;

/**
 * Estrategia de precios para primera clase.
 */

public class FirstClassPricing implements PricingStrategy {

    /**
     * Calcula el precio de una reserva.
     *
     * @param flight Vuelo de la reserva.
     * @param daysInAdvance Días de anticipación.
     * @param additionalServices Servicios adicionales.
     * @return Precio de la reserva.
     */
    @Override
    public double calculatePrice(
            Flight flight,
            int daysInAdvance,
            double additionalServices
    ) {
        double price = flight.getBasePrice() * 2.20;

        if (daysInAdvance >= 60) {
            price = price * 0.95;
        }

        return price + additionalServices;
    }
    
}
