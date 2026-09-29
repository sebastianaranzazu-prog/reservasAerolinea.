from monitoring.microservice_monitor import MicroserviceMonitor
from alerts.email_alert import EmailAlert
from alerts.slack_alert import SlackAlert
from alerts.sms_alert import SMSAlert
from alerts.teams_alert import TeamsAlert
from adapters.legacy_monitoring_api import LegacyMonitoringAPI
from adapters.legacy_monitoring_adapter import LegacyMonitoringAdapter


class MonitoringFacade:

    def __init__(self):
        self.monitor = MicroserviceMonitor()

    def add_email_alert(self):
        email = EmailAlert()
        self.monitor.attach(email)

    def add_slack_alert(self):
        slack = SlackAlert()
        self.monitor.attach(slack)

    def add_sms_alert(self):
        sms = SMSAlert()
        self.monitor.attach(sms)

    def add_teams_alert(self):
        teams = TeamsAlert()
        self.monitor.attach(teams)

    def monitor_legacy_service(self, service_name):
        legacy_api = LegacyMonitoringAPI()

        adapter = LegacyMonitoringAdapter(legacy_api)

        self.monitor.check_service(service_name, adapter)