package domain;

import interfaces.ReservationState;

/**
 * Estado de una reserva cancelada.
 */

public class CancelledState implements ReservationState {

    /* No se puede confirmar una reserva cancelada */
    @Override
    public void confirm(Reservation reservation) {
        System.out.println("Una reserva cancelada no puede confirmarse.");
    }

    /* No se puede cancelar una reserva cancelada */
    @Override
    public void cancel(Reservation reservation) {
        System.out.println("La reserva ya está cancelada.");
    }

    /* No se puede modificar una reserva cancelada */
    @Override
    public void modify(Reservation reservation) {
        System.out.println("Una reserva cancelada no puede modificarse."
        );
    }

    /* No se puede hacer check-in de una reserva cancelada */
    @Override
    public void checkIn(Reservation reservation) {
        System.out.println(
                "No se puede hacer check-in de una reserva cancelada."
        );
    }

    /* No se puede abordar con una reserva cancelada */
    @Override
    public void board(Reservation reservation) {
        System.out.println(
                "No se puede abordar con una reserva cancelada."
        );
    }
    
    /* Devuelve el nombre del estado */
    public String getName() {
        return "CANCELADA";
    }
    
}
