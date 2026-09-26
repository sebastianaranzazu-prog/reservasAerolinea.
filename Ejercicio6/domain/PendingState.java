package domain;

import interfaces.ReservationState;

/**
 * Estado inicial de una reserva.
 */

public class PendingState implements ReservationState {

    @Override 
    public void confirm(Reservation reservation) {
        reservation.changeState(new ConfirmedState());    
    }

    @Override 
    public void cancel(Reservation reservation) {
        reservation.changeState(new CancelledState());    
    }

    @Override 
    public void modify(Reservation reservation) {
        
        // reservation.changeState(new PendingState());

        System.out.println(
                "La reserva pendiente puede ser modificada."
        );   
    }

    @Override
    public void checkIn(Reservation reservation) {
        System.out.println(
                "No se puede hacer check-in de una reserva pendiente."
        );
    }

    @Override
    public void board(Reservation reservation) {
        System.out.println(
                "No se puede abordar con una reserva pendiente."
        );
    }

    @Override
    public String getName() {
        return "PENDIENTE";
    }
    
}
