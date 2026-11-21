import logging
from application.ports.event_bus import EventBus
from application.ports.alert_observer import AlertObserver
from domain.models.alert_event import AlertEvent

logger = logging.getLogger(__name__)

class EventDispatcher(EventBus):
    """
    Implementación concreta del contrato EventBus.
    Administra observadores y distribuye eventos de alerta.
    """

    def __init__(self):
        self._observers: list[AlertObserver] = []

    def subscribe(self, observer: AlertObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: AlertObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def publish(self, event: AlertEvent) -> None:
        for observer in tuple(self._observers):
            try:
                observer.update(event)

            except Exception:
                logger.exception(
                    "Error notificando al observador %s",
                    type(observer).__name__
                )