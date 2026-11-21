from abc import ABC, abstractmethod

class ThresholdStrategy(ABC):
    """
    Contrato para las estrategias de evaluación de umbrales.
    """

    @abstractmethod
    def evaluate(self, value: float, threshold: float) -> bool:
        """Determina si una métrica supera el umbral."""
        pass

class GreaterThanThresholdStrategy(ThresholdStrategy):
    """
    Activa la alerta únicamente cuando el valor
    es estrictamente mayor que el umbral.
    """

    def evaluate(self, value: float, threshold: float) -> bool:
        return value > threshold

class GreaterThanOrEqualThresholdStrategy(ThresholdStrategy):
    """
    Genera una alerta cuando el valor es mayor
    o igual al umbral establecido.
    """

    def evaluate(self, value: float, threshold: float) -> bool:
        return value >= threshold