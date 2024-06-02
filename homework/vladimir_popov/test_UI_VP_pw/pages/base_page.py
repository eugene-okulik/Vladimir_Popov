from playwright.sync_api import expect, Page, Locator


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    new_page = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page:
            self.page.goto(f"{self.base_url}/{self.new_page}")
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator) -> Locator:
        return self.page.locator(locator).first

    def check_page(self, check_page):
        print(f"PAGE: {self.page.url}")
        self.page.wait_for_url(f"{self.base_url}/{check_page}")
        assert self.page.url == f"{self.base_url}/{check_page}"

    def check_field_required_error_message(self, field):
        field_required_error_message_locator = f"//*[@id='{field}-error']"
        field_required_error_message = self.find(field_required_error_message_locator)
        expect(field_required_error_message).to_be_visible()

    def check_element_text(self, locator, text):
        element = self.find(locator)
        expect(element).to_have_text(text)
