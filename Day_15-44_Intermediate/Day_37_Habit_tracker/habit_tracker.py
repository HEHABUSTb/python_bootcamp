import requests
from datetime import datetime
from env import API_KEY

USER_NAME = "hehabustb"
GRAPH_ID = "cycling1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

def create_user():
    # https://pixe.la/@hehabustb

    user_param = {
        "token": API_KEY,
        "username": USER_NAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_param)
    print(response.text)
    response.raise_for_status()


def create_graph():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

    params = {
        "id": GRAPH_ID,
        "name": "Cycling graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai",
    }

    headers = {
        "X-USER-TOKEN": API_KEY,
    }

    response = requests.post(url=graph_endpoint, json=params, headers=headers)
    print(response.text)
    response.raise_for_status()

def post_value_to_graph(date: str, value: float):
    endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"

    params = {
        "date": f"{date}",
        "quantity": f"{value}",
    }

    headers = {
        "X-USER-TOKEN": API_KEY,
    }

    response = requests.post(url=endpoint, json=params, headers=headers)
    print(response.text)
    response.raise_for_status()

def put_value_to_graph(date: str, value: float):
    endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"

    params = {
        "quantity": f"{value}",
    }

    headers = {
        "X-USER-TOKEN": API_KEY,
    }

    response = requests.put(url=endpoint, json=params, headers=headers)
    print(response.text)
    response.raise_for_status()



if __name__ == "__main__":
    today = datetime.now().strftime("%Y%m%d")
    # post_value_to_graph(date=today, value=10)
    put_value_to_graph(today, 12)