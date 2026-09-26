package usecase;

import domain.Reservation;
import interfaces.PricingStrategy;

/**
 * Caso de uso para cambiar la categoría de una reserva.
 */

public class UpgradeReservationUseCase {

    public void execute(
            Reservation reservation,
            PricingStrategy newPricingStrategy
    ) {
        reservation.upgrade(newPricingStrategy);
    }
    
}
