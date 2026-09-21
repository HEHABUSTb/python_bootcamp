import os
from dataclasses import dataclass
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ACCOUNT_EMAIL = "super_test@test.com"
ACCOUNT_PASSWORD = "test_password1"
GYM_URL = "https://appbrewery.github.io/gym/"

# locators
LOGIN_BUTTON = (By.ID, "login-button")

EMAIL_INPUT = (By.ID, "email-input")
PASSWORD_INPUT = (By.ID, "password-input")
SUBMIT_BUTTON = (By.ID, "submit-button")

SCHEDULE_PAGE = (By.ID, "schedule-page")

@dataclass
class Statistics:
    classes_booked: int = 0
    classes_waitlisted: int = 0
    already_booked_waitlisted: int = 0

    @property
    def total_classes(self) -> int:
        return self.classes_booked + self.classes_waitlisted



# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(r"https://appbrewery.github.io/gym/")

# ----------------  Step 2 - Automated Login ----------------

wait = WebDriverWait(driver, 2)

#click on login button
login_btn = wait.until(ec.element_to_be_clickable(LOGIN_BUTTON))
login_btn.click()

# Fill in login form
email_input = wait.until(ec.presence_of_element_located(EMAIL_INPUT))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(*PASSWORD_INPUT)
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

# Click Login
submit_btn = driver.find_element(*SUBMIT_BUTTON)
submit_btn.click()

# Wait until schedule page appear
wait.until(ec.presence_of_element_located(SCHEDULE_PAGE))

# ----------------  Step 2 - Book the upcoming Tuesday class ----------------

EVENT_CLASSES = (By.CLASS_NAME, "ClassCard_card__KpCx5")
events = driver.find_elements(*EVENT_CLASSES)
statistics = Statistics()

if not events:
    print("No events found.")

desired_date = datetime.today().date()

for event in events:
    event_date_list = event.get_attribute("data-class-id").split("-")
    event_name = event_date_list[0]

    date_str = "-".join(event_date_list[1:4])
    event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    event_hour = event.text

    if (event_date == desired_date or event_date ==  desired_date + timedelta(days=2)) and "6:00 PM" in event_hour:
        print(f"Event found:{event_name} on {date_str}")
        book_button =  event.find_element(By.CSS_SELECTOR, "div button")
        book_button_text = book_button.text

        match book_button_text:
            case "Book":
                statistics.already_booked_waitlisted += 1
                print(f"✓ Already booked:{event_name} on {date_str} at {event_hour}")
            case "Waitlisted":
                statistics.already_booked_waitlisted += 1
                print(f"✓ Already on waitlist:{event_name} on {date_str} at {event_hour}")
            case "Join Waitlist":
                book_button.click()
                statistics.classes_waitlisted += 1
                print(f"✓ Join waitlist:{event_name} on {date_str} at {event_hour}")
            case _:
                book_button.click()
                statistics.classes_booked += 1
                print(f"✓ Booked:{event_name} on {date_str} at {event_hour}")


print("--- BOOKING SUMMARY ---")
print(f"Classes booked: {statistics.classes_booked}")
print(f"Classes waitlisted: {statistics.classes_waitlisted}")
print(f"Already booked/waitlisted:{statistics.already_booked_waitlisted}")
print(f"Total Tuesday 6pm classes processed:{statistics.total_classes}")

# ----------------  Step 3 - Verify Class bookings ----------------

MY_BOOKINGS_LINK = (By.ID, "my-bookings-link")
driver.find_element(*MY_BOOKINGS_LINK).click() # go to my bookings
BOOKING_PAGE = (By.ID, "my-bookings-page")
wait.until(ec.presence_of_element_located(BOOKING_PAGE))

print(f"--- VERIFYING ON MY BOOKINGS PAGE ---")

# Find ALL booking cards (both confirmed and waitlist)
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

verified_cards = 0
for card in all_cards:
    class_name = card.find_element(By.CSS_SELECTOR, "h3").text
    class_time = card.find_element(By.CSS_SELECTOR, "div p").text
    print(f"✓ Verified: {class_name} on {class_time}")
    if ("Sut" or "Tue" in class_name) and "6:00 PM" in class_time:
        verified_cards += 1

print(f"--- VERIFICATION RESULT ---")
print(f"Expected: {statistics.already_booked_waitlisted} bookings")
print(f"Found: {verified_cards} bookings")

if statistics.total_classes != verified_cards:
    print(f"❌ MISMATCH: {statistics.total_classes} != {verified_cards} bookings")
else:
    print("✅ SUCCESS: All bookings verified!")