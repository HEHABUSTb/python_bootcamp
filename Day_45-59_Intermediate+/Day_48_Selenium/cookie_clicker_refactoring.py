from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

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

# Base url
BASE_URL = r"https://ozh.github.io/cookieclicker/"


class CookieClicker:

    def __init__(self, ):
        self.driver = webdriver.Chrome()
        self.timelimit = 1

    def click_cookie(self):
        try:
            self.driver.find_element(*COOKIE_BUTTON).click()
        except StaleElementReferenceException:
            print("Cookie is stale, waiting...")

        print(f"Cookies per second:'{self.driver.find_element(*COOKIE_NUMBER).text}'")

    def find_best_product(self) -> WebElement | None:
        products = self.driver.find_elements(*UNLOCKED_PRODUCTS)
        if not products:
            print("No products found")
            return None

        best_price = 0
        best_index = 0

        for i in range(len(products)):
            price = products[i].find_element(*PRICE)
            if best_price < int(price.text):
                best_price = int(price.text)
                best_index = i

        return products[best_index]

    def open_browser(self):
        self.driver.get(BASE_URL)

    def play_game(self):
        # Start actually play
        timelimit = 1  # mins
        end_time = datetime.now() + timedelta(minutes=timelimit)
        next_product_check = datetime.now()

        while datetime.now() < end_time:

            # check for upgrades every 5 sec
            if datetime.now() >= next_product_check:
                best_product = self.find_best_product()
                if best_product:
                    best_product.click()
                next_product_check = datetime.now() + timedelta(seconds=5)

            # just click cookie
            self.click_cookie()

    def main(self):
        self.open_browser()
        self.select_language()
        self.play_game()

    def select_language(self):
        language_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(LANGUAGE_BUTTON))
        language_button.click()



if __name__ == "__main__":
    cookie_clicker = CookieClicker()
    cookie_clicker.main()
