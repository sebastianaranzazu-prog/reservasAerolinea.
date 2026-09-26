package usecase;

import domain.Reservation;

/**
 * Caso de uso para confirmar una reserva.
 */

public class ConfirmReservationUseCase {
    public void execute(Reservation reservation) {
        reservation.confirm();
        reservation.processPayment();
    }
    
}
