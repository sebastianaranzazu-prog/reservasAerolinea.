import unittest
from dataclasses import FrozenInstanceError
from domain.models.monitoring_config import MonitoringConfig

class MonitoringConfigTests(unittest.TestCase):

    def test_default_configuration(self):
        config = MonitoringConfig()

        self.assertEqual(config.cpu_threshold, 80.0)
        self.assertEqual(config.memory_threshold, 80.0)
        self.assertEqual(config.monitoring_interval, 60)

    def test_rejects_cpu_threshold_above_100(self):
        with self.assertRaises(ValueError):
            MonitoringConfig(cpu_threshold=120)

    def test_rejects_memory_threshold_below_zero(self):
        with self.assertRaises(ValueError):
            MonitoringConfig(memory_threshold=-10)

    def test_rejects_boolean_threshold(self):
        with self.assertRaises(ValueError):
            MonitoringConfig(cpu_threshold=True)

    def test_rejects_zero_interval(self):
        with self.assertRaises(ValueError):
            MonitoringConfig(monitoring_interval=0)

    def test_configuration_is_immutable(self):
        config = MonitoringConfig()

        with self.assertRaises(FrozenInstanceError):
            config.cpu_threshold = 90

if __name__ == "__main__":
    unittest.main()
