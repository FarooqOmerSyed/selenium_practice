import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.children.org/'

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures('driver')
def test_dropdown(driver):
    wait = WebDriverWait(driver, 6)
    
    dropdown = wait.until(EC.presence_of_element_located((By.ID, 'country')))
    dropdown2 = wait.until(EC.presence_of_element_located((By.ID, 'Gender')))
    
    select = Select(dropdown)
    select2 = Select(dropdown2)
    
    select.select_by_visible_text('India')
    select2.select_by_visible_text('Boys')
    
    time.sleep(2)
    
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '''//form//a[3]''')))
    button.click()
    
   
