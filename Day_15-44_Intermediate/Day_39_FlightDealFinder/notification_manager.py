from pprint import pprint

from twilio.rest import Client
from env import account_sid, auth_token


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)
        self.from_number = "+19517138313"
        self.to_number = "+48885587735"

    def send_notification(self, message):
        message = self.client.messages.create(
            body=message,
            from_=self.from_number,
            to=self.to_number
        )

        pprint(message)

        return message