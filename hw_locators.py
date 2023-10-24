from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new chrome browser instance
service = Service(driver_path)
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(service=service)# options=chrome_options)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

# to handle captcha
sleep(2)
driver.refresh()
sleep(2)

# click on the sign-in link
driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']").click()

# Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email field
driver.find_element(By.ID, "ap_email").send_keys("abc@gmail.com")

# Continue button
driver.find_element(By.ID, "continue")

# Conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(), 'Conditions of Use')]")

# Privacy Notice link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(), 'Privacy Notice')]")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

# Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

#clear up all history and quit the browser instance
driver.quit()
