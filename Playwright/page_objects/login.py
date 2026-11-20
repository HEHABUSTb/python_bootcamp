from playwright.sync_api import Page
from Playwright.conftest import User
from Playwright.page_objects.dashboard import Dashboard


class LoginPage:

    def __init__(self, page: Page, user: User):
        self.login_url = "https://rahulshettyacademy.com/client"
        self.page = page
        self.user = user


    def navigate(self):
        self.page.goto(self.login_url)

    def login(self):
        email = self.page.locator('input#userEmail')
        email.fill(self.user.email)

        password = self.page.locator('input#userPassword')
        password.fill(self.user.password)

        self.page.locator('input#login').click()

        return Dashboard(page=self.page)