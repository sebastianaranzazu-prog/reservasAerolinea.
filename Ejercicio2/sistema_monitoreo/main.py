from facade.monitoring_facade import MonitoringFacade

facade = MonitoringFacade()

# Registramos los canales de alerta
facade.add_email_alert()
facade.add_slack_alert()
facade.add_sms_alert()
facade.add_teams_alert()

# Monitoreamos un microservicio
facade.monitor_legacy_service("payments-service")