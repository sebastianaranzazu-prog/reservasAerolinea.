from application.ports.alert_observer import AlertObserver
from domain.models.alert_event import AlertEvent


class TeamsAlert(AlertObserver):
    """
    Observador encargado de representar las alertas de Teams.
    """

    def update(self, event: AlertEvent) -> None:
        print(
            f"[TEAMS] Alerta: {event.service_name} "
            f"superó el umbral de {event.metric}. "
            f"Valor actual: {event.value}% "
            f"(Umbral: {event.threshold}%)."
        )
