from adapters.monitoring_api import MonitoringAPI

# Nuestro Adapter cumple con la norma de MonitoringAPI#
class LegacyMonitoringAdapter(MonitoringAPI):

#Se recibe la API Antigua como parámetro y se implementa el método get_cpu_usage()
# para adaptarse a la interfaz de MonitoringAPI.

    def __init__(self, legacy_api):
        self.legacy_api = legacy_api

    def get_cpu_usage(self):
        data = self.legacy_api.get_metrics()

        return data["cpu_usage_percent"]