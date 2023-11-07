Feature: Testing cart features

  Scenario: User check the added product to the cart
    Given Launch home page
    When  Enter the product to search and click
    And   Select the item of your choice and click Add to cart
    And   From right side navigation menu, click on "View cart & check out"
    Then  Verify cart has single cart item
