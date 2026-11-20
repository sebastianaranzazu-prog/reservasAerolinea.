from abc import ABC, abstractmethod


class MonitoringAPI(ABC):
    """
    Contrato para las fuentes de métricas del sistema.
    """

    @abstractmethod
    def get_cpu_usage(self) -> float:
        """Devuelve el porcentaje de uso de CPU."""
        pass
