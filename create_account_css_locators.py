from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# create driver instance
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the browser
driver.get("https://www.amazon.com/")
sleep(2)
driver.refresh()
sleep(2)

# click on the signin
driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()

# click on create account button
driver.find_element(By.CSS_SELECTOR, "a#createAccountSubmit").click()

# check for the amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon")

# create account header
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# your name field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# mobile number or email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

sleep(2)
# password field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Re-enter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# continue button
driver.find_element(By.CSS_SELECTOR, "[type='submit']")

# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# Privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

#sign in
driver.find_element(By.CSS_SELECTOR,"div.a-row a.a-link-emphasis[href*='signin']")

sleep(2)


# close all instances of browser
driver.quit()
