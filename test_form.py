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
    user_name.clear()
    user_name.send_keys("selenium")

    time.sleep(1)

    contact_number = driver.find_element(By.NAME, "contactnumber")
    contact_number.send_keys("123-1234567")

    time.sleep(1)

    pickupdate = driver.find_element(By.NAME, "pickupdate")
    try:
       pickupdate.send_keys("03-10-2024")
    except Exception as e:
       print(f"Error sending date: {e}")

    
    driver.execute_script("arguments[0].value = '03-10-2024';", pickupdate)
    pickupdate.send_keys("03-10-2024")

    time.sleep(3)

    payment = driver.find_element(By.NAME, "payment")
    select = Select(payment)
    select.select_by_visible_text("card")

    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, '''/html/body/main/div[2]/div/div/div/div/form/div[5]/button''')
    submit_button.click()
