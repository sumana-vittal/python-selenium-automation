from selenium.webdriver.common.by import By
from behave import given, then


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('Open product page https://www.target.com/p/A-89191279')
def open_product_page(context):
    context.driver.get("https://www.target.com/p/A-89191279")


@then('verify each color can be selected')
def verify_product_colors(context):
    expected_colors = ['Black', 'Green', 'Oatmeal', 'Red']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        actual_colors.append(selected_color)

    assert actual_colors == expected_colors, \
        f"Expected colors {expected_colors} didn't match with actual colors {actual_colors}"

