from playwright.sync_api import Page, expect
import re


def test_click_red_button(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button = page.locator("#colorChange")
    expect(button).to_have_class(re.compile("text-danger"))
    button.click()
