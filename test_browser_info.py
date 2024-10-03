import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://practice.expandtesting.com/my-browser"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()

def test_browser_info(driver):
    info_button = driver.find_element(By.ID, "browser-toggle")
    info_button.click()

    time.sleep(2)

    table_id = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "browser-platform")))
    assert table_id.text == "Win32"
