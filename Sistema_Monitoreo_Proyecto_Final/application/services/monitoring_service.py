from application.ports.monitoring_api import MonitoringAPI
import logging
from application.ports.event_bus import EventBus
from domain.models.monitoring_config import MonitoringConfig
from domain.models.alert_event import AlertEvent
from domain.strategies.threshold_strategy import ThresholdStrategy
logger = logging.getLogger(__name__)

class MonitoringService:
    """
    Coordina la evaluación de métricas y la generación de eventos.
    """

    def __init__(
        self,
        config: MonitoringConfig,
        monitoring_api: MonitoringAPI,
        strategy: ThresholdStrategy,
        event_dispatcher: EventBus
    ):
        self._config = config
        self._monitoring_api = monitoring_api
        self._strategy = strategy
        self._event_dispatcher = event_dispatcher

    def _evaluate_metric(
        self,
        service_name: str,
        metric: str,
        value: float,
        threshold: float
    ) -> AlertEvent | None:
        """
        Evalúa una métrica y publica un evento si supera el umbral.
        """

        logger.info(
    "Monitoreando %s - %s: %s%% - Umbral: %s%%",
        service_name,
        metric,
        value,
        threshold
        )

        if not self._strategy.evaluate(value, threshold):
            return None

        event = AlertEvent(
            service_name=service_name,
            metric=metric,
            value=value,
            threshold=threshold
        )

        self._event_dispatcher.publish(event)

        return event

    def check_service(self, service_name: str) -> list[AlertEvent]:
        """
        Comprueba CPU y memoria del microservicio.

        Devuelve los eventos generados durante la comprobación.
        """

        generated_events = []

        cpu_usage = self._monitoring_api.get_cpu_usage()

        cpu_event = self._evaluate_metric(
            service_name,
            "CPU",
            cpu_usage,
            self._config.cpu_threshold
        )

        if cpu_event is not None:
            generated_events.append(cpu_event)

        memory_usage = self._monitoring_api.get_memory_usage()

        memory_event = self._evaluate_metric(
            service_name,
            "Memoria",
            memory_usage,
            self._config.memory_threshold
        )

        if memory_event is not None:
            generated_events.append(memory_event)

        return generated_events