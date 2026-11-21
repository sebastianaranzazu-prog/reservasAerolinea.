class LegacyMonitoringAPI:
    """
    Simula una API antigua que proporciona métricas
    de un microservicio.
    """

    def get_metrics(self) -> dict:
        return {
            "cpu_usage_percent": 95,
            "memory_usage_percent": 88
        }
