import time
from playwright.sync_api import Page, expect, Playwright

def login(page: Page, username='rahulshettyacademy', password='Learning@830$3mK2'):
    page.get_by_label('Username:').fill(username)
    page.get_by_label('Password:').fill(password)

    page.get_by_role("combobox").select_option(value="teach")
    page.locator("input#terms").check()
    page.locator("input#signInBtn").click()

def test_dynamic_selection(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    login(page)

    # Get iphone X, Nokia Edge -> verify 2 items located ic cart
    iphone_card = page.locator("app-card").filter(has_text='iphone X')
    iphone_card.get_by_role('button').click()

    nokia_card = page.locator("app-card").filter(has_text='Nokia Edge')
    nokia_card.get_by_role('button').click()

    # Go to checkout and validate products
    page.get_by_text('Checkout').click()

    expect(page.locator(".media-body")).to_have_count(count=2)