import unittest
from application.events.event_dispatcher import EventDispatcher
from application.ports.monitoring_api import MonitoringAPI
from application.ports.alert_observer import AlertObserver
from application.services.monitoring_service import MonitoringService
from domain.models.monitoring_config import MonitoringConfig
from domain.models.alert_event import AlertEvent

from domain.strategies.threshold_strategy import (
    GreaterThanThresholdStrategy,
    GreaterThanOrEqualThresholdStrategy
)

class FakeMonitoringAPI(MonitoringAPI):
    """
    Fuente simulada de métricas para las pruebas.
    """

    def __init__(self, cpu_usage, memory_usage):
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage

    def get_cpu_usage(self):
        return self.cpu_usage

    def get_memory_usage(self):
        return self.memory_usage

class RecordingObserver(AlertObserver):
    """
    Observador que almacena los eventos recibidos.
    """

    def __init__(self):
        self.events = []

    def update(self, event: AlertEvent):
        self.events.append(event)

class MonitoringServiceTests(unittest.TestCase):

    def setUp(self):
        self.dispatcher = EventDispatcher()
        self.observer = RecordingObserver()

        self.dispatcher.subscribe(self.observer)

    def create_service(self, cpu, memory, strategy=None):

        if strategy is None:
            strategy = GreaterThanThresholdStrategy()

        return MonitoringService(
        config=MonitoringConfig(),
        monitoring_api=FakeMonitoringAPI(cpu, memory),
        strategy=strategy,
        event_dispatcher=self.dispatcher
    )

    def test_generates_two_alerts(self):

        service = self.create_service(95, 88)

        events = service.check_service("payments-service")

        self.assertEqual(len(events), 2)

        self.assertEqual(
            [event.metric for event in events],
            ["CPU", "Memoria"]
        )

        self.assertEqual(len(self.observer.events), 2)

    def test_does_not_generate_alerts_below_threshold(self):

        service = self.create_service(70, 65)

        events = service.check_service("payments-service")

        self.assertEqual(len(events), 0)
        self.assertEqual(len(self.observer.events), 0)

    def test_does_not_alert_at_exact_threshold(self):

        service = self.create_service(80, 80)

        events = service.check_service("payments-service")

        self.assertEqual(len(events), 0)
        self.assertEqual(len(self.observer.events), 0)

    def test_generates_only_cpu_alert(self):

        service = self.create_service(95, 70)

        events = service.check_service("payments-service")

        self.assertEqual(len(events), 1)

        self.assertEqual(events[0].metric, "CPU")

        self.assertEqual(len(self.observer.events), 1)

    def test_greater_or_equal_strategy_alerts_at_threshold(self):

        service = self.create_service(
        80,
        70,
        GreaterThanOrEqualThresholdStrategy()
    )

        events = service.check_service("payments-service")

        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].metric, "CPU")
        self.assertEqual(len(self.observer.events), 1)

if __name__ == "__main__":
    unittest.main()