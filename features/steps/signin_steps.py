from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify "Your cart is empty" message is displayed')
def verify_empty_cart_message(context):
    result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert result == 'Your cart is empty', f"Error: Expected 'Your cart is empty' but got {result}"


@when('Click on Sign In')
def click_on_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign In')
def click_menu_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_sign_in_opened(context):
    result_sign_in_button = context.driver.find_element(By.ID, "login").is_displayed()
    result_user_field = context.driver.find_element(By.ID, "username").is_displayed()
    assert (result_sign_in_button and result_user_field) is True, f"Error: Expected the Sign In page!"