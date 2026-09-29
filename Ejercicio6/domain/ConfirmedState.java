package domain;

import interfaces.ReservationState;

/**
 * Estado de una reserva confirmada.
 */

public class ConfirmedState implements ReservationState{
    
    /* La reserva ya esta confirmada */
     @Override
    public void confirm(Reservation reservation) {
        System.out.println(
                "La reserva ya está confirmada."
        );
    }

    /* La reserva se cancela */
    @Override
    public void cancel(Reservation reservation) {
        reservation.changeState(new CancelledState());
    }

    /* No se puede modificar una reserva confirmada */
    @Override
    public void modify(Reservation reservation) {
        System.out.println(
                "Una reserva confirmada no puede modificarse directamente."
        );
    }

    /* Se pasa al estado de check-in */
    @Override
    public void checkIn(Reservation reservation) {
        reservation.changeState(new CheckInState());
    }

    /* Primero se debe realizar el check-in */
    @Override
    public void board(Reservation reservation) {
        System.out.println(
                "Primero se debe realizar el check-in."
        );
    }

    /* Devuelve el nombre del estado */
    @Override
    public String getName() {
        return "CONFIRMADA";
    }

}
