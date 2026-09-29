

import domain.EconomyPricing;
import domain.Flight;
import domain.Passenger;
import domain.PremiumPricing;
import domain.Reservation;
import domain.ReservationBuilder;
import domain.Seat;
import infraestructura.AppNotifier;
import infraestructura.EmailNotifier;
import infraestructura.SMSNotifier;
import usecase.CancelReservationUseCase;
import usecase.ConfirmReservationUseCase;
import usecase.CreateReservationUseCase;
import usecase.UpgradeReservationUseCase;

public class Main {
    public static void main(String[] args) {

        /*
         * 1. Crear los datos básicos.
         */
        Passenger passenger = new Passenger(
                "P001",
                "Ana García",
                "ana@correo.com",
                "3001234567"
        );

        /* Vuelo */
        Flight flight = new Flight(
                "AV101",
                "Bogotá",
                "Madrid",
                800.0,
                "2026-12-20"
        );

        /* Asiento */
        Seat seat = new Seat(
                "12A",
                "Ventana"
        );

        /*
         * 2. Crear una reserva utilizando Builder.
         */
        ReservationBuilder builder = new ReservationBuilder()
                .withReservationCode("RES-1001")
                .withPassenger(passenger)
                .withFlight(flight)
                .withSeat(seat)
                .withBasePrice(800.0)
                .withDaysInAdvance(40)
                .withPricingStrategy(new EconomyPricing())
                .addService("Equipaje adicional")
                .addService("Selección de asiento");

        /* creacion del caso de la reserva */
        CreateReservationUseCase createUseCase =
                new CreateReservationUseCase();

        Reservation reservation =
                createUseCase.execute(builder);

        /*
         * 3. Registrar observadores.
         */
        reservation.addObserver(
                new EmailNotifier(passenger.getEmail())
        );

        reservation.addObserver(
                new SMSNotifier(passenger.getPhone())
        );

        reservation.addObserver(
                new AppNotifier(passenger.getId())
        );

        System.out.println(reservation);
        

        /*
         * 4. Confirmar la reserva.
         */
        ConfirmReservationUseCase confirmUseCase =
                new ConfirmReservationUseCase();

        confirmUseCase.execute(reservation);

        System.out.println(reservation);

        /*
         * 5. Realizar upgrade a clase premium.
         */
        UpgradeReservationUseCase upgradeUseCase =
                new UpgradeReservationUseCase();

        upgradeUseCase.execute(
                reservation,
                new PremiumPricing()
        );

        /*
         * 6. Realizar check-in.
         */
        reservation.checkIn();

        /*
         * 7. Abordar.
         */
        reservation.board();

        /*
         * 8. Intentar cancelar después de abordar.
         */
        CancelReservationUseCase cancelUseCase =
                new CancelReservationUseCase();

        cancelUseCase.execute(reservation);

        /*
         * 9. Mostrar el resultado final.
         */
        System.out.println(reservation);

    }
}