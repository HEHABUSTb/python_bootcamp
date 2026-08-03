from pprint import pprint
from types import SimpleNamespace

import requests

APP_ID = "app_8fb51baefdba4b9cafdec15a"
API_KEY = "nix_live_SkCLeXZl43ylLhmWU2Hfkm6lqW92bDW8"


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