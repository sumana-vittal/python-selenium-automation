from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")

#PRODUCT_LISTING = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_LISTING = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardVariantDefault']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")

#PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


@given('Open product page {product}')
def open_product_page(context, product):
    context.driver.get(f"https://www.target.com/p/{product}")


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


@then('Verify every product on Target Search result page has product name and product image')
def verify_product_image_and_title(context):
    # code for scrolling and loading products
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.driver.wait.until(EC.presence_of_element_located(PRODUCT_LISTING))
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.driver.wait.until(EC.presence_of_element_located(PRODUCT_LISTING))
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.driver.wait.until(EC.presence_of_element_located(PRODUCT_LISTING))

    products = context.driver.find_elements(*PRODUCT_LISTING)
    print(f"Found {len(products)} Products")
    for product in products:
        # check for the product image.
        product_img = product.find_element(*PRODUCT_IMAGE)
        assert product_img, "Missing product image!"

        # check for the product title.
        product_title = product.find_element(*PRODUCT_TITLE).text
        print(product_title)
        assert product_title, "Title of the product is missing!"


