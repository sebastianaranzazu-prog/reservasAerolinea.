package usecase;

import domain.Reservation;
import domain.ReservationBuilder;

/**
 * Caso de uso para crear reservas.
 */

public class CreateReservationUseCase {
    
    /**
     * Recibe un Builder y construye una reserva válida.
     */
    public Reservation execute(ReservationBuilder builder) {
        return builder.build();
    }
    
}
