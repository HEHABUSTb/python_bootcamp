from playwright.sync_api import Page, expect
from Playwright.conftest import User


class OrdersHistory:

    def __init__(self, page: Page):
        self.page = page


    def select_order(self, order_id: str):
        order_rows = self.page.locator("tr")
        expect(order_rows.first).to_be_visible()
        expect(order_rows.filter(has_text=order_id)).to_be_visible()
