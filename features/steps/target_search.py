from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, "search").send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()


@then('Verify search worked for {product}')
def verify_search(context, product):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert product in search_results_header, f"Error: Expected test {product} not in {search_results_header}"


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    assert expected_keyword in context.driver.current_url, f"Error: Expected result didn't match!"



