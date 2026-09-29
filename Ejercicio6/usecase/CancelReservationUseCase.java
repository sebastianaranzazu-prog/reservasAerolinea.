package usecase;

import domain.Reservation;

/* 
 * Caso de uso para cancelar una reserva
 */
public class CancelReservationUseCase {

    public void execute(Reservation reservation) {
        reservation.cancel();
    }
    
}
