import unittest
from application.events.event_dispatcher import EventDispatcher
from application.ports.alert_observer import AlertObserver
from domain.models.alert_event import AlertEvent

class FailingObserver(AlertObserver):
    """Observador que simula un error."""

    def update(self, event: AlertEvent) -> None:
        raise RuntimeError("Fallo simulado en Slack")

class RecordingObserver(AlertObserver):
    """Observador que registra los eventos recibidos."""

    def __init__(self):
        self.events = []

    def update(self, event: AlertEvent) -> None:
        self.events.append(event)

class EventDispatcherTests(unittest.TestCase):

    def test_failed_observer_does_not_stop_others(self):

        dispatcher = EventDispatcher()

        failing_observer = FailingObserver()
        working_observer = RecordingObserver()

        dispatcher.subscribe(failing_observer)
        dispatcher.subscribe(working_observer)

        event = AlertEvent(
            service_name="payments-service",
            metric="CPU",
            value=95,
            threshold=80
        )

        with self.assertLogs(
            "application.events.event_dispatcher",
            level="ERROR"
        ):
            dispatcher.publish(event)

        self.assertEqual(len(working_observer.events), 1)

        self.assertIs(working_observer.events[0], event)

    def test_same_observer_is_not_registered_twice(self):

        dispatcher = EventDispatcher()
        observer = RecordingObserver()

        dispatcher.subscribe(observer)
        dispatcher.subscribe(observer)

        event = AlertEvent(
            service_name="payments-service",
            metric="CPU",
            value=95,
            threshold=80
        )

        dispatcher.publish(event)

        self.assertEqual(len(observer.events), 1)

    def test_unsubscribed_observer_receives_no_events(self):

        dispatcher = EventDispatcher()
        observer = RecordingObserver()

        dispatcher.subscribe(observer)
        dispatcher.unsubscribe(observer)

        event = AlertEvent(
            service_name="payments-service",
            metric="CPU",
            value=95,
            threshold=80
        )

        dispatcher.publish(event)

        self.assertEqual(len(observer.events), 0)

if __name__ == "__main__":
    unittest.main()