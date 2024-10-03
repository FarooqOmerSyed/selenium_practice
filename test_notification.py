import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://practice.expandtesting.com/notification-message-rendered"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_notification_message(driver):
    # Wait for the link to be clickable
    notification_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Click here"))
    )
    notification_link.click()
    
    # Wait for the notification message to appear
    notification_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    
    # Check the text of the notification message
    assert "Action successful" in notification_message.text or "Action unsuccessful, please try again" in notification_message.text
