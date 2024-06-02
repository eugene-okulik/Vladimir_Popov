from pages.base_page import BasePage


womens_sales_button_locator = "//*[@class='more button'][text()='Shop Women’s Deals']"
mens_sales_icon_locator = "//*[@class='more icon'][text()='Shop Men’s Deals']"


class SalesPage(BasePage):
    new_page = "sale.html"
    womens_sales_button_locator = "//*[@class='more button'][text()='Shop Women’s Deals']"
    mens_sales_icon_locator = "//*[@class='more icon'][text()='Shop Men’s Deals']"

    def open_women_sales(self):
        womens_sales_button = self.find(womens_sales_button_locator)
        womens_sales_button.click()

    def open_men_sales(self):
        mens_sales_icon = self.find(mens_sales_icon_locator)
        mens_sales_icon.click()
