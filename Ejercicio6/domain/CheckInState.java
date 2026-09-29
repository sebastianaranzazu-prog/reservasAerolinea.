package domain;

import interfaces.ReservationState;

/**
 * Estado posterior al check-in.
 */

public class CheckInState implements ReservationState{

    /** No se puede confirmar una reserva */
     @Override
    public void confirm(Reservation reservation) {
        System.out.println(
                "La reserva ya pasó por confirmación."
        );
    }

    /** No se puede cancelar una reserva */
    @Override
    public void cancel(Reservation reservation) {
        System.out.println(
                "La cancelación después del check-in requiere validación especial."
        );
    }

    /** No se puede modificar una reserva */
    @Override
    public void modify(Reservation reservation) {
        System.out.println(
                "No se puede modificar una reserva después del check-in."
        );
    }

    /** No se puede hacer check-in de una reserva */
    @Override
    public void checkIn(Reservation reservation) {
        System.out.println(
                "El check-in ya fue realizado."
        );
    }

    /** Se pasa al estado de abordado */
    @Override
    public void board(Reservation reservation) {
        reservation.changeState(new BoardedState());
    }

    /** Devuelve el nombre del estado */
    @Override
    public String getName() {
        return "CHECK-IN REALIZADO";
    }
    
}
