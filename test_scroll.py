import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

global url 
url = "https://www.amazon.in/"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_scroll(driver):
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("tecno pop 9")
    time.sleep(2)
    driver.find_element(By.ID, "nav-search-submit-button").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    
    

