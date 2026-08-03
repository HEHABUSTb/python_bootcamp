from datetime import datetime
from operator import itemgetter
from pprint import pprint
from types import SimpleNamespace

import requests

APP_ID = ""
API_KEY = ""
SHEETY_KEY = ""


# Calculate calories burned from a natural language exercise description.
Subject = SimpleNamespace(weight_kg = 67, height_cm = 168, age=34, gender='male')

base_url = 'https://app.100daysofpython.dev'
endpoint = "/v1/nutrition/natural/exercise"

print(f"Subject: {vars(Subject)}")
exercise_text = input("Tell me which exercises you did: ")

payload = { "query": exercise_text, **vars(Subject)}
headers = { "x-app-id": APP_ID, "x-app-key": API_KEY }

response = requests.post(url=f"{base_url}{endpoint}", json=payload, headers=headers, timeout=5)
pprint(response.json())

exercise = response.json()['exercises'][0]

name, duration, calories = itemgetter("name", "duration_min", "nf_calories")(exercise)

# Send this data to Google sheets
today = datetime.now()


url = f"https://api.sheety.co/{SHEETY_KEY}/myWorkouts/workouts"


payload = { "workout":
                { "date": today.strftime("%d/%m/%Y"),
                  "time": today.strftime("%H:%M:%S"),
                  "exercise": name,
                  "duration": duration,
                  "calories": calories }}

response = requests.post(url=url, json=payload, timeout=5)
