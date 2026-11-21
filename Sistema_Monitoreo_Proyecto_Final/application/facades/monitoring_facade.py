from application.services.monitoring_service import MonitoringService
from application.ports.event_bus import EventBus
from application.ports.alert_observer import AlertObserver
from domain.models.alert_event import AlertEvent

class MonitoringFacade:
    """
    Proporciona un punto de acceso simplificado
    al sistema de monitoreo.
    """
    def __init__(
        self,
        monitoring_service: MonitoringService,
        event_dispatcher: EventBus
    ):
        self._monitoring_service = monitoring_service
        self._event_dispatcher = event_dispatcher

    def add_observer(self, observer: AlertObserver) -> None:
        self._event_dispatcher.subscribe(observer)

    def remove_observer(self, observer: AlertObserver) -> None:
        self._event_dispatcher.unsubscribe(observer)

    def monitor_service(
        self,
        service_name: str
    ) -> list[AlertEvent]:

        return self._monitoring_service.check_service(service_name)