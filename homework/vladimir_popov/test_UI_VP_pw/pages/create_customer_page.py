from pages.base_page import BasePage


first_name_field_locator = "#firstname"
last_name_field_locator = "#lastname"
email_field_locator = "#email_address"
password_field_locator = "#password"
password_confirm_field_locator = "#password-confirmation"
create_account_button_locator = "//button[contains(@class, 'submit')]"


class CreateCustomerPage(BasePage):
    new_page = "customer/account/create/"

    def add_first_name(self, first_name=""):
        first_name_field = self.find(first_name_field_locator)
        first_name_field.fill(first_name)

    def add_last_name(self, last_name):
        last_name_field = self.find(last_name_field_locator)
        last_name_field.fill(last_name)

    def add_email(self, email):
        email_field = self.find(email_field_locator)
        email_field.fill(email)

    def add_password(self, password):
        password_field = self.find(password_field_locator)
        password_field.fill(password)
        confirm_password_field = self.find(password_confirm_field_locator)
        confirm_password_field.fill(password)

    def click_create_account_button(self):
        create_account_button = self.find(create_account_button_locator)
        create_account_button.click()
