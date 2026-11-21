from abc import ABC, abstractmethod
from domain.models.alert_event import AlertEvent


class AlertObserver(ABC):
    """
    Contrato para los componentes que reciben eventos de alerta.
    """

    @abstractmethod
    def update(self, event: AlertEvent) -> None:
        """
        Procesa un evento de alerta.
        """
        pass
