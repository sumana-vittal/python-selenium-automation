from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# install the driver path
driver_path = ChromeDriverManager().install()

# create the driver instance
service = Service(driver_path)

# set chromeoptions for incognito window
chrome_options = Options()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(service=service, options=chrome_options)

# set browser windows property
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

# code to handle captcha
sleep(2)
driver.refresh()
sleep(2)

# ope the orders page
driver.find_element(By.ID, "nav-orders").click()

# check if the opened url is the order sign in page.
expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH,  "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, \
        f" Error : Expected text {expected_result} didn't match with actual text {actual_result}"
print("Test case passed!")

# clear history and close all browser instances
driver.quit()
