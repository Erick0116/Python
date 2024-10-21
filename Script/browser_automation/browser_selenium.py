from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    # Open Facebook
    driver.get("https://www.bullhorn.com/client-login/")
    time.sleep(2)

    # Locate the email and password fields
    email_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Enter your credentials
    email_field.send_keys("your_email@example.com")  # Replace with your email
    password_field.send_keys("your_password")          # Replace with your password

    # Click the login button
    login_button = driver.find_element(By.NAME, "Login2")
    login_button.click()
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)
