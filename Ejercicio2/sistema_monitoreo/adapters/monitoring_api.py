from abc import ABC, abstractmethod

class MonitoringAPI(ABC):

    @abstractmethod
    def get_cpu_usage(self):
        pass