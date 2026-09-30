import time
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup, Tag
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

ZILLOW_URL = r"https://appbrewery.github.io/Zillow-Clone/"

@dataclass
class RentOffer:
    address: str
    price: str
    link: str

# Get data from zillow html page
response = requests.get(ZILLOW_URL)
print(f"Response status code:'{response.status_code}'")
# pprint(response.json())
response.raise_for_status()
content = response.content

# scrap data by bs
soup = BeautifulSoup(content, "html.parser")

card_datas = soup.select("div[class='StyledPropertyCardDataWrapper']")

result = []
for card in card_datas:
    link = card.select_one(r"a[data-test='property-card-link']").get("href")
    address = card.select_one(r"address").text.strip()
    price = card.select_one(r"span[data-test='property-card-price']").text.replace(r"+/mo", "")
    # to do: validate data
    result.append(RentOffer(address=address, price=price, link=link))

print(result)


# Use Selenium to fill in the form
options = Options()
options.add_argument("--lang=en-US")
options.add_experimental_option(
    "prefs",
    {"intl.accept_languages": "en,en_US"}
)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 10)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdVhz6wWXCEQPG7nnRayHBSX1SJxJEzCtgwukjhoLbytKTGbQ/viewform?usp=publish-editor")



for offer in result:
    input_fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

    input_fields[0].click()
    input_fields[0].send_keys(offer.address)

    input_fields[1].click()
    input_fields[1].send_keys(offer.price)

    input_fields[2].click()
    input_fields[2].send_keys(offer.link)

    driver.find_element(By.CSS_SELECTOR, "div form div div  div[role='button']").click()

    send_again_link = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div a")))
    send_again_link.click()

