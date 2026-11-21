from application.ports.alert_observer import AlertObserver
from domain.models.alert_event import AlertEvent

class SlackAlert(AlertObserver):
    """
    Observador encargado de representar las alertas de Slack.
    """

    def update(self, event: AlertEvent) -> None:
        print(
            f"[SLACK] Alerta: {event.service_name} "
            f"superó el umbral de {event.metric}. "
            f"Valor actual: {event.value}% "
            f"(Umbral: {event.threshold}%)."
        )
