package infraestructura;

import interfaces.ReservationObserver;

/**
 * Envía notificaciones a una aplicación móvil.
 */

public class AppNotifier implements ReservationObserver{
    
     private final String userId;

    public AppNotifier(String userId) {
        this.userId = userId;
    }

    @Override
    public void update(String message) {
        System.out.println(
                "[APP - usuario " + userId + "]: " + message
        );
    }
    
    
    /* 
     @Override
    public void update(String message) {
        System.out.println("Notificación de la app: " + message);
    }
    */
   
    
}
