from pages.base_page import BasePage
from playwright.sync_api import expect


first_item_locator = "//*[@data-product-id='2017']"
add_to_compare_button_locator = "//*[@title='Add to Compare']"
first_compare_item_locator = "//a[text()='Ana Running Short']"
add_to_cart_button_locator = "//form[@data-product-sku='WSH10']//button[@title='Add to Cart']"
clear_compare_items_button_locator = "//*[@id='compare-clear-all']"
popup_accept_button_locator = "//button[contains(@class, 'action-accept')]"


class EcoFriendlyCollectionPage(BasePage):
    new_page = "collections/eco-friendly.html"

    def add_to_compare(self):
        first_item = self.find(first_item_locator)
        first_item.hover()
        add_to_compare_button = self.find(add_to_compare_button_locator)
        add_to_compare_button.click()

    def check_compared_item_added(self):
        self.find(first_compare_item_locator)

    def add_item_to_cart(self):
        first_item = self.find(first_item_locator)
        first_item.hover()
        add_to_cart_button = self.find(add_to_cart_button_locator)
        add_to_cart_button.click()

    def clear_compare_items(self):
        clear_compare_items_button = self.find(clear_compare_items_button_locator)
        clear_compare_items_button.click()
        popup_accept_button = self.find(popup_accept_button_locator)
        popup_accept_button.click()

    def check_compare_item_is_not_visible(self):
        first_item_locator = self.find(first_compare_item_locator)
        expect(first_item_locator).not_to_be_visible()
