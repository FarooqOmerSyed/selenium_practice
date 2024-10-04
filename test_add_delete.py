import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://practice.expandtesting.com/add-remove-elements"

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_delete(driver):
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(3):
        add_button.click()

    # Wait for the delete buttons to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually"))
    )
    
    # Find all delete buttons
    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
    
    for delete_button in delete_buttons:
        delete_button.click()
