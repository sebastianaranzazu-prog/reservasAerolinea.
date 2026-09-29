from alerts.alert_observer import AlertObserver

class SMSAlert(AlertObserver):

    def update(self, service_name, metric, value):
        print(
            f"[SMS] Alerta: {service_name} "
            f"superó el umbral de {metric}. Valor actual: {value}%"
        )
    