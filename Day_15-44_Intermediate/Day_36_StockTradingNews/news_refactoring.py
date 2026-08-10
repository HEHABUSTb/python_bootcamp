"""
Проверяет, изменилась ли цена акции более чем на PRICE_CHANGE_THRESHOLD %
за последний торговый день, и если да — печатает свежие новости о компании.
"""

import logging
from dataclasses import dataclass

import requests
from env import STOCK_API, NEWS_API

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"
PRICE_CHANGE_THRESHOLD = 2.0  # в процентах
NEWS_ARTICLES_LIMIT = 3

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


@dataclass
class PriceMovement:
    latest_date: str
    latest_close: float
    prev_date: str
    prev_open: float

    @property
    def percent_change(self) -> float:
        return abs(self.prev_open - self.latest_close) / self.prev_open * 100

    @property
    def is_significant(self) -> bool:
        return self.percent_change > PRICE_CHANGE_THRESHOLD


def get_price_movement(symbol: str) -> PriceMovement:
    """Запрашивает дневные цены и возвращает данные за последние 2 торговых дня."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "apikey": STOCK_API,
        "symbol": symbol,
        "outputsize": "compact",
    }

    response = requests.get(STOCK_ENDPOINT, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    time_series = data.get("Time Series (Daily)")
    if not time_series:
        # Alpha Vantage при ошибке/лимите возвращает 200 OK с полем "Note" или "Error Message"
        raise RuntimeError(f"Unexpected API response: {data}")

    dates = sorted(time_series.keys(), reverse=True)
    latest_date, prev_date = dates[0], dates[1]

    latest_day = time_series[latest_date]
    prev_day = time_series[prev_date]

    logger.info("Latest (%s): close=%s", latest_date, latest_day["4. close"])
    logger.info("Previous (%s): open=%s", prev_date, prev_day["1. open"])

    return PriceMovement(
        latest_date=latest_date,
        latest_close=float(latest_day["4. close"]),
        prev_date=prev_date,
        prev_open=float(prev_day["1. open"]),
    )


def get_company_news(company_name: str, from_date: str, limit: int = NEWS_ARTICLES_LIMIT) -> list[dict]:
    """Возвращает список новостных статей о компании начиная с from_date."""
    params = {
        "q": company_name,
        "from": from_date,
        "sortBy": "popularity",
        "apiKey": NEWS_API,
    }

    response = requests.get(NEWS_ENDPOINT, params=params, timeout=10)
    response.raise_for_status()
    articles = response.json().get("articles", [])

    return articles[:limit]


def print_articles(articles: list[dict]) -> None:
    for article in articles:
        print(article["title"])
        print(article["description"])
        print(article["url"])
        print("/" * 50)


def main() -> None:
    movement = get_price_movement(STOCK_SYMBOL)

    logger.info("Price change: %.2f%%", movement.percent_change)

    if not movement.is_significant:
        print("No news")
        return

    print("Get News")
    articles = get_company_news(COMPANY_NAME, from_date=movement.prev_date)
    print_articles(articles)


if __name__ == "__main__":
    main()