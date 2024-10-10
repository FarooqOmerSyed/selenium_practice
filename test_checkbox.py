import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://the-internet.herokuapp.com/checkboxes"


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()


def test_checkboxes(driver):
    checkboxes = driver.find_elements(By.TAG_NAME, "input")
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
            time.sleep(2)

    for checkbox in checkboxes:
        assert checkbox.is_selected(), "the checkbox should be selected"

    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()
            time.sleep(2)



