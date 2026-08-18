from dataclasses import dataclass, field
from email.message import EmailMessage
from pprint import pprint
import smtplib
from env import SMTP_ADDRESS, EMAIL_ADDRESS, EMAIL_PASSWORD

from bs4 import BeautifulSoup, Tag
import requests

if not all([SMTP_ADDRESS, EMAIL_ADDRESS, EMAIL_PASSWORD]):
    print(f"Aborting setup env.py first")

@dataclass
class AmazonProduct:
    expected_price: float
    url: str = r"https://appbrewery.github.io/instant_pot/"

    def is_new_price_better(self, new_price: float) -> bool:
         return new_price < self.expected_price

@dataclass
class EmailAlert:
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    sender_email: str = field(default_factory=lambda: SMTP_ADDRESS)
    sender_password: str = field(default_factory=lambda: EMAIL_PASSWORD)
    recipient_email: str = field(default_factory=lambda: EMAIL_ADDRESS)

    def send_email_alert(self, product: AmazonProduct, current_price: float) -> None:
        message = EmailMessage()
        message["Subject"] = "Price drop alert!"
        message["From"] = self.sender_email
        message["To"] = self.recipient_email

        message.set_content(
            f"Price dropped to ${current_price:.2f} "
            f"(your target was ${product.expected_price:.2f}).\n{product.url}"
        )

        with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(message)


@dataclass
class Tracker:
    url: str

    def main(self) -> float:
        response = self._get(self.url)
        return tracker.get_price_from_response(response)

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
            print(f"{price_float:.2f}")
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
    product = AmazonProduct(expected_price=100.0)
    tracker = Tracker(url=AmazonProduct.url)
    new_price = tracker.main()

    if new_price < product.expected_price:
        EmailAlert().send_email_alert(product, new_price)
