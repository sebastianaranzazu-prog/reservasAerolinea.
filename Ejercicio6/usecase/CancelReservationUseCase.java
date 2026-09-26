package usecase;

import domain.Reservation;

public class CancelReservationUseCase {

    public void execute(Reservation reservation) {
        reservation.cancel();
    }
    
}
