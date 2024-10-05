import time 
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


global url 
url = "https://www.calculator.net/bmi-calculator.html"

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_bmi_calculator(driver):
    age_select = driver.find_element(By.ID, "cage")
    age_select.clear()
    age_select.send_keys("27")

    time.sleep(1)

    gender_select = driver.find_element(By.XPATH, '''/html/body/div[3]/div[1]/div[4]/div[2]/table/tbody/tr/td/form/table[1]/tbody/tr[2]/td[2]/label[2]/span''')
    gender_select.click()

    time.sleep(1)

    height_input = driver.find_element(By.ID, "cheightmeter")
    height_input.clear()
    height_input.send_keys("143")

    time.sleep(1)

    weight_input = driver.find_element(By.ID, "ckg")
    weight_input.clear()
    weight_input.send_keys("56")

    time.sleep(1)

    submit_button = driver.find_element(By.NAME, "x")
    submit_button.click()

    time.sleep(4)