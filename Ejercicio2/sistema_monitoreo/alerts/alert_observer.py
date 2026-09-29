from abc import ABC, abstractmethod

class AlertObserver(ABC):

    @abstractmethod
    def update(self, service_name, metric, value):
        pass
