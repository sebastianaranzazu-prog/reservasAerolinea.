package domain;

import interfaces.ReservationState;

/**
 * Estado final que indica que el pasajero ya abordó.
 */

public class BoardedState implements ReservationState {

    /* No se puede confirmar una reserva abordada */
     @Override
    public void confirm(Reservation reservation) {
        System.out.println(
                "El pasajero ya abordó el vuelo."
        );
    }

    /* No se puede cancelar una reserva abordada */
    @Override
    public void cancel(Reservation reservation) {
        System.out.println(
                "No se puede cancelar una reserva abordada."
        );
    }

    /* No se puede modificar una reserva abordada */
    @Override
    public void modify(Reservation reservation) {
        System.out.println(
                "No se puede modificar una reserva abordada."
        );
    }

    /* No se puede hacer check-in de una reserva abordada */
    @Override
    public void checkIn(Reservation reservation) {
        System.out.println(
                "El pasajero ya realizó el check-in."
        );
    }

    /* No se puede abordar con una reserva abordada */
    @Override
    public void board(Reservation reservation) {
        System.out.println(
                "El pasajero ya abordó."
        );
    }

    /* Devuelve el nombre del estado */
    @Override
    public String getName() {
        return "ABORDADA";
    }
    
}
