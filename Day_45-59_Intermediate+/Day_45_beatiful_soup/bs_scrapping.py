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
    score = int(score_tag.text.split()[0])

    articles.append(SimpleNamespace(title=link.getText(), link=link['href'], score=score))

articles.sort(key=lambda article: article.score, reverse=True)
print(articles)


pprint(articles)

