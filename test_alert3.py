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
    alert_btn = driver.find_element(By.XPATH, '''//*[@id="confirmBtn"]''')
    alert_btn.click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()
    time.sleep(2)
    assert alert_text == "Press a button!", "FAILED: Alert message is not correct"
    time.sleep(2)