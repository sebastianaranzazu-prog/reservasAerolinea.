class MonitoringConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not hasattr(self, "cpu_threshold"):
            self.cpu_threshold = 80
            self.memory_threshold = 80
            self.monitoring_interval = 60

def check_memory(self, service_name, memory_usage):
    threshold = self.config.memory_threshold

    print(
        f"Monitoreando {service_name} - "
        f"Memoria: {memory_usage}% - "
        f"Umbral: {threshold}%"
    )

    if memory_usage > threshold:
        print("⚠️ Umbral de memoria superado.")
        self.notify(service_name, "Memoria", memory_usage)