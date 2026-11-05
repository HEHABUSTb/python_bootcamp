from playwright.sync_api import Page, expect, Playwright
import time

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
