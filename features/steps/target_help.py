from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given("Open target help page 'https://help.target.com/help'")
def click_target_help(context):
    context.driver.get("https://help.target.com/help")
    #sleep(2)


@then('Verify Target Help page is opened')
def verify_target_help_url(context):
    assert '/help' in context.driver.current_url, f"Error: Expected /help url!"


@then('Verify Target Help Logo is present')
def verify_target_help_logo(context):
    expected_header = 'Target Help'
    result_header = context.driver.find_element(By.CSS_SELECTOR, "[class='custom-h2']").text
    assert result_header == expected_header, f"Error: Expected header is {expected_header} but found {result_header}"


@then('Verify Search Text field')
def verify_search_field(context):
    result = context.driver.find_element(By.CSS_SELECTOR, "[class='search-input']").is_displayed()
    assert result is True, f"Error: Missing Search Text Field!"


@then('Verify Search Button field')
def verify_search_button(context):
    result = context.driver.find_element(By.CSS_SELECTOR, "[class='btn-sm search-btn']").is_displayed()
    assert result is True, f"Error: Missing Search Button Field!"


@then("Verify header 'What would you like field' displayed")
def verify_liking_header(context):
    expected_header = 'What would you like to do?'
    result_header = context.driver.find_element(By.CSS_SELECTOR, "h2[class='custom-h2 header']").text
    assert result_header == expected_header, f"Error: Expected header is {expected_header} but got {result_header}"


@then("Verify 'What would you like field' has {number} elements")
def your_liking_elements(context, number):
    liking_elements = context.driver.find_elements(By.XPATH, "(//div[@class='col-lg-12'])[1] //div[@class='grid_6']")
    assert len(liking_elements) == int(number), f"Error: Expected {number} elements but got {len(liking_elements)}"


@then('Verify Help block has {number} elements')
def verify_help_block(context, number):
    help_elements = context.driver.find_elements(By.CSS_SELECTOR, "[class*='grid_4']")
    assert len(help_elements) == int(number), f"Error: Expected {number} of elements, but found {len(help_elements)}"


@then("Verify header 'Browse all Help pages'")
def verify_help_header(context):
    expected_text = "Browse all Help pages"
    result_text = context.driver.find_element(By.CSS_SELECTOR, "#divID1 h2").text
    assert result_text == expected_text, f"Error: Expected text is {expected_text}, but found {result_text}"




