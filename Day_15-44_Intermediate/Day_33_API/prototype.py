import requests
from datetime import datetime
import re

MY_LAT = 52.229675
MY_LONG = 21.012230

response = requests.get(url="http://api.open-notify.org/iss-now.json")
#print(response)

code = response.status_code
response.raise_for_status()
assert code == 200, f"Status code not equal 200 actual status code '{code}'"

data = response.json()
#print(data)




parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
#print(sunset)


def get_time(string: str):
    pattern = r"\d{2}:\d{2}:\d{2}"
    match = re.search(pattern=pattern, string=string)
    return match.group()

print(get_time(sunrise))
print(get_time(sunset))
print(datetime.now().time())
