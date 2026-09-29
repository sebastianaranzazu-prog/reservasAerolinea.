package usecase;

import domain.Reservation;
import domain.ReservationBuilder;

/**
 * Caso de uso para crear reservas.
 */

public class CreateReservationUseCase {
    
    public Reservation execute(ReservationBuilder builder) {
        return builder.build();
    }
    
}
