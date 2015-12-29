from elastalert.alerts import Alerter, BasicMatchString
import requests
import json

class SlackAlerter(Alerter, BasicMatchString):
    required_options = set(["slack_webhook_url"])
    def alert(self, matches):
        for match in matches:
            data = {'text':  str(BasicMatchString(self.rule, match)) }
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post(self.rule['slack_webhook_url'], data=json.dumps(data), headers=headers)

    def get_info(self):
        return {'type': 'Slack alerter'}
