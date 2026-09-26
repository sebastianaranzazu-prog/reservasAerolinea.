package infraestructura;

import interfaces.ReservationObserver;

/**
 * Envía notificaciones por correo electrónico.
 */

public class EmailNotifier implements ReservationObserver {

    private final String email;

    public EmailNotifier(String email) {
        this.email = email;
    }

    @Override
    public void update(String message) {
        System.out.println(
                "[EMAIL enviado a " + email + "]: " + message
        );
    }
    
}
