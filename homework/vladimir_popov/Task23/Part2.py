from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

first_name_field_lokator = "firstName"
last_name_field_lokator = "lastName"
email_field_lokator = "//*[@id='userEmail-wrapper']//input"
gender_male_radiobutton_lokator = "//label[@for='gender-radio-1']"
mobile_number_field_lokator = "userNumber"
date_of_birth_field_lokator = "dateOfBirthInput"
year_dropdown_lokator = '//select[@class="react-datepicker__year-select"]'
month_dropdown_lokator = '//select[@class="react-datepicker__month-select"]'
subjects_container_lokator = "subjectsInput"
sports_checkbox_lokator = "//label[@for='hobbies-checkbox-1']"
reading_checkbox_lokator = "//label[@for='hobbies-checkbox-2']"
music_checkbox_lokator = "//label[@for='hobbies-checkbox-3']"
current_address_field_lokator = "currentAddress"
state_field_lokator = "//*[@id='state']//input"
city_field_lokator = "//*[@id='city']//input"
submit_button_lokator = "submit"
student_name_field_table_lokator = "//td[1][text()='Student Name']//ancestor::tr//td[2]"
student_email_field_table_lokator = "//td[1][text()='Student Email']//ancestor::tr//td[2]"
student_gender_field_table_lokator = "//td[1][text()='Gender']//ancestor::tr//td[2]"
student_mobile_field_table_lokator = "//td[1][text()='Mobile']//ancestor::tr//td[2]"
student_date_of_birth_field_lokator = "//td[1][text()='Date of Birth']//ancestor::tr//td[2]"
student_subjects_field_lokator = "//td[1][text()='Subjects']//ancestor::tr//td[2]"
student_hobbies_field_lokator = "//td[1][text()='Hobbies']//ancestor::tr//td[2]"
student_address_field_lokator = "//td[1][text()='Address']//ancestor::tr//td[2]"
student_state_and_city_field_lokator = "//td[1][text()='State and City']//ancestor::tr//td[2]"

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()


def choose_date_of_birth(day, month_of_birth, year):
    date_of_birth_field.is_displayed()
    date_of_birth_field.click()
    year_dropdown = driver.find_element(By.XPATH, year_dropdown_lokator)
    month_dropdown = driver.find_element(By.XPATH, month_dropdown_lokator)
    year_dropdown.is_displayed()
    year_dropdown.click()
    year = driver.find_element(By.XPATH, f'//select[@class="react-datepicker__year-select"]//option[@value="{year}"]')
    year.click()
    year_dropdown.click()
    month_dropdown.is_displayed()
    month_dropdown.click()
    month = driver.find_element(By.XPATH, f'//select[@class="react-datepicker__month-select"]//option'
                                f'[text()="{month_of_birth}"]'
                                )
    month.click()
    month_dropdown.click()
    day = driver.find_element(By.XPATH, f'//div[contains(@aria-label,"{month_of_birth} {day}")]')
    day.click()


first_name_field = driver.find_element(By.ID, first_name_field_lokator)
first_name_field.send_keys("Max")
last_name_field = driver.find_element(By.ID, last_name_field_lokator)
last_name_field.send_keys("Mustermann")
email_field = driver.find_element(By.XPATH, email_field_lokator)
email_field.send_keys("max.mustermann@mail.com")
gender_male_radiobutton = driver.find_element(By.XPATH, gender_male_radiobutton_lokator)
gender_male_radiobutton.click()
mobile_number_field = driver.find_element(By.ID, mobile_number_field_lokator)
mobile_number_field.send_keys("4955557871")
date_of_birth_field = driver.find_element(By.ID, date_of_birth_field_lokator)
choose_date_of_birth(12, "January", 2000)
subjects_container_field = driver.find_element(By.ID, subjects_container_lokator)
subjects_container_field.send_keys("Maths")
subjects_container_field.send_keys(Keys.RETURN)
subjects_container_field.send_keys("Computer Science")
subjects_container_field.send_keys(Keys.RETURN)
subjects_container_field.send_keys("Physics")
subjects_container_field.send_keys(Keys.RETURN)
submit_button = driver.find_element(By.ID, submit_button_lokator)
driver.execute_script("arguments[0].scrollIntoView(true)", submit_button)
sports_checkbox_field = driver.find_element(By.XPATH, sports_checkbox_lokator)
sports_checkbox_field.is_enabled()
sports_checkbox_field.click()
reading_checkbox_field = driver.find_element(By.XPATH, reading_checkbox_lokator)
reading_checkbox_field.is_displayed()
reading_checkbox_field.click()
music_checkbox_field = driver.find_element(By.XPATH, music_checkbox_lokator)
music_checkbox_field.is_displayed()
music_checkbox_field.click()
current_address_field = driver.find_element(By.ID, current_address_field_lokator)
current_address_field.send_keys("Teststrasse, 1")
state_field = driver.find_element(By.XPATH, state_field_lokator)
state_field.send_keys("NCR")
state_field.send_keys(Keys.RETURN)
city_field = driver.find_element(By.XPATH, city_field_lokator)
city_field.send_keys("Delhi")
city_field.send_keys(Keys.RETURN)
submit_button.is_displayed()
submit_button.is_enabled()
submit_button.click()

student_name_result = driver.find_element(By.XPATH, student_name_field_table_lokator).text
student_email_result = driver.find_element(By.XPATH, student_email_field_table_lokator).text
student_gender_result = driver.find_element(By.XPATH, student_gender_field_table_lokator).text
student_mobile_result = driver.find_element(By.XPATH, student_mobile_field_table_lokator).text
student_date_of_birth_result = driver.find_element(By.XPATH, student_date_of_birth_field_lokator).text
student_subjects_result = driver.find_element(By.XPATH, student_subjects_field_lokator).text
student_hobbies_result = driver.find_element(By.XPATH, student_hobbies_field_lokator).text
student_address_result = driver.find_element(By.XPATH, student_address_field_lokator).text
student_state_and_city_result = driver.find_element(By.XPATH, student_state_and_city_field_lokator).text

print(f"Student Name: {student_name_result}")
print(f"Student Email: {student_email_result}")
print(f"Gender: {student_gender_result}")
print(f"Mobile: {student_mobile_result}")
print(f"Date of Birth: {student_date_of_birth_result}")
print(f"Subjects: {student_subjects_result}")
print(f"Hobbies: {student_hobbies_result}")
print(f"Address: {student_address_result}")
print(f"State and City: {student_state_and_city_result}")
