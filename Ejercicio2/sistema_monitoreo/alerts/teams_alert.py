from alerts.alert_observer import AlertObserver

class TeamsAlert(AlertObserver):

    def update(self, service_name, metric, value):
        print(
            f"[TEAMS] Alerta: {service_name} "
            f"superó el umbral de {metric}. Valor actual: {value}%"
        )
    