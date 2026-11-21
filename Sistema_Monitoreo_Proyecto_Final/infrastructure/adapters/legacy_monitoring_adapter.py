from application.ports.monitoring_api import MonitoringAPI

class LegacyMonitoringAdapter(MonitoringAPI):
    """
    Adapta la API antigua al contrato MonitoringAPI.
    """

    def __init__(self, legacy_api):
        self._legacy_api = legacy_api

    def _get_metric(self, metric_name: str) -> float:
        metrics = self._legacy_api.get_metrics()

        if not isinstance(metrics, dict):
            raise TypeError(
                "La API antigua debe devolver un diccionario."
            )

        if metric_name not in metrics:
            raise ValueError(
                f"La API no contiene la métrica {metric_name}."
            )

        value = metrics[metric_name]

        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            raise TypeError(
                f"La métrica {metric_name} debe ser numérica."
            )

        if not 0 <= value <= 100:
            raise ValueError(
                f"La métrica {metric_name} debe estar entre 0 y 100."
            )

        return float(value)

    def get_cpu_usage(self) -> float:
        return self._get_metric("cpu_usage_percent")

    def get_memory_usage(self) -> float:
        return self._get_metric("memory_usage_percent")