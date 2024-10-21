from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    # Open Facebook
    driver.get("https://www.facebook.com")

    # Wait for the page to load
    time.sleep(2)

    # Locate the email and password fields
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "pass")

    # Enter your credentials
    email_field.send_keys("your_email@example.com")  # Replace with your email
    password_field.send_keys("your_password")          # Replace with your password

    # Click the login button
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Wait for a while to ensure the login process completes
    time.sleep(5)

    # At this point, you should be logged in. You can add additional actions here.

except Exception as e:
    print("An error occurred:", e)

# The browser will remain open for you to observe the logged-in state.
