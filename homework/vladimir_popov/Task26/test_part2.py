from playwright.sync_api import Page, expect
from time import sleep


male_checkbox_locator = "//label[@for='gender-radio-1']"
date_of_birth_locator = "#dateOfBirthInput"
date_of_birth_dropdown_locator = "//*[@class='react-datepicker-popper']"
year_dropdown_locator = '//select[@class="react-datepicker__year-select"]'
month_dropdown_locator = '//select[@class="react-datepicker__month-select"]'
subjects_container_locator = "#subjectsInput"
sports_checkbox_locator = "//label[@for='hobbies-checkbox-1']"
reading_checkbox_locator = "//label[@for='hobbies-checkbox-2']"
music_checkbox_locator = "//label[@for='hobbies-checkbox-3']"
state_field_lokator = "//*[@id='state']//input"
city_field_lokator = "//*[@id='city']//input"


def test_part_two(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    first_name_field = page.get_by_role(role="textbox", name="First Name")
    first_name_field.fill("Max")
    last_name_field = page.get_by_role(role="textbox", name="Last Name")
    last_name_field.fill("Mustermann")
    email_field = page.get_by_role(role="textbox", name="name@example.com")
    email_field.fill("max.mustermann@mail.com")
    male_checkbox = page.locator(male_checkbox_locator)
    male_checkbox.click()
    user_number_field = page.get_by_role(role="textbox", name="Mobile Number")
    user_number_field.fill("015157770252")
    date_of_birth = page.locator(date_of_birth_locator)
    date_of_birth.click()
    year_dropdown = page.locator(year_dropdown_locator)
    year_dropdown.select_option("2000")
    month_dropdown = page.locator(month_dropdown_locator)
    month_dropdown.select_option("January")
    day = page.locator("//*[contains(@class, 'react-datepicker__day')][text()='22']")
    day.click()
    subjects_container_field = page.locator(subjects_container_locator)
    subjects_container_field.click()
    subjects_container_field.fill("Maths")
    subjects_container_field.press("Enter")
    subjects_container_field.fill("Computer Science")
    subjects_container_field.press("Enter")
    subjects_container_field.fill("Physics")
    subjects_container_field.press("Enter")
    sports_checkbox = page.locator(sports_checkbox_locator)
    sports_checkbox.click()
    reading_checkbox = page.locator(reading_checkbox_locator)
    reading_checkbox.click()
    music_checkbox = page.locator(music_checkbox_locator)
    music_checkbox.click()
    current_address_field = page.get_by_role(role="textbox", name="Current Address")
    current_address_field.fill("Teststraße 1, Musterstadt")
    state_field = page.locator(state_field_lokator)
    state_field.fill("NCR")
    state_field.press("Enter")
    city_field = page.locator(city_field_lokator)
    city_field.fill("Delhi")
    city_field.press("Enter")
    submit_button = page.get_by_role(role="button", name="submit")
    submit_button.click()
