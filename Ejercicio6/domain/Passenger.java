package domain;

/**
 * Representa al pasajero de una reserva.
 */

public class Passenger {

    // Id de reserva
    private final String id;

    // Nombre del pasajero
    private final String name;

    // Email del pasajero
    private final String email;

    // Telefono del pasajero
    private final String phone;

    public Passenger(String id, String name, String email, String phone) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public String getPhone() {
        return phone;
    }

    @Override
    public String toString() {
        return name + " - " + email;
    }
    
}
