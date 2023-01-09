from twilio.rest import Client
import os
import datetime
import requests
from operator import itemgetter
from dotenv import load_dotenv
load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        # Your Account SID from twilio.com/console
        self.account_sid = os.getenv('ACCOUNT_SID_TWILO')
        # Your Auth Token from twilio.com/console
        self.auth_token = os.getenv('AUTH_TOKEN')
        self.client = Client(self.account_sid, self.auth_token)

    def sendNotify(self, messages):
        message = self.client.messages.create(
            to="+9720503339698",
            from_="+13853964007",
            body=messages)
        print(message.sid)
