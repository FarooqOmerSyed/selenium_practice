import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://practice.expandtesting.com/upload"
file_path = "C:\\Users\\OMER FAROOQ SYED\\Desktop\\START-HERE.txt"

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()

def test_file_upload(driver):
    upload_file = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '''//*[@id="fileInput"]'''))
    )
    try:
        upload_file.send_keys(file_path)
    except Exception as e:
        print(f"Error: {e}")
        assert False, f"File upload failed: {e}"

    file_submit = driver.find_element(By.ID, 'fileSubmit')
    file_submit.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '''/html/body/main/div[2]/div/h1'''))
    )
    assert success_message.text == "File Uploaded!", "File upload was not successful"

    print("File uploaded successfully")
