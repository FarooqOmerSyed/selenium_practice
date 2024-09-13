from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

global url
url = "https://www.selenium.dev/documentation/webdriver/interactions/alerts/"


def test_alert_popup():
    driver = webdriver.Chrome()
    driver.get(url)
    element = driver.find_element(By.LINK_TEXT, "See an example alert")
    element.click()

    wait = WebDriverWait(driver, timeout=2)
    alert = wait.until(lambda d : d.switch_to.alert)
    text = alert.text
    alert.accept()
    assert text == "Sample alert"

    driver.quit()