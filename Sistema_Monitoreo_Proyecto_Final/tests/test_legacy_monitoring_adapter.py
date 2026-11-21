import unittest
from infrastructure.adapters.legacy_monitoring_adapter import (
    LegacyMonitoringAdapter
)

class FakeLegacyMonitoringAPI:
    """Simula diferentes respuestas de la API antigua."""

    def __init__(self, metrics):
        self.metrics = metrics

    def get_metrics(self):
        return self.metrics

class LegacyMonitoringAdapterTests(unittest.TestCase):

    def create_adapter(self, metrics):
        api = FakeLegacyMonitoringAPI(metrics)
        return LegacyMonitoringAdapter(api)

    def test_returns_cpu_and_memory(self):
        adapter = self.create_adapter({
            "cpu_usage_percent": 95,
            "memory_usage_percent": 88
        })

        self.assertEqual(adapter.get_cpu_usage(), 95.0)
        self.assertEqual(adapter.get_memory_usage(), 88.0)

    def test_rejects_non_dictionary_response(self):
        adapter = self.create_adapter("respuesta incorrecta")

        with self.assertRaises(TypeError):
            adapter.get_cpu_usage()

    def test_rejects_missing_metric(self):
        adapter = self.create_adapter({
            "memory_usage_percent": 70
        })

        with self.assertRaises(ValueError):
            adapter.get_cpu_usage()

    def test_rejects_boolean_metric(self):
        adapter = self.create_adapter({
            "cpu_usage_percent": True
        })

        with self.assertRaises(TypeError):
            adapter.get_cpu_usage()

    def test_rejects_non_numeric_metric(self):
        adapter = self.create_adapter({
            "cpu_usage_percent": "noventa"
        })

        with self.assertRaises(TypeError):
            adapter.get_cpu_usage()

    def test_rejects_cpu_above_100(self):
        adapter = self.create_adapter({
            "cpu_usage_percent": 101
        })

        with self.assertRaises(ValueError):
            adapter.get_cpu_usage()

    def test_rejects_negative_memory(self):
        adapter = self.create_adapter({
            "memory_usage_percent": -10
        })

        with self.assertRaises(ValueError):
            adapter.get_memory_usage()

if __name__ == "__main__":
    unittest.main()
