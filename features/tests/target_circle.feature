Feature: Target circle UI tests

  Scenario: User checks the 5 benefit boxes
    Given Open target.com
    When  Click on the target circle
    Then  Verify the target circle url is opened
    And   Verify the 5 benefit boxes