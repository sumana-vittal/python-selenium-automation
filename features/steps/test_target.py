from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target home page')
def open_home_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on the Cart icon')
def click_on_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(2)


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


@when('Search the product to add')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys('mug')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


@when('Select the product by clicking on Add to cart')
def add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor13891751']").click()


@when('From right side navigation menu, click "View cart & check out"')
def click_cart_checkout(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()


@then('Verify cart has individual cart items and the total price')
def verify_cart_item(context):
    expected_text = '1 item'
    result_text = (context.driver.find_element(By.CSS_SELECTOR, "span[class*='styles__CartSummarySpan']").
                   text)
    assert expected_text in result_text, f"Error: Expected text {expected_text} is not {result_text}."


