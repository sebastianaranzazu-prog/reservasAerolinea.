from dataclasses import dataclass


@dataclass(frozen=True)
class MonitoringConfig:
    """
    Configuración general del sistema de monitoreo.
    """

    cpu_threshold: float = 80.0
    memory_threshold: float = 80.0
    monitoring_interval: int = 60

    def __post_init__(self):
        self._validate_threshold(
            "cpu_threshold",
            self.cpu_threshold
        )

        self._validate_threshold(
            "memory_threshold",
            self.memory_threshold
        )

        if (
            isinstance(self.monitoring_interval, bool)
            or not isinstance(self.monitoring_interval, int)
            or self.monitoring_interval <= 0
        ):
            raise ValueError(
                "El intervalo debe ser un entero positivo."
            )

    @staticmethod
    def _validate_threshold(name, value):

        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
        ):
            raise ValueError(
                f"{name} debe ser un valor numérico."
            )

        if not 0 <= value <= 100:
            raise ValueError(
                f"{name} debe estar entre 0 y 100."
            )
