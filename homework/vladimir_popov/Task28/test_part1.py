from playwright.sync_api import Route, Expect, Page
import json
import re


def test_iphone(page: Page):


    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 15 про"
        body = json.dumps(body)
        route.fulfill(response=response, body=body)


    page.route(re.compile("digital-mat"), handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    iphone_button = page.locator("//button[@data-trigger-id='digitalmat-1']")
    iphone_button.click()
