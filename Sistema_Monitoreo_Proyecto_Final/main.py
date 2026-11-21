from domain.models.monitoring_config import MonitoringConfig
from domain.strategies.threshold_strategy import GreaterThanThresholdStrategy
from application.events.event_dispatcher import EventDispatcher
from application.services.monitoring_service import MonitoringService
from application.facades.monitoring_facade import MonitoringFacade
from infrastructure.sources.legacy_monitoring_api import LegacyMonitoringAPI
from infrastructure.adapters.legacy_monitoring_adapter import LegacyMonitoringAdapter
from infrastructure.notifications.email_alert import EmailAlert
from infrastructure.notifications.slack_alert import SlackAlert
from infrastructure.notifications.sms_alert import SMSAlert
from infrastructure.notifications.teams_alert import TeamsAlert
import logging
from presentation.cli import run

def build_facade() -> MonitoringFacade:
    """
    Construye los componentes y sus dependencias.
    """

    config = MonitoringConfig()

    legacy_api = LegacyMonitoringAPI()
    monitoring_api = LegacyMonitoringAdapter(legacy_api)

    strategy = GreaterThanThresholdStrategy()

    dispatcher = EventDispatcher()

    dispatcher.subscribe(EmailAlert())
    dispatcher.subscribe(SlackAlert())
    dispatcher.subscribe(SMSAlert())
    dispatcher.subscribe(TeamsAlert())

    monitoring_service = MonitoringService(
        config=config,
        monitoring_api=monitoring_api,
        strategy=strategy,
        event_dispatcher=dispatcher
    )

    return MonitoringFacade(
        monitoring_service=monitoring_service,
        event_dispatcher=dispatcher
    )

def main():
    """
    Punto de entrada de la aplicación.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s"
    )

    facade = build_facade()

    run(facade)

if __name__ == "__main__":
    main()
