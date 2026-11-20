import logging
from application.ports.alert_observer import AlertObserver
from domain.models.alert_event import AlertEvent

logger = logging.getLogger(__name__)

class EventDispatcher:
    """
    Administra los observadores y distribuye los eventos de alerta.
    """

    def __init__(self):
        self._observers: list[AlertObserver] = []

    def subscribe(self, observer: AlertObserver) -> None:
        """Registra un observador."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: AlertObserver) -> None:
        """Elimina un observador si está registrado."""
        if observer in self._observers:
            self._observers.remove(observer)

    def publish(self, event: AlertEvent) -> None:
        """Distribuye un evento a los observadores registrados."""

        for observer in tuple(self._observers):
            try:
                observer.update(event)

            except Exception:
                logger.exception(
                    "Error notificando al observador %s",
                    type(observer).__name__
                )
