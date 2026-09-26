package domain;

/**
 * Representa un vuelo disponible.
 */

public class Flight {
    
    // numero de vuelo
    private final String flightNumber;

    // origen de vuelo
    private final String origin;

    // destino de vuelo
    private final String destination;

    // precio base
    private final double basePrice;

     // fecha de salida
    private final String departureDate;

    public Flight(
            String flightNumber,
            String origin,
            String destination,
            double basePrice,
            String departureDate
    ) {
        this.flightNumber = flightNumber;
        this.origin = origin;
        this.destination = destination;
        this.basePrice = basePrice;
        this.departureDate = departureDate;
    }

    public String getFlightNumber() {
        return flightNumber;
    }

    public String getOrigin() {
        return origin;
    }

    public String getDestination() {
        return destination;
    }

    public double getBasePrice() {
        return basePrice;
    }

    public String getDepartureDate() {
        return departureDate;
    }

    @Override
    public String toString() {
        return flightNumber + " - "
                + origin + " a "
                + destination
                + " - Fecha: "
                + departureDate;
    }
    
}
