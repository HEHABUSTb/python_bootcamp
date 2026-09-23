from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = "nsanvold@gmail.com"
Y_PASSWORD = "lY4xlGtlwGLXGz4B"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.down = int
        self.up = int
        self.result_id: str = ""


    def get_internet_speed(self):
        self.driver.get(r"https://www.speedtest.net/")

        # Reject cookies
        self.wait.until(ec.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()

        # Press Go button
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='start speed test - connection type multi']"))).click()

        # Wait until result url appear
        wait = WebDriverWait(self.driver, 150)
        self.result_id = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "p.MuiTypography-root a[title='Opens in new tab']"))).text

        # Find and validate speed results
        speed_results = self.driver.find_elements(By.CSS_SELECTOR, "div.MuiBox-root h3.MuiBox-root")
        if not speed_results or len(speed_results) != 2:
            print(f"Expected valid speed_results, got {speed_results}")
        self.up = speed_results[1].text
        self.down = speed_results[0].text

        # Print result_id and speeds
        print(f"Result_id:'{self.result_id}'")
        print(f"Download speed:'{self.down}'")
        print(f"Upload speed:'{self.up}'")


    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)

        # enter creds
        email_field = self.wait.until(ec.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(Y_EMAIL)

        password_field = self.wait.until(ec.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(Y_PASSWORD)

        # Push login button
        submit_button = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        submit_button.click()

        # Find post field
        post_field = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Post text']")))
        tweet = f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        post_field.send_keys(tweet)

        # Push the tweet button
        tweet_button = self.wait.until(ec.element_to_be_clickable((By.ID, "post-btn")))
        tweet_button.click()

    def validate_web_element(self, element: WebElement):
        pass

def main() -> None:
    bot = InternetSpeedTwitterBot()
    try:
        bot.get_internet_speed()
        bot.tweet_at_provider()

        input("Press Enter to close the browser...")

    finally:
        bot.driver.quit()



if __name__ == "__main__":
    main()