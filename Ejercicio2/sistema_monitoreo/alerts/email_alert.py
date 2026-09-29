from alerts.alert_observer import AlertObserver

class EmailAlert(AlertObserver):

    def update(self, service_name, metric, value):
        print(
            f"[EMAIL] Alerta: {service_name} "
            f"superó el umbral de {metric}. Valor actual: {value}%"
        )