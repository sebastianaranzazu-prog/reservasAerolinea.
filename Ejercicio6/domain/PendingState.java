package domain;

import interfaces.ReservationState;

/**
 * Estado inicial de una reserva.
 */

public class PendingState implements ReservationState {

    /** Se pasa al estado de confirmada */
    @Override 
    public void confirm(Reservation reservation) {
        reservation.changeState(new ConfirmedState());    
    }

    /** Se pasa al estado de cancelada */
    @Override 
    public void cancel(Reservation reservation) {
        reservation.changeState(new CancelledState());    
    }

    /** No se puede modificar una reserva pendiente */
    @Override 
    public void modify(Reservation reservation) {
        // reservation.changeState(new PendingState());
        System.out.println(
                "La reserva pendiente puede ser modificada."
        );   
    }

    /** No se puede hacer check-in de una reserva pendiente */
    @Override
    public void checkIn(Reservation reservation) {
        System.out.println(
                "No se puede hacer check-in de una reserva pendiente."
        );
    }

    /** No se puede abordar con una reserva pendiente */
    @Override
    public void board(Reservation reservation) {
        System.out.println(
                "No se puede abordar con una reserva pendiente."
        );
    }

    /** Devuelve el nombre del estado */
    @Override
    public String getName() {
        return "PENDIENTE";
    }
    
}
