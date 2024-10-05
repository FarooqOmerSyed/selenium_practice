import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

global url 
url = "https://practice.expandtesting.com/forgot-password"

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()

def test_forgot_password(driver):
    user_email = driver.find_element(By.ID, "email")
    user_email.send_keys("oolwabbvfogerdolif@hthlm.com")
    submit_button = driver.find_element(By.XPATH, '''/html/body/main/div[2]/div/div/div/div/div/form/button''')
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '''/html/body/main/div[2]/div/div/p''')))

    success_message = driver.find_element(By.XPATH, '''/html/body/main/div[2]/div/div/p''')

    assert success_message.text == "An e-mail has been sent to you which explains how to reset your password.", "failed to reset password"