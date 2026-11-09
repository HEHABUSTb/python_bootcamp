from playwright.sync_api import Playwright, expect
from  helpers.api_base import APIHelper

from Playwright.helpers.api_base import APIHelper


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create order by API -> get order_id for validation
    api_helper = APIHelper(playwright=playwright)
    oder_id = api_helper.create_order()
    oder_id = 'dsadasdas'

    # Login -> enter creds
    page.goto("https://rahulshettyacademy.com/client")

    email = page.locator('input#userEmail')
    email.fill('')

    password = page.locator('input#userPassword')
    password.fill('')

    page.locator('input#login').click()

    # Go to History page and validate order id from API call
    page.locator('button[routerlink="/dashboard/myorders"]').click()

    order_rows = page.locator("tr")
    expect(order_rows.first).to_be_visible()
    expect(order_rows.filter(has_text=oder_id)).to_be_visible()

    context.close()