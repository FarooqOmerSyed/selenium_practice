from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(11)   # wait for seconds best practice
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys('standard_user')
    driver.find_element(By.ID, "password").send_keys('secret_sauce')
    time.sleep(4)  # time module for wait -> better to use implicitly_wait
    driver.find_element(By.ID, "login-button").click()
    
    assert "Swag Labs" in driver.title
    driver.close()
