import unittest
from application.ports.event_bus import EventBus
from application.ports.monitoring_api import MonitoringAPI
from application.services.monitoring_service import MonitoringService
from domain.models.monitoring_config import MonitoringConfig
from domain.strategies.threshold_strategy import GreaterThanThresholdStrategy

class FakeMonitoringAPI(MonitoringAPI):

    def get_cpu_usage(self):
        return 95

    def get_memory_usage(self):
        return 70

class RecordingEventBus(EventBus):
    """
    Implementación alternativa del contrato EventBus.
    Registra eventos sin utilizar EventDispatcher.
    """

    def __init__(self):
        self.events = []
        self.observers = []

    def subscribe(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def publish(self, event):
        self.events.append(event)

class DependencyInversionTests(unittest.TestCase):

    def test_service_accepts_alternative_event_bus(self):

        event_bus = RecordingEventBus()

        service = MonitoringService(
            config=MonitoringConfig(),
            monitoring_api=FakeMonitoringAPI(),
            strategy=GreaterThanThresholdStrategy(),
            event_dispatcher=event_bus
        )
        events = service.check_service("payments-service")

        self.assertEqual(len(events), 1)
        self.assertEqual(len(event_bus.events), 1)

        self.assertEqual(
            event_bus.events[0].metric,
            "CPU"
        )
if __name__ == "__main__":
    unittest.main()