from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open target.com')
def open_home_page(context):
    context.driver.get("https://www.target.com/")


@when('Click on the target circle')
def click_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='TargetCircle']").click()


@then('Verify the target circle url is opened')
def verify_website(context):
    result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='circle-logo']").is_displayed()
    assert result is True, f"Error: Not an expected page!"


@then('Verify the {number} benefit boxes')
def verify_benefit_box(context,number):
    benefit_webelements = context.driver.find_elements(By.CSS_SELECTOR, "[class*='BenefitsGrid'] li")
    assert len(benefit_webelements) == int(number), (f"Error: Expected number of benefit boxes is {number}, but found "
                                                     f"{len(benefit_webelements)}")

