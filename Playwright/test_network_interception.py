import time

from playwright.sync_api import Page, Route

FAKE_PAYLOAD_RESPONSE= {"data": [], "message": "No Orders"}

def intercept_response(route: Route) -> None:
    route.fulfill(
        json=FAKE_PAYLOAD_RESPONSE
    )

def intercept_request(route: Route) -> None:
    route.continue_(url='https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6af442cd92a4341c4c114a8c')

def test_mocking_request(page: Page):
    page.goto("https://rahulshettyacademy.com/client")

    # Intercept network and put fake payload
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)

    # Login -> go to my orders
    page.locator('input#userEmail').fill('')
    page.locator('input#userPassword').fill('')

    page.locator('input#login').click()
    page.locator('button[routerlink="/dashboard/myorders"]').click()
    page.get_by_role('button', name='View').first.click()

    # check that no autorize message appear
    message = page.locator(".blink_me").text_content()
    print(message)

    time.sleep(2)


def test_network_intercepting(page: Page):
    page.goto("https://rahulshettyacademy.com/client")

    # Intercept network and put fake payload
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)

    # Login -> go to my orders
    email = page.locator('input#userEmail')
    email.fill('')
    password = page.locator('input#userPassword')
    password.fill('')

    page.locator('input#login').click()
    page.locator('button[routerlink="/dashboard/myorders"]').click()

    # verify text
    order_text = page.locator("div.mt-4").text_content()
    time.sleep(2)
    print(order_text)