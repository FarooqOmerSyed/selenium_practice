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
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()

def test_alert(driver):
    alert_btn = driver.find_element(By.XPATH, '''//*[@id="alertBtn"]''')
    alert_btn.click()
    
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    
    alert = Alert(driver)
    alert_text = alert.text
    alert.accept()
    
    time.sleep(2)
    assert alert_text == "I am an alert box!", "FAIL: Incorrect alert text"
