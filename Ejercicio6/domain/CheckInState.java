package domain;

import interfaces.ReservationState;

/**
 * Estado posterior al check-in.
 */

public class CheckInState implements ReservationState{

     @Override
    public void confirm(Reservation reservation) {
        System.out.println(
                "La reserva ya pasó por confirmación."
        );
    }

    @Override
    public void cancel(Reservation reservation) {
        System.out.println(
                "La cancelación después del check-in requiere validación especial."
        );
    }

    @Override
    public void modify(Reservation reservation) {
        System.out.println(
                "No se puede modificar una reserva después del check-in."
        );
    }

    @Override
    public void checkIn(Reservation reservation) {
        System.out.println(
                "El check-in ya fue realizado."
        );
    }

    @Override
    public void board(Reservation reservation) {
        reservation.changeState(new BoardedState());
    }

    @Override
    public String getName() {
        return "CHECK-IN REALIZADO";
    }
    
}
