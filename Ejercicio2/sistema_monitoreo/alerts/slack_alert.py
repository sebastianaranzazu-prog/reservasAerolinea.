from alerts.alert_observer import AlertObserver

class SlackAlert(AlertObserver):

    def update(self, service_name, metric, value):
        print(
            f"[SLACK] Alerta: {service_name} "
            f"superó el umbral de {metric}. Valor actual: {value}%"
        )