import random
from codecs import ignore_errors
from pprint import pprint

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from types import SimpleNamespace
from datetime import datetime, timedelta

from selenium.webdriver.common.devtools.v85.network import Cookie
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selectors
LANGUAGE_BUTTON = (By.ID, "langSelect-EN")
COOKIE_BUTTON = (By.ID, "bigCookie")
COOKIE_NUMBER = (By.ID, "cookies")

# Upgrades selectors
UNLOCKED_PRODUCTS = (By.CSS_SELECTOR, ".product.unlocked.enabled")
PRICE = (By.CSS_SELECTOR, ".price")
UNLOCKED_UPGRADES = (By.CSS_SELECTOR, ".crate.upgrade.enabled")

def find_best_product() -> WebElement | None:
    products = driver.find_elements(*UNLOCKED_PRODUCTS)
    if not products:
        return None

    best_price = 0
    best_index = 0

    for i in range(len(products)):
        price = products[i].find_element(*PRICE)
        if best_price < int(price.text):
            best_price = int(price.text)
            best_index = i

    return products[best_index]


driver = webdriver.Chrome()
driver.get(r"https://ozh.github.io/cookieclicker/")

# select language
language_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(LANGUAGE_BUTTON))
language_button.click()

# Start actually play
timelimit = 1 # mins
end_time = datetime.now() + timedelta(minutes=timelimit)
next_product_check = datetime.now()

while datetime.now() < end_time:

    # check for upgrades every 5 sec
    if datetime.now() >= next_product_check:
        best_product = find_best_product()
        if best_product:
            best_product.click()
        next_product_check = datetime.now() + timedelta(seconds=5)

    # just click cookie
    driver.find_element(*COOKIE_BUTTON).click()


print(f"Cookies per second:'{driver.find_element(*COOKIE_NUMBER).text}'")