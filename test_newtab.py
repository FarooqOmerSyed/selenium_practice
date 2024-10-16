import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

def test_new_tab(driver):
    new_tab = driver.find_element(By.XPATH, '''/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[3]/div[1]/button''')
    new_tab.click()
    
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    assert driver.title == "Your Store"
    driver.close()

