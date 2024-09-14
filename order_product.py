from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (make sure to have the appropriate driver for your browser)
driver = webdriver.Firefox()

try:
    # Open Amazon
    driver.get('https://www.amazon.com')

    # Search for the product
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.send_keys('bluetooth speaker')
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Select the first product from the search results
    first_product = driver.find_element(By.CSS_SELECTOR, 'div.s-main-slot div.s-result-item')
    first_product.click()
    time.sleep(2)

    # Add the product to the cart
    add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-button')
    add_to_cart_button.click()
    time.sleep(2)

    # Proceed to checkout
    proceed_to_checkout_button = driver.find_element(By.ID, 'hlb-ptc-btn-native')
    proceed_to_checkout_button.click()
    time.sleep(2)

    # Place the order (this step is commented out for safety)
    # place_order_button = driver.find_element(By.NAME, 'placeYourOrder1')
    # place_order_button.click()

finally:
    # Close the browser
    driver.quit()
