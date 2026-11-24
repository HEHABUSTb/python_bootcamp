import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from Playwright.conftest import User
from Playwright.helpers.api_base import APIHelper
from pathlib import Path

from Playwright.page_objects.login import LoginPage

DATA_DIR = Path(__file__).parent / "data"

# Json file -> util -> User DataClass
with open(DATA_DIR / 'credentials.json') as json_file:
    test_data = json.load(json_file)
    # print(test_data)
    user_creds = test_data.get('users')


@pytest.mark.parametrize('user', user_creds, indirect=True)
def test_e2e_web_api(playwright: Playwright, user: User, browser_instance):
    print('Test E2E Web API')
    print(user.email, user.password)

    # Create order by API -> get order_id for validation
    api_helper = APIHelper(playwright=playwright, user=user)
    order_id = api_helper.create_order()

    # Login -> enter creds
    login_page = LoginPage(page=browser_instance, user=user)
    login_page.navigate()
    dashboard_page = login_page.login()

    # Go to History page and validate order id from API call
    orders_history_page = dashboard_page.click_orders_link()
    orders_history_page.select_order(order_id=order_id)

    time.sleep(3)
