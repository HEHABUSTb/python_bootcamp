from playwright.sync_api import Page
from Playwright.page_objects.orders_history import OrdersHistory


class Dashboard:

    def __init__(self, page: Page):
        self.page = page


    def click_orders_link(self):
        self.page.locator('button[routerlink="/dashboard/myorders"]').click()

        return OrdersHistory(page=self.page)

