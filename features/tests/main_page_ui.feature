Feature: Main page UI tests

  Scenario: Header has correct amount of links
    Given Open target home page
    Then Verify header is present
    And Verify header has 5 links