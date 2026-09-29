package domain;

import interfaces.PricingStrategy;

/**
 * Estrategia de precios para clase premium.
 */
public class PremiumPricing implements PricingStrategy{

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
        double price = flight.getBasePrice() * 1.40;

        /*
         * La clase premium puede tener un pequeño descuento
         * cuando se compra con mucha anticipación.
         */
        if (daysInAdvance >= 45) {
            price = price * 0.95;
        }

        return price + additionalServices;
    }
    
}
