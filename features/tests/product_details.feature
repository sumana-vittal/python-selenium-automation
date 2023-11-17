Feature: Test scenarios for product details

  Scenario: verify the colors of the product
    Given Open product page A-89191279
    Then verify each color can be selected

  Scenario: verify the colors product image and title
    Given Open target home page
    When  Search for tea
    Then Verify every product on Target Search result page has product name and product image