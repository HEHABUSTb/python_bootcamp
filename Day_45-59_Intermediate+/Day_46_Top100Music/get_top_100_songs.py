import requests
from bs4 import BeautifulSoup
from datetime import datetime
from types import SimpleNamespace
import ytmusicapi



def validate_date(retry_number: int = 3) -> str | None:

    while retry_number > 0:
        date_str = input("Which year you wanna to travel? Type the date in format YYYY-MM-DD:")

        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            retry_number -= 1
            print(f"Invalid date format or non-existent date. Attempts left: {retry_number}")

    print("No valid date provided. Aborting.")
    return None


def get_best_100_songs(date_str: str = "2026-04-18") -> list[SimpleNamespace]:
    # Scrap html
    response = requests.get(f'https://appbrewery.github.io/bakeboard-hot-100/{date_str}/')
    print(f"Response status code:'{response.status_code}'")
    response.raise_for_status()

    # Find all best 100 songs
    soup = BeautifulSoup(response.content, 'html.parser')

    chart_entries = soup.select("div.chart-entry")
    result = []

    for chart_entry in chart_entries:
        position = chart_entry.select_one("span.chart-entry__rank-number").text

        info = chart_entry.select_one("div.chart-entry__info").text
        info = info.split("\n")
        info.remove("")

        result.append(SimpleNamespace(rank=position, song=info[0], author=info[1]))

    return result


# Get date str in format YYYY-MM-DD
# date_str = validate_date()

best_songs = get_best_100_songs()
print(best_songs)









