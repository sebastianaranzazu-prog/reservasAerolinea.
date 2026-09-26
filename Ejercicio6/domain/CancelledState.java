package domain;

import interfaces.ReservationState;

/**
 * Estado de una reserva cancelada.
 */

public class CancelledState implements ReservationState {

    @Override
    public void confirm(Reservation reservation) {
        System.out.println("Una reserva cancelada no puede confirmarse.");
    }

    @Override
    public void cancel(Reservation reservation) {
        System.out.println("La reserva ya está cancelada.");
    }

    @Override
    public void modify(Reservation reservation) {
        System.out.println("Una reserva cancelada no puede modificarse."
        );
    }

    @Override
    public void checkIn(Reservation reservation) {
        System.out.println(
                "No se puede hacer check-in de una reserva cancelada."
        );
    }

    @Override
    public void board(Reservation reservation) {
        System.out.println(
                "No se puede abordar con una reserva cancelada."
        );
    }
    
    public String getName() {
        return "CANCELADA";
    }
    
}
