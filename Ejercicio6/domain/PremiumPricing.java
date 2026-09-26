package domain;

import interfaces.PricingStrategy;

/**
 * Estrategia de precios para clase premium.
 */
public class PremiumPricing implements PricingStrategy{
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
