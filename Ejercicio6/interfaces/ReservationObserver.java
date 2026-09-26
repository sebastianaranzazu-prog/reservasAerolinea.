package interfaces;

/**
 * Define el contrato para los observadores de una reserva.
 */

public interface  ReservationObserver {

    /**
     * Se ejecuta cuando ocurre un cambio en la reserva.
     *
     * @param message mensaje de notificación
     */
    
    void update(String message);
    
}
