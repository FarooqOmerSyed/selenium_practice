import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

url = "https://the-internet.herokuapp.com/context_menu"


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()


def test_context_menu(driver):
    element = driver.find_element(By.ID, 'hot-spot')
    actions = ActionChains(driver)
    actions.context_click(element).perform()

    time.sleep(3)

    alert = Alert(driver)
    alert_text = alert.text
    assert alert_text == "You selected a context menu", "failed miserbley"
    time.sleep(1)
    alert.accept()
    print("the text is successfully accepted")


