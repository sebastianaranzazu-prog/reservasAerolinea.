package domain;

import interfaces.PricingStrategy;

/**
 * Estrategia de precios para clase económica.
 */

public class EconomyPricing implements PricingStrategy {
    
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
        double price = flight.getBasePrice();

        /*
         * Si se compra con al menos 30 días de anticipación,
         * se aplica un descuento del 10%.
         */
        if (daysInAdvance >= 30) {
            price = price * 0.10;
        }

        return price + additionalServices;
    }

}
