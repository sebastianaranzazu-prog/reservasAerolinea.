from abc import ABC, abstractmethod
from domain.entities import Order


class OrderRepository(ABC):
    """
    Contrato para persistencia de órdenes.
    La infraestructura debe implementar esta interfaz.
    """

    @abstractmethod
    def save(self, order: Order):
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Order:
        pass