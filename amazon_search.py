from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (make sure to have the appropriate driver for your browser)
driver = webdriver.Firefox()

try:
    # Open the website
    driver.get('https://www.amazon.in/')  # Replace with the actual URL

    # Find the search box using its ID and enter the search term
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')  # Replace 'search-box-id' with the actual ID
    search_box.clear()
    search_box.send_keys('bluetooth speaker')
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
