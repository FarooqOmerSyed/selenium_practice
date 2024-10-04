import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

url = "https://practice.expandtesting.com/download"
download_dir = "C:\\Users\\OMER FAROOQ SYED\\Desktop"

@pytest.fixture()
def driver():
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    yield driver
    driver.quit()

def test_download_file(driver):
    file_download = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '''/html/body/main/div[2]/div/div/div[27]/a'''))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", file_download)  # Scroll the element into view
    file_download.click()
    
    # Wait for the file to be downloaded
    time.sleep(5)  # Adjust the sleep time as needed

    # Verify the file is downloaded
    downloaded_file = os.path.join(download_dir, "some-file.txt")  # Update with the actual file name and extension
    assert os.path.exists(downloaded_file), "File download failed"

    print("File downloaded successfully")
