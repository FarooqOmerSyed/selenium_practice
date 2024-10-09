import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

url = "https://the-internet.herokuapp.com/broken_images"


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_broken_images(driver):
    images = driver.find_elements(By.TAG_NAME, 'img')
    broken_images = []

    for img in images:
        img_src = img.get_attribute('src')
        response = requests.get(img_src)

        if response.status_code != 200:
            broken_images.append(img_src)

    assert len(broken_images) != 0, f"Broken images found: {broken_images}"
