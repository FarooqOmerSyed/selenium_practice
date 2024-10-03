from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

global url 
url = "https://practice.expandtesting.com/drag-and-drop"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    draggable_element = driver.find_element(By.ID, "column-a")
    droppable_element = driver.find_element(By.ID, "column-b")
    actions = ActionChains(driver)
    time.sleep(4)
    actions.drag_and_drop(draggable_element, droppable_element).perform()

print("Drag and drop test completed!")