import requests
from types import SimpleNamespace
from twilio.rest import Client

# twilio creds
account_sid = "AC0b1a42feba443c78f71ba8ad7b743380"
auth_token = "5db80a87e9ab19a8acca01f0597cc076"

# For search lat and lon use https://www.latlong.net/
# Or API https://openweathermap.org/api/geocoding-api?collection=other
MyCity = SimpleNamespace(name=r"Warszawa", api_key=r"35d2fcd3a40cc1432ef2f8460ce4b1ef", lat=52.22, lon=21.01)

endpoint = r"https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": MyCity.lat,
    "lon": MyCity.lon,
    "appid": MyCity.api_key,
    "cnt": 4,
}

# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={MyCity.lat}&lon={MyCity.lon}&appid={MyCity.api_key}")
response = requests.get(endpoint, params=weather_params)

data = response.json()
print(f"Status code: {response.status_code}")

weathers = data["list"]
bring_umbrela = False

for weather in weathers:
    # print(f"Weather ID: {weather["weather"][0]["id"]}")
    if weather["weather"][0]["id"] < 600:
        # print("bring_umbrela")
        bring_umbrela = True

number = +19517138313

client = Client(account_sid, auth_token)

if bring_umbrela:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_= "+19517138313",
        to='+48885587735'
    )
    print(f"Bring umbrela it would be a rain!")
else:
    message = client.messages.create(
        body="Sunny days ahead!",
        from_="+19517138313",
        to='+48885587735'
    )


print(f"Message status: {message.status}")
print(data)
