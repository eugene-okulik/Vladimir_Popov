import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from time import sleep


add_to_card_button_locator = (By.XPATH, "//*[@onclick='addToCart(1)']")
cart_button_locator = (By.XPATH, "//*[@id='cartur']")


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def test_item_added_to_cart(driver):
    driver.get("https://www.demoblaze.com/index.html")
    wait = WebDriverWait(driver, 5)
    phone = "Samsung galaxy s6"
    item1_locator = (By.XPATH, f"//a[text()='{phone}']")
    wait.until(EC.visibility_of_element_located(item1_locator))
    item = driver.find_element(*item1_locator)
    ActionChains(driver).key_down(Keys.CONTROL).click(item).key_up(Keys.CONTROL).perform()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    wait.until(EC.visibility_of_element_located(add_to_card_button_locator))
    add_to_card_button = driver.find_element(*add_to_card_button_locator)
    add_to_card_button.click()
    alert = Alert(driver)
    wait.until(EC.alert_is_present)
    alert.accept()
    wait.until(EC.visibility_of_element_located(cart_button_locator))
    cart_button = driver.find_element(*cart_button_locator)
    driver.close()
    driver.switch_to.window(windows[0])
    cart_button = driver.find_element(*cart_button_locator)
    cart_button.click()
    item1_locator = (By.XPATH, f"//td[text()='{phone}']")
    wait.until(EC.visibility_of_element_located(item1_locator))
    item = driver.find_element(*item1_locator)
