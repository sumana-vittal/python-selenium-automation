Feature:Test for Target Help UI

  Scenario:User check for the Target Help Logo
    Given Open target help page 'https://help.target.com/help'
    Then  Verify Target Help page is opened
    And   Verify Target Help Logo is present

  Scenario:User check for the Search Text
    Given Open target help page 'https://help.target.com/help'
    Then  Verify Target Help page is opened
    And   Verify Search Text field

  Scenario:User check for the Search Button
    Given Open target help page 'https://help.target.com/help'
    Then  Verify Target Help page is opened
    And   Verify Search Button field

  Scenario:User check for the UI element 'What would you like field'
    Given Open target help page 'https://help.target.com/help'
    Then  Verify Target Help page is opened
    And   Verify header 'What would you like field' displayed
    And   Verify 'What would you like field' has 7 elements

  Scenario:User check for the Target Help block elements
    Given Open target help page 'https://help.target.com/help'
    Then  Verify Target Help page is opened
    Then  Verify Help block has 3 elements

  Scenario:User check for the header 'Browse all Help pages'
   Given Open target help page 'https://help.target.com/help'
    Then  Verify Target Help page is opened
    Then  Verify header 'Browse all Help pages'

