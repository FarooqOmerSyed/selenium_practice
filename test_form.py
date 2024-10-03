import time 
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://practice.expandtesting.com/form-validation"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()


def test_form(driver):
    user_name = driver.find_element(By.ID, "validationCustom01")
    user_name.send_keys("selenium")

    contact_number = driver.find_element(By.NAME, "contactnumber")
    contact_number.send_keys("123-1234567")
