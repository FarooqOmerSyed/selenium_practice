from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
url = 'https://www.amazon.in/'

def search_amzn():
    try:
        driver.get(url)
        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.clear()
        search_box.send_keys('Lenovo Laptop')
        search_box.send_keys(Keys.RETURN)
        time.sleep(6)
    finally:
        driver.quit()
    
if __name__ == '__main__':
    search_amzn()
    





