from pprint import pprint

import requests
from bs4 import BeautifulSoup

response = requests.get(r"https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.content, 'html.parser')

all_titles = soup.find_all("h3", class_="title")

best_movies = [title.text.split(" ", 1) for title in all_titles]
best_movies.reverse()

pprint(best_movies)
