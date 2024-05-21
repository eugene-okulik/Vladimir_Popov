from playwright.sync_api import Page, expect


def test_part_one(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role(role="link", name="Form Authentication").click()
    username_field = page.get_by_role(role="textbox", name="username")
    username_field.fill("tomsmith")
    password_field = page.get_by_role(role="textbox", name="password")
    password_field.fill("SuperSecretPassword!")
    page.get_by_role(role="button", name=" Login").click()
