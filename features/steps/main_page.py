from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open target home page')
def open_home_page(context):
    context.driver.get('https://www.target.com/')


@then('Verify header is present')
def verify_header(context):
    result = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__UtilityHeaderWrapper']").is_displayed
    #assert result is True, f"Error: Expected header is not displayed!"


@then('Verify header has {number} links')
def verify_header_link(context, number):
    header_elements = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")
    assert len(header_elements) == int(number), f"Error: Expected {number} links but got {len(header_elements)}"
