package interfaces;

import domain.Reservation;

/**
 * Define las operaciones que cada estado de una reserva debe manejar.
 */

public interface ReservationState {
    void confirm(Reservation reservation);
    void cancel(Reservation reservation);
    void modify(Reservation reservation);
    void checkIn(Reservation reservation);
    void board(Reservation reservation);
    String getName();
}
