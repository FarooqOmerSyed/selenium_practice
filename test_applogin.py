import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://practice.expandtesting.com/notes/app/login'


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    input_email = driver.find_element(By.ID, 'email')
    input_email.clear()
    input_email.send_keys('exampple@gmail.com')

    time.sleep(2)

    input_password = driver.find_element(By.ID, 'password')
    input_password.clear()
    input_password.send_keys('123@Abcd')

    time.sleep(2)

    submit_button = driver.find_element(By.XPATH,
                                        '''/html/body/main/div[2]/div/div/div/div/div/div/div/form/div[2]/button''')
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '''/html/body/main/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div''')))

    result_message = driver.find_element(By.XPATH,
                                         '''/html/body/main/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div''')

    assert 'Incorrect email address or password' in result_message.text, 'test failed!!'


