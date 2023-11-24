from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@when('Click on the Cart icon')
def click_on_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    #sleep(2)
    #context.driver.wait.until(EC.url_contains("cart"), message="Cart page is not displayed!")


@when('Search the product to add')
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys('mug')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


@when('Select the product by clicking on Add to cart')
def add_to_cart(context):
    sleep(5)
    # context.driver.wait.until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='addToCartButton']")),
    #     message="Element not visible"
    # )
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='addToCartButton']").click()


@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not shown in side navigation'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when('From right side navigation menu, click "View cart & check out"')
def click_cart_checkout(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()


@then('Verify cart has correct product')
def verify_search(context):
    actual_text = context.driver.find_element(*SEARCH_RESULT_TXT).text
    assert context.product_name in actual_text, \
        f"Expected text '{context.product_name}' not in actual '{actual_text}'"


@then('Verify cart has individual cart items and the total price')
def verify_cart_item(context):
    expected_text = '1 item'
    result_text = (context.driver.find_element(By.CSS_SELECTOR, "span[class*='styles__CartSummarySpan']").
                   text)
    assert expected_text in result_text, f"Error: Expected text {expected_text} is not {result_text}."

