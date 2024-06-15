# https://www.meteomatics.com/en/sign-up-weather-api-test-account/

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = os.environ.get("OWM_API")
api_key = "/"
twilio_num = "+/"

account_sid = "/"
auth_token = os.environ.get("auth_token")
# detroit
connection = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast?lat=42.331429&lon=-83.045753&cnt=4&appid=/")

print(connection.status_code)
connection.raise_for_status()
data = connection.json()
will_rain = False

weather_slice = data["list"][:4]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Seems like it might rain today, bring an umbrella!⚡",
        from_=twilio_num,
        to='+/'
    )
    print(message.status)
