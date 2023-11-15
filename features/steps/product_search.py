from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    #sleep(4)
    # context.driver.wait.until(
    #     EC.text_to_be_present_in_element_value((By.NAME, 'q'), search_word),
    #     message="Text is not updated in the element!"
    # )


@when('Click on search icon')
def click_search_icon(context):
    # sleep(1)
    # context.driver.wait.until(
    #     EC.visibility_of_element_located((By.NAME, 'btnK')),
    #     message="Submit button not present!"
    # )
    context.driver.find_element(*SEARCH_SUBMIT).click()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
