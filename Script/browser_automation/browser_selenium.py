from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")

    # Locate the search box
    search_box = driver.find_element(By.NAME, "q")

    # Enter a search query
    search_box.send_keys("Code With Mosh")
    search_box.send_keys(Keys.RETURN)  # Press Enter

    # Wait for results to load
    time.sleep(2)

    # Find and print titles of search results
    results = driver.find_elements(By.CSS_SELECTOR, 'h3')
    for index, result in enumerate(results):
        print(f"{index + 1}: {result.text}")

finally:
    # Close the browser
    driver.quit()
