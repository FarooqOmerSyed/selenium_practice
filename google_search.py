from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def google_search(query):
    # Initialize the WebDriver
    driver = webdriver.Firefox()
    
    try:
        # Open Google
        driver.get('https://www.google.com')
        
        # Perform a search
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results to load
        time.sleep(3)
        
        # Verify the results
        assert query in driver.title
        print(f"Test passed: '{query}' found in title.")
        
    except AssertionError:
        print(f"Test failed: '{query}' not found in title.")
        
    finally:
        # Close the browser
        driver.quit()

# Call the function
google_search('Selenium WebDriver')
