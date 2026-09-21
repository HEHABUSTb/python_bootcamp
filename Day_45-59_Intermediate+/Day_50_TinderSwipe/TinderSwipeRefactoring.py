from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
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

def push_button(selector):
    button = wait.until(ec.element_to_be_clickable(selector))
    button.click()

# Create browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get(TINDER_URL)

# Step 1: pass through login
push_button(LOGIN_BUTTON)
push_button(LOGIN_BUTTON_FACEBARK)

# switch to the login window
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
assert driver.title == "Facebark"

driver.find_element(*INPUT_EMAIL).send_keys("test@email.com")
driver.find_element(*INPUT_PASSWORD).send_keys("1234")
push_button(SUBMIT_BUTTON)

driver.switch_to.window(driver.window_handles[0])
assert driver.title == "Tindog"

# Step 2: Dismiss all requests
push_button(ALLOW_BUTTON)
push_button(NOT_ACCEPTED_BUTTON)

push_button(ALLOW_BUTTON)

wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "main.tindog-swipe-container")))

# Step 3: Hit like 10 times

for i in range(10):
    try:
        like_button = wait.until(ec.element_to_be_clickable(LIKE_BUTTON))
        like_button.click()
    except ElementClickInterceptedException:
        driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()

input(r"Should i close browser?")
driver.quit()
