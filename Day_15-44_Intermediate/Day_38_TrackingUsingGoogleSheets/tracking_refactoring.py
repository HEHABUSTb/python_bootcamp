from datetime import datetime
from operator import itemgetter
from dataclasses import dataclass
from pprint import pprint
from types import SimpleNamespace

import requests

APP_ID = ""
API_KEY = ""
SHEETY_KEY = ""


# Calculate calories burned from a natural language exercise description.
@dataclass
class Exercise:
    subject: Subject

    @property
    def _auth_headers(self) -> dict:
        return {"x-app-id": APP_ID, "x-app-key": API_KEY}

    def post_to_google_sheet(self) -> dict:
        today = datetime.now()

        url = f"https://api.sheety.co/{SHEETY_KEY}/myWorkouts/workouts"

        name, duration, calories = self.get_calories()

        payload = {"workout":
                       {"date": today.strftime("%d/%m/%Y"),
                        "time": today.strftime("%H:%M:%S"),
                        "exercise": name,
                        "duration": duration,
                        "calories": calories}}

        return self._post(url, payload, {})

    def get_calories(self):
        base_url = 'https://app.100daysofpython.dev'
        endpoint = "/v1/nutrition/natural/exercise"

        exercise_text = input("Tell me which exercises you did: ")

        url = f"{base_url}{endpoint}"
        payload = {"query": exercise_text, **vars(self.subject)}

        result = self._post(url, payload, self._auth_headers)
        exercise = result['exercises'][0]

        return itemgetter("name", "duration_min", "nf_calories")(exercise)

    @staticmethod
    def _post(endpoint: str, payload: dict, headers: dict) -> dict:
        response = requests.post(url=endpoint, json=payload, headers=headers, timeout=5)
        pprint(response.json())
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    Subject = SimpleNamespace(weight_kg=67, height_cm=168, age=34, gender='male')
    exercise = Exercise(Subject)
    exercise.post_to_google_sheet()