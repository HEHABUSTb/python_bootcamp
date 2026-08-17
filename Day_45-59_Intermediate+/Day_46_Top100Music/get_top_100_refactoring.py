"""Scrape the "Bakeboard" Hot 100 chart for a given date and sync the songs
into a YouTube Music playlist.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

CHART_URL_TEMPLATE = "https://appbrewery.github.io/bakeboard-hot-100/{date}/"
DEFAULT_DATE = "2026-04-18"
DATE_FORMAT = "%Y-%m-%d"
YT_AUTH_FILE = "browser.json"
MAX_DATE_ATTEMPTS = 3


@dataclass(frozen=True)
class Song:
    """A single chart entry."""
    rank: str
    title: str
    artist: str


def prompt_for_date(max_attempts: int = MAX_DATE_ATTEMPTS) -> str | None:
    """Ask the user for a date until it's valid or the attempts run out."""
    attempts_left = max_attempts

    while attempts_left > 0:
        date_str = input(
            "Which year do you want to travel to? Type the date as YYYY-MM-DD: "
        )
        try:
            datetime.strptime(date_str, DATE_FORMAT)
            return date_str
        except ValueError:
            attempts_left -= 1
            print(f"Invalid date format or non-existent date. Attempts left: {attempts_left}")

    print("No valid date provided. Aborting.")
    return None


def fetch_chart_html(date_str: str) -> str:
    """Download the chart page for the given date."""
    url = CHART_URL_TEMPLATE.format(date=date_str)
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")
    response.raise_for_status()
    return response.text


def parse_top_100(html: str) -> list[Song]:
    """Parse the chart HTML into a list of Song entries."""
    soup = BeautifulSoup(html, "html.parser")
    songs = []

    for entry in soup.select("div.chart-entry"):
        rank = entry.select_one("span.chart-entry__rank-number").text.strip()

        info_lines = [
            line for line in entry.select_one("div.chart-entry__info").text.split("\n") if line
        ]
        title, artist = info_lines[0], info_lines[1]

        songs.append(Song(rank=rank, title=title, artist=artist))

    return songs


def get_top_100_songs(date_str: str = DEFAULT_DATE) -> list[Song]:
    """Fetch and parse the top 100 songs chart for the given date."""
    html = fetch_chart_html(date_str)
    return parse_top_100(html)


def get_or_create_playlist(yt: YTMusic, name: str) -> str:
    """Return the id of an existing playlist with this name, or create one."""
    playlists = yt.get_library_playlists()
    print(f"Found {len(playlists)} playlists in your library.")

    for playlist in playlists:
        if playlist["title"] == name:
            return playlist["playlistId"]

    return yt.create_playlist(name, name)


def add_songs_to_playlist(yt: YTMusic, playlist_id: str, songs: list[Song]) -> None:
    """Search for each song on YouTube Music and add the first match to the playlist."""
    for song in songs:
        search_results = yt.search(song.title)

        if not search_results or not search_results[0].get("videoId"):
            print(f"Skipped: '{song.title}'")
            continue

        video_id = search_results[0]["videoId"]
        yt.add_playlist_items(playlist_id, [video_id])
        print(f"Added song: '{song.title}'")


def main() -> None:
    date_str = DEFAULT_DATE  # swap for `prompt_for_date()` to ask the user interactively
    if date_str is None:
        return

    songs = get_top_100_songs(date_str)
    print(songs)

    yt = YTMusic(YT_AUTH_FILE)
    playlist_name = f"Back in {date_str}"
    playlist_id = get_or_create_playlist(yt, playlist_name)

    add_songs_to_playlist(yt, playlist_id, songs)


if __name__ == "__main__":
    main()
