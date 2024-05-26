from playwright.sync_api import Page, expect


def test_accept_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    button = page.get_by_role(role="link", name="Click")
    button.click()
    result_text = page.locator("#result-text")
    expect(result_text).to_have_text("Ok")
