from pprint import pprint

import requests
from bs4 import BeautifulSoup
from types import SimpleNamespace

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.content, 'html.parser')

titlelines = soup.select("span.titleline")

articles = []

for tl in titlelines:
    link = tl.find('a')

    subtext = tl.find_parent("tr").find_next_sibling("tr")
    score_tag = subtext.select_one("span.score")

    articles.append(SimpleNamespace(title=link.getText(), link=link['href'], score=score_tag.text))


pprint(articles)

