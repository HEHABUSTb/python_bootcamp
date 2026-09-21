import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

TINDER_URL =r"https://app.100daysofpython.dev/services/tindog/u/ralzJlEZV8IVOBmxLUR9dqq4YZK07ZT-"

LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-tindog-login")
LOGIN_BUTTON_FACEBARK = (By.CSS_SELECTOR, "button.btn-facebark")

INPUT_EMAIL = (By.ID, "email")
INPUT_PASSWORD = (By.ID, "pass")
SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

ALLOW_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
NOT_ACCEPTED_BUTTON = (By.CSS_SELECTOR, "button.btn-secondary")

NOPE_BUTTON = (By.CSS_SELECTOR, "button.btn-nope")
LIKE_BUTTON = (By.CSS_SELECTOR, "button.btn-like")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # Don't close browser for debug


driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 5)
driver.get(TINDER_URL)

# Step 1: pass through login
login_button = wait.until(ec.element_to_be_clickable(LOGIN_BUTTON))
login_button.click()

facebark_login_button = wait.until(ec.element_to_be_clickable(LOGIN_BUTTON_FACEBARK))
facebark_login_button.click()

# switch to the login window
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_input = driver.find_element(*INPUT_EMAIL)
email_input.send_keys("test@email.com")

password_input = driver.find_element(*INPUT_PASSWORD)
password_input.send_keys("1234")

submit_button = driver.find_element(*SUBMIT_BUTTON)
submit_button.click()

driver.switch_to.window(driver.window_handles[0])
print(driver.title)

# Step 2: Dismiss all requests
allow_button = wait.until(ec.element_to_be_clickable(ALLOW_BUTTON))
allow_button.click()

not_accepted_button = wait.until(ec.element_to_be_clickable(NOT_ACCEPTED_BUTTON))
not_accepted_button.click()

allow_button = wait.until(ec.element_to_be_clickable(ALLOW_BUTTON))
allow_button.click()

# TO DO: check that appear <main class="tindog-swipe-container">

# Step 3: Hit like 10 times

for i in range(10):
    try:
        like_button = wait.until(ec.element_to_be_clickable(LIKE_BUTTON))
        like_button.click()
    except ElementClickInterceptedException:
        driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
