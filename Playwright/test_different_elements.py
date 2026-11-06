from dataclasses import dataclass

from playwright.sync_api import Page, expect, Playwright, Locator
import time


@dataclass(frozen=True)
class Product:
    name: str
    price: int
    discount_price: int

def get_products(product_rows: Locator) -> dict[str, Product]:
    products = {}

    for row in product_rows.all():
        cell = [c.strip() for c in row.locator("td").all_text_contents()]
        products[cell[0]] = Product(cell[0], int(cell[1]), int(cell[2]))
        #print(cell)

    return products

def test_handle_tabled(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Indus solution
    for index in range(page.locator("th[role='columnheader']").count()):
        if page.locator("th[role='columnheader']").nth(index).filter(has_text='Price').count() > 0:
            price_column = index
            print(f"Price column value is:'{price_column}'")
            break

    rice_row = page.locator("tr").filter(has_text='Rice')
    rice_price = rice_row.locator("td").nth(price_column)

    print(rice_price.text_content())  # 37
    expect(rice_price).to_have_text("37")

    # Rework by me
    product_rows = page.locator("tbody tr")
    products = get_products(product_rows)

    print(products)
    rice = products.get('Rice')
    print(f"Product:{rice.name}, price:{rice.price}")


def test_handle_alert(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # Handle alert box
    page.on('dialog', lambda dialog: dialog.accept())

    page.locator('input#confirmbtn').click()


    # Frame handling
    frame = page.frame_locator('iframe#courses-iframe')
    frame.get_by_role('link', name='All Access plan').click()
    expect(frame.locator('body')).to_contain_text(' Happy Subscibers!')


def test_displayed_element(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    hide_element = page.get_by_placeholder('Hide/Show Example')
    expect(hide_element).to_be_visible()

    # push the hide button
    page.locator('input#hide-textbox').click()
    expect(hide_element).to_be_hidden()
