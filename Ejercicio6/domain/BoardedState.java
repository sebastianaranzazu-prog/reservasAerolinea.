package domain;

import interfaces.ReservationState;

/**
 * Estado final que indica que el pasajero ya abordó.
 */

public class BoardedState implements ReservationState {

     @Override
    public void confirm(Reservation reservation) {
        System.out.println(
                "El pasajero ya abordó el vuelo."
        );
    }

    @Override
    public void cancel(Reservation reservation) {
        System.out.println(
                "No se puede cancelar una reserva abordada."
        );
    }

    @Override
    public void modify(Reservation reservation) {
        System.out.println(
                "No se puede modificar una reserva abordada."
        );
    }

    @Override
    public void checkIn(Reservation reservation) {
        System.out.println(
                "El pasajero ya realizó el check-in."
        );
    }

    @Override
    public void board(Reservation reservation) {
        System.out.println(
                "El pasajero ya abordó."
        );
    }

    @Override
    public String getName() {
        return "ABORDADA";
    }
    
}
