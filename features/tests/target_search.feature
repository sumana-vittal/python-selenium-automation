Feature: Search tests

  Scenario: User can search for coffee
    Given Open target home page
    When  Search for coffee
    Then  Verify search worked for coffee
    And   Verify coffee in search result url

  Scenario: User can search for tea
    Given Open target home page
    When  Search for tea
    Then  Verify search worked for tea
    And   Verify tea in search result url

  Scenario: User can search for christmas lights
    Given Open target home page
    When  Search for christmas lights
    Then  Verify search worked for christmas lights
    And   Verify christmas+lights in search result url

  Scenario Outline: User can search for a product
    Given Open target home page
    When  Search for <product>
    Then  Verify search worked for <product>
    And   Verify <expected_url> in search result url
    Examples:
    |product          | expected_url   |
    |coffee           | coffee         |
    |tea              |tea             |
    |christmas lights |christmas+lights|



