package interfaces;

import domain.Flight;

/**
 * Define el contrato para calcular el precio de una reserva.
 */
public interface  PricingStrategy {

    /**
     * Calcula el precio final de una reserva.
     *
     * @param flight vuelo seleccionado
     * @param daysInAdvance cantidad de días de anticipación
     * @param additionalServices costo de servicios adicionales
     * @return precio total
     */

     double calculatePrice(
            Flight flight,
            int daysInAdvance,
            double additionalServices
    );
    
}
