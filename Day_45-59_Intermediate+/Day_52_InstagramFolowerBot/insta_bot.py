import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

SIMILAR_ACCOUNT = "rordongamsay"   # the account whose followers you'll follow
USERNAME = "nsanvold@gmail.com"       # your Share-a-Naan (or Instagram) username (your email)
PASSWORD = "7_aaBZ-VvDf4t9bD"
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get(LOGIN_URL)

        email_field = self.wait.until(ec.presence_of_element_located((By.ID, "username")))
        email_field.send_keys(USERNAME)

        password_field = self.wait.until(ec.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(PASSWORD)

        # Push login button
        submit_button = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        # close pop-up message
        save_info = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_info:
            save_info[0].click()

        notifications = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if notifications:
            notifications[0].click()

    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}/followers")

        scroll = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".followers-scroll")))

        for _ in range(10):
            # "scroll this element to the bottom" → loads the next batch of followers
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(1)

    def follow(self):
        followers = self.driver.find_elements(By.CSS_SELECTOR, '.followers-scroll button')

        for follower in followers:
            try:
                follower.click()
            except ElementClickInterceptedException:
                self.driver.find_element(By.CSS_SELECTOR, 'button.naan-unfollow-cancel').click()



def main() -> None:
    insta = InstaFollower()

    try:
        insta.login()
        insta.find_followers()
        insta.follow()



        input("Press Enter to close the browser...")

    finally:
        insta.driver.quit()

if __name__ == "__main__":
    main()
