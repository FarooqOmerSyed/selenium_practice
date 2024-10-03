from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Replace with the path to your WebDriver (e.g., chromedriver)
driver = webdriver.Firefox()

# Open the webpage
driver.get("https://practice.expandtesting.com/drag-and-drop")
driver.maximize_window()

# Locate draggable and droppable elements
draggable_element = driver.find_element(By.ID, "column-a")
droppable_element = driver.find_element(By.ID, "column-b")

# Create an ActionChains object
actions = ActionChains(driver)
time.sleep(4)
# Perform drag and drop
actions.drag_and_drop(draggable_element, droppable_element).perform()



# Close the browser
driver.quit()

print("Drag and drop test completed!")