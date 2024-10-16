import time 
import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://testautomationpractice.blogspot.com/"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_alert(driver):
    alert_btn = driver.find_element(By.XPATH, '''//*[@id="promptBtn"]''')
    alert_btn.click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.send_keys("prince caspian")
    alert.accept()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="demo"]''')))
    assert driver.find_element(By.XPATH, '''//*[@id="demo"]''').text == "Hello prince caspian! How are you today?"
    time.sleep(4)