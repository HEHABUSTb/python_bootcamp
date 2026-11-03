import time
from playwright.sync_api import Page, expect, Playwright


def fill_box_field(page: Page, label: str, value: str):
    box = page.get_by_label(label)
    box.fill(value)

def test_playwright(playwright):
    browser = playwright.chromium.launch(headless=False)
    browser_context = browser.new_context() # Create separate window without cookies

    page = browser_context.new_page()
    page.goto("https://www.google.com")


# chromium headless mode with 1 single context
def test_playwright_shortcut(page: Page):
    page.goto("https://www.google.com")


def test_core_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    fill_box_field(page, 'Username:', 'username')
    fill_box_field(page, 'Password:', 'password')

    page.get_by_role("combobox").select_option(value="teach")
    page.locator("input#terms").check()
    page.locator("input#signInBtn").click()

    time.sleep(1)

def test_wrong_password(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    fill_box_field(page, 'Username:', 'rahulshettyacademy')
    fill_box_field(page, 'Password:', 'wrong_password')

    page.get_by_role("combobox").select_option(value="teach")
    page.locator("input#terms").check()
    page.locator("input#signInBtn").click()

    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefox_browser(playwright: Playwright):
    firefox = playwright.firefox.launch(headless=False)
    firefox_page = firefox.new_page()

    firefox_page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    time.sleep(1)
