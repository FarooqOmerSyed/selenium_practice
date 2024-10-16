import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "https://testautomationpractice.blogspot.com/"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()

def test_dbcbtn(driver):
    input_field = driver.find_element(By.ID, "field1")
    input_field.clear()
    input_field.send_keys("oh hello! this is a test")
    time.sleep(2)
    
    submit_btn = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
    actions = ActionChains(driver)
    actions.double_click(submit_btn).perform()
    
    time.sleep(2)
