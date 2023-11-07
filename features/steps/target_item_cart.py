from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Launch home page')
def launch_home_page(context):
    context.driver.get("https://www.target.com")


@when('Enter the product to search and click')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys('mug')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


@when('Select the item of your choice and click Add to cart')
def add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor13891751']").click()


@when('From right side navigation menu, click on "View cart & check out"')
def click_cart_checkout(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()


@then('Verify cart has single cart item')
def verify_cart_item(context):
    expected_text = '1 item'
    result_text = (context.driver.find_element(By.CSS_SELECTOR, "span[class*='styles__CartSummarySpan']").
                   text)
    assert expected_text in result_text, f"Error: Expected text {expected_text} is not {result_text}."



