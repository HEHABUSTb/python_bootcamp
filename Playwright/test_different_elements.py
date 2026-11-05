from playwright.sync_api import Page, expect, Playwright


def test_displayed_element(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    hide_element = page.get_by_placeholder('Hide/Show Example')
    expect(hide_element).to_be_visible()

    # push the hide button
    page.locator('input#hide-textbox').click()
    expect(hide_element).to_be_hidden()
