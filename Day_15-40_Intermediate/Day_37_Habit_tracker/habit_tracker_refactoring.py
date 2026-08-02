import requests
import logging
from dataclasses import dataclass

from datetime import datetime
from env import API_KEY

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

PIXELA_BASE_URL = "https://pixe.la/v1/users"


@dataclass
class PixelaClient:
    user_name: str
    token: str
    graph_id: str

    @property
    def _auth_headers(self) -> dict:
        return {"X-USER-TOKEN": self.token}

    def create_user(self):
        payload = {
            "token": self.token,
            "username": self.user_name,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

        return self._post(PIXELA_BASE_URL, payload, headers={})

    def create_graph(self, name: str, unit: str, graph_type: str = "float", color: str = "ajisai") -> dict:
        endpoint = f"{PIXELA_BASE_URL}/{self.user_name}/graphs"

        payload = {
            "id": self.graph_id,
            "name": name,
            "unit": unit,
            "type": graph_type,
            "color": color,
        }

        return self._post(endpoint, payload, headers=self._auth_headers)

    def post_value(self, date: str, value: float) -> dict:
        endpoint = f"{PIXELA_BASE_URL}/{self.user_name}/graphs/{self.graph_id}"
        payload = {"date": date, "quantity": str(value)}
        return self._post(endpoint, payload, headers=self._auth_headers)

    def update_value(self, date: str, value: float) -> dict:
        endpoint = f"{PIXELA_BASE_URL}/{self.user_name}/graphs/{self.graph_id}/{date}"
        payload = {"quantity": str(value)}
        return self._put(endpoint, payload, headers=self._auth_headers)

    @staticmethod
    def _post(endpoint: str, payload: dict, headers: dict) -> dict:
        response = requests.post(url=endpoint, json=payload, headers=headers, timeout=10)
        logger.info("POST %s -> %s: %s", endpoint, response.status_code, response.text)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _put(endpoint: str, payload: dict, headers: dict) -> dict:
        response = requests.put(url=endpoint, json=payload, headers=headers, timeout=10)
        logger.info("PUT %s -> %s: %s", endpoint, response.status_code, response.text)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    tracker = PixelaClient(user_name="hehabustb", token=API_KEY, graph_id="cycling1")
    today = datetime.now().strftime("%Y%m%d")

    # tracker.create_user()
    # tracker.create_graph(name="Cycling graph", unit="Km")
    # tracker.post_value(date=today, value=10)
    tracker.update_value(date=today, value=13)

