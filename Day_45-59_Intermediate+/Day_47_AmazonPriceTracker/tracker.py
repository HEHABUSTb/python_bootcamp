from dataclasses import dataclass
from pprint import pprint

from bs4 import BeautifulSoup, Tag
import requests


@dataclass
class AmazonProduct:
    expected_price: float
    url: str = r"https://appbrewery.github.io/instant_pot/"

    def is_new_price_better(self, new_price: float) -> bool:
         return new_price < self.expected_price


@dataclass
class Tracker:
    url: str

    def main(self) -> None:
        response = self._get(self.url)
        print(tracker.get_price_from_response(response))



    @staticmethod
    def _get(url: str) -> str:
        response = requests.get(f"{url}")
        print(f"Response status code:'{response.status_code}'")
        # pprint(response.json())
        response.raise_for_status()

        return response.content

    @staticmethod
    def get_price_from_response(content: str) -> float | None:
        soup = BeautifulSoup(content, "html.parser")
        price_tag = soup.select(r"span.aok-offscreen")
        price_float = Tracker.is_price_valid(price_tag)

        if price_float:
            return price_float
        else:
            print(f"No price found:'{content}'")
            return None

    @staticmethod
    def is_price_valid(price: list[Tag]) -> bool | float:
        if not price[0]:
            return False
        try:
            return float(price[0].text.split("$")[1])
        except (ValueError, TypeError):
            return False


if __name__ == "__main__":
    product = AmazonProduct(expected_price=22.0)
    tracker = Tracker(url=AmazonProduct.url)
    tracker.main()

