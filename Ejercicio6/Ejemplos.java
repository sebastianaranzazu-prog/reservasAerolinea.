import domain.Reservation;
import interfaces.PricingStrategy;

public class Ejemplos {

    /*
     * Forma genera usar múltiples condicionales para estados
     *
     */

    if (status == PENDING) {
    if (operation.equals("confirm")) {
        // ...
    } else if (operation.equals("cancel")) {
        // ...
    }
    } else if (status == CONFIRMED) {
        // ...
    }

    /*
     * Builder permite crear la reserva paso a paso y solamente agregar las características necesarias
     */
    new ReservationBuilder()
        .withPassenger(passenger)
        .withFlight(flight)
        .withSeat("12A")
        .withSeatClass(SeatClass.PREMIUM)
        .addService(AdditionalService.MEAL)
        .withPreferences("Asiento de pasillo")
        .withPricingStrategy(new PremiumPricing())
        .build();

    /**
     * Estrategia para temporada alta.
     */

    /* 
        public class HighSeasonPricing implements PricingStrategy {

            @Override
            public double calculatePrice(Reservation reservation) {
                double price = reservation.getBasePrice() * 1.25;

                for (AdditionalService service :
                        reservation.getAdditionalServices()) {
                    price += service.getPrice();
                }

                return price;
            }
        }
    */

    /* Luego se utiliza así: */

    /*
    reservation.setPricingStrategy(
        new HighSeasonPricing()
    );
    */



}   
