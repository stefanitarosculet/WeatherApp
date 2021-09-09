import requests
from twilio.rest import Client

account_sid = 'ACb8c93f45290d3c15451c8e47e9495508'
auth_token = '8e60ac431985aa912b5aa17e47f905c5'

api_key = "a195489e4c0476565116846673a3fdb4"
parameters = {
    "lat":43.006890,
    "lon":131.926630,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}
response = requests.get(url = "https://api.openweathermap.org/data/2.5/onecall", params =parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    for each in hour["weather"]:
        if each["id"] < 700:
            will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Is going to rain today. Remember to bring an umbrella ☂️.",
        from_='+447401269901',
        to='+447462555605'
    )
    print(message.status)

