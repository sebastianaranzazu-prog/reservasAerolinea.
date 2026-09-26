package infraestructura;

import interfaces.ReservationObserver;

/**
 * Envía notificaciones mediante SMS.
 */

public class SMSNotifier implements ReservationObserver{

    private final String phone;

    public SMSNotifier(String phone) {
        this.phone = phone;
    }

    @Override
    public void update(String message) {
        System.out.println(
                "[SMS enviado al número " + phone + "]: " + message
        );
    }
    
}
