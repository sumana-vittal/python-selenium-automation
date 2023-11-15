from time import sleep

from behave import given, then, when
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.target.com")
element = driver.find_element(By.CSS_SELECTOR, "[href='https://help.target.com/help']")
print(element.text)
action = ActionChains(driver)
action.move_to_element(element)

action.click(on_element=element)
action.perform()
sleep(2)

driver.quit()
