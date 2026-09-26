package domain;

/**
 * Representa un asiento del avión.
 *  Ventana, Pasillo y salida de emergencia
 */

public class Seat {
    private final String number;
    private final String type;

    public Seat(String number, String type) {
        this.number = number;
        this.type = type;
    }

    public String getNumber() {
        return number;
    }

    public String getType() {
        return type;
    }

    @Override
    public String toString() {
        return number + " - " + type;
    }

}
