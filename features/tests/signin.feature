Feature: Testing the signin features

 Scenario: User check Logged out user can access Sign In
    Given Open target home page
    When  Click on Sign In
    And   From right side navigation menu, click Sign In
    Then  Verify Sign In form opened
