package domain;

import interfaces.ReservationState;

/**
 * Estado de una reserva confirmada.
 */

public class ConfirmedState implements ReservationState{
    
     @Override
    public void confirm(Reservation reservation) {
        System.out.println(
                "La reserva ya está confirmada."
        );
    }

    @Override
    public void cancel(Reservation reservation) {
        reservation.changeState(new CancelledState());
    }

    @Override
    public void modify(Reservation reservation) {
        System.out.println(
                "Una reserva confirmada no puede modificarse directamente."
        );
    }

    @Override
    public void checkIn(Reservation reservation) {
        reservation.changeState(new CheckInState());
    }

    @Override
    public void board(Reservation reservation) {
        System.out.println(
                "Primero se debe realizar el check-in."
        );
    }

    @Override
    public String getName() {
        return "CONFIRMADA";
    }

}
