package domain;

import interfaces.PricingStrategy;

/**
 * Estrategia de precios para primera clase.
 */

public class FirstClassPricing implements PricingStrategy {

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
