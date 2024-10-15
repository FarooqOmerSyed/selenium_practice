import time
import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

url = "https://testautomationpractice.blogspot.com/"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window
    yield driver
    driver.quit()

def test_dynamicBtn(driver):
    btn = driver.find_element(By.XPATH, '''/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[2]/div[1]/button''')
    time.sleep(2)
    btn.click()
    time.sleep(2)
    if btn.text == "STOP" or "START":
        print("Dynamic button is working")
    else:
        print("Dynamic button is not working")