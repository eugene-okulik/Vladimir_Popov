from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


# def test_choose_language(driver):
#     driver.get("https://www.qa-practice.com/elements/select/single_select")
#     input_language = 'Python'
#     choose_language_field = driver.find_element(By.ID, "id_choose_language")
#     choose_language_field.click()
#     language = driver.find_element(By.XPATH, f"//*[@id='id_choose_language']//option[text()='{input_language}']")
#     language.is_displayed()
#     language.click()
#     choose_language_field.click()
#     submit_button = driver.find_element(By.ID, "submit-id-submit")
#     submit_button.is_displayed()
#     submit_button.click()
#     result_text = driver.find_element(By.ID, "result-text").text
#     assert result_text == input_language


def test_hello_world_is_displayed(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.ID, "start")
    start_button.is_displayed()
    start_button.click()
    hello_world = driver.find_element(By.XPATH, "//*[@id='finish']")
    hello_world.is_displayed()
