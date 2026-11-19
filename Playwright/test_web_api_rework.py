import json

import pytest
from playwright.sync_api import Playwright, expect

from Playwright.conftest import User
from Playwright.helpers.api_base import APIHelper
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# Json file -> util -> User DataClass
with open(DATA_DIR / 'credentials.json') as json_file:
    test_data = json.load(json_file)
    # print(test_data)
    user_creds = test_data.get('users')


@pytest.mark.parametrize('user', user_creds, indirect=True)
def test_e2e_web_api(playwright: Playwright, user: User):
    print('Test E2E Web API')
    print(user.email, user.password)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create order by API -> get order_id for validation
    api_helper = APIHelper(playwright=playwright, user=user)
    oder_id = api_helper.create_order()

    # Login -> enter creds
    page.goto("https://rahulshettyacademy.com/client")

    email = page.locator('input#userEmail')
    email.fill(user.email)

    password = page.locator('input#userPassword')
    password.fill(user.password)

    page.locator('input#login').click()

    # Go to History page and validate order id from API call
    page.locator('button[routerlink="/dashboard/myorders"]').click()

    order_rows = page.locator("tr")
    expect(order_rows.first).to_be_visible()
    expect(order_rows.filter(has_text=oder_id)).to_be_visible()

    context.close()