from config.monitoring_config import MonitoringConfig

class MicroserviceMonitor:

    def __init__(self):
        self.config = MonitoringConfig()
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, service_name, metric, value):
        for observer in self.observers:
            observer.update(service_name, metric, value)

    def check_cpu(self, service_name, cpu_usage):
        threshold = self.config.cpu_threshold

        print(
            f"Monitoreando {service_name} - "
            f"CPU: {cpu_usage}% - "
            f"Umbral: {threshold}%"
        )

        if cpu_usage > threshold:
            print("⚠️ Umbral de CPU superado.")
            self.notify(service_name, "CPU", cpu_usage)

    def check_service(self, service_name, monitoring_api):
        cpu_usage = monitoring_api.get_cpu_usage()

        self.check_cpu(service_name, cpu_usage)