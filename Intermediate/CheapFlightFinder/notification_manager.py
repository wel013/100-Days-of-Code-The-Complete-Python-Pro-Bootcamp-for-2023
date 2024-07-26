import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = os.environ.get("API_KEY")

account_sid = os.environ.get("SID")
auth_token =  os.environ.get("TOKEN")


class NotificationManager:

    def __init__(self, origin, origina_city, dest, dest_city, depart, return_date, price, stops, number):
        self.original = origin
        self.original_city = origina_city
        self.dest = dest
        self.dest_city = dest_city
        self.depart = depart
        self.return_date = return_date
        self.price = price
        self.stops = stops
        self.number = number

    def send_message(self):
        client = Client(account_sid, auth_token)
        message_body = (
            f"There is a new cheap flight from {self.original_city} ({self.original}) to "
            f"{self.dest_city} ({self.dest}) leaves on {self.depart} and returns on {self.return_date} at {self.price} with {self.stops} stop overs."
        )
        print(message_body)
        message = client.messages.create(
            body=message_body,
            from_=twilio_num,
            to=self.number
        )
        print(message.status)
