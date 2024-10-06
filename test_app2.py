import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://practice.expandtesting.com/tracalorie/"


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()


def test_app(driver):
    item_name = driver.find_element(By.ID, 'item-name')
    item_name.clear()
    item_name.send_keys('banana')
    time.sleep(2)

    item_calories = driver.find_element(By.ID, 'item-calories')
    item_calories.clear()
    item_calories.send_keys('121')
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, '''/html/body/div[1]/div/div/form/div/button[1]''')
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '''/html/body/div[1]/ul/li[1]/em''')))

    first_item_calories = driver.find_element(By.XPATH, '''/html/body/div[1]/ul/li[1]/em''')

    assert '121 Calories' in first_item_calories.text, 'FAIL: Item calories do not match!'
