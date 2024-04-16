from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/input/simple")
driver.maximize_window()
text_string = driver.find_element(By.ID, "id_text_string")
text_string.send_keys("TestVP")
text_string.send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "result-text")))
result_string = driver.find_element(By.ID, "result-text")
result_text = result_string.text
print(result_text)
