from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Open the webpage
driver.get("https://testautomationpractice.blogspot.com/")  
driver.maximize_window()
time.sleep(11)

# Locate the slider handle element
slider_handle = driver.find_element(By.XPATH, '''/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[8]/div[1]/div/span''')

# Get the initial slider position
initial_position = slider_handle.get_attribute("style").split(": ")[-1].rstrip(";")
print("Initial position:", initial_position)

# Generate a random percentage value between 1 and 100
random_position = str(random.randint(1, 100)) + "%"

# Set the slider position directly using JavaScript
driver.execute_script(f"arguments[0].style.left = '{random_position}';", slider_handle)

# Verify the new slider position
new_position = slider_handle.get_attribute("style").split(": ")[-1].rstrip(";")
print("New position:", new_position)
assert new_position == random_position, "Incorrect slider position after setting"

# wait for 5 seconds to see the result
time.sleep(5)

# Close the browser
driver.quit()


print("Slider test passed!")