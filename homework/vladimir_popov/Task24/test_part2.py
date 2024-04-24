import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


cookies_confirm_button_locator = (By.XPATH, "//*[@class='fc-footer-buttons-container']//button[contains(@class, 'fc-cta-consent')]")


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_add_to_compare(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    actions = ActionChains(driver)
    first_item = driver.find_element(By.XPATH, "//*[@data-product-id='14']")
    cookies_confirm_button = driver.find_element(*cookies_confirm_button_locator)
    cookies_confirm_button.click()
    add_to_compare_button = driver.find_element(By.XPATH, "//*[@title='Add to Compare']")
    actions.move_to_element(first_item).move_to_element(add_to_compare_button).click(add_to_compare_button).perform()
    first_compare_item = driver.find_element(By.XPATH, "//a[text()='Push It Messenger Bag']")
    first_compare_item.is_displayed()
