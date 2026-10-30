import time

from playwright.sync_api import Page

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
