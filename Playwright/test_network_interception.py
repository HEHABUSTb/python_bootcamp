import time

from playwright.sync_api import Page, expect, Playwright, Locator, Response, Request

FAKE_PAYLOAD_RESPONSE= {"data": [], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json=FAKE_PAYLOAD_RESPONSE
    )



def test_network(page: Page):
    page.goto("https://rahulshettyacademy.com/client")

    # Intercept network and put fake payload
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)

    # Login -> go to my orders
    email = page.locator('input#userEmail')
    email.fill('msanvold@gmail.com')
    password = page.locator('input#userPassword')
    password.fill('Rewqasdf1')

    page.locator('input#login').click()
    page.locator('button[routerlink="/dashboard/myorders"]').click()

    # verify text
    order_text = page.locator("div.mt-4").text_content()
    time.sleep(2)
    print(order_text)