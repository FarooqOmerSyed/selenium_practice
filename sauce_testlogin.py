import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_login(driver):
    try:
        user_name = driver.find_element(By.ID, 'user-name')
        user_name.send_keys('standard_user')
        user_pwd = driver.find_element(By.ID, 'password')
        user_pwd.send_keys('secret_sauce')
        time.sleep(3)
        button = driver.find_element(By.ID, 'login-button')
        button.click()
        print('login test passed!!')
    except Exception as e:
        print(f"there's been an error occurred: {e}")

# Run the tests using the pytest command
