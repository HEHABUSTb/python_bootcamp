from playwright.sync_api import Playwright

from Playwright.conftest import User

ORDER_PAYLOAD = {"orders":[{"country": "Poland", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}


class APIHelper:
    def __init__(self, playwright: Playwright, user: User):
        self.base_url = "https://rahulshettyacademy.com"
        self.playwright = playwright
        self.user = user
        self.token = self.get_token()

    def get_token(self):
        api_request_context = self.playwright.request.new_context(base_url=self.base_url)
        response = api_request_context.post('/api/ecom/auth/login',
                                 data={"userEmail": self.user.email, "userPassword": self.user.password},)
        assert response.ok, f"Login failed for {self.user.email}: {response.status} {response.text()}"

        # print(response.json())
        token = response.json().get("token")

        if not token:
            raise Exception('No token found')

        return token

    def create_order(self):
        api_request_context = self.playwright.request.new_context(base_url=self.base_url)
        response = api_request_context.post('/api/ecom/order/create-order',
                                 data=ORDER_PAYLOAD,
                                 headers={'Authorization': self.token,
                                          'Content-Type': 'application/json'})

        assert response.ok
        print(response.json())
        response_body = response.json()

        order_id = response_body.get("orders")[0]

        if not order_id:
            raise Exception('No order id found')

        return order_id