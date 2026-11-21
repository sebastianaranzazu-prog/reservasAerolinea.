from abc import ABC, abstractmethod
from application.ports.alert_observer import AlertObserver
from domain.models.alert_event import AlertEvent

class EventBus(ABC):
    """
    Contrato para publicar eventos y administrar observadores.
    """

    @abstractmethod
    def subscribe(self, observer: AlertObserver) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: AlertObserver) -> None:
        pass

    @abstractmethod
    def publish(self, event: AlertEvent) -> None:
        pass