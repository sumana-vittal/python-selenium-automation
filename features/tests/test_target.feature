Feature: Testing Target.com features

  Scenario: User check for empty cart message
    Given Open target home page
    When  Click on the Cart icon
    Then  Verify "Your cart is empty" message is displayed

  Scenario: User check Logged out user can access Sign In
    Given Open target home page
    When  Click on Sign In
    And   From right side navigation menu, click Sign In
    Then  Verify Sign In form opened

  Scenario: User check the added product to the cart
    Given Open target home page
    When  Search the product to add
    And   Select the product by clicking on Add to cart
    And   From right side navigation menu, click "View cart & check out"
    Then  Verify cart has individual cart items and the total price

