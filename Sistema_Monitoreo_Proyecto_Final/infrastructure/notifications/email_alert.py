from application.ports.alert_observer import AlertObserver
from domain.models.alert_event import AlertEvent

class EmailAlert(AlertObserver):
    """
    Observador encargado de representar las alertas por correo.
    """

    def update(self, event: AlertEvent) -> None:
        print(
            f"[EMAIL] Alerta: {event.service_name} "
            f"superó el umbral de {event.metric}. "
            f"Valor actual: {event.value}% "
            f"(Umbral: {event.threshold}%)."
        )
