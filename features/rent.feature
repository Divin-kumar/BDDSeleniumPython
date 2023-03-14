Feature: Rent functionality

  Scenario: Accessing Rent Property based on the locality
    Given I open Application URL in the Browser
    And I navigate to rent tab
    When I open Owner Properties
    And I click on Top Localities and preferred Property
    Then I should get Property in that Locality

  Scenario: Accessing Rental Properties based on the preferred location
    Given I open Application URL in the Browser
    And I navigate to rent tab
    When I select the location as chennai
    And I click the search button
    Then I should access Properties in chennai

  Scenario: Accessing Top Agents in Chennai location
    Given I open Application URL in the Browser
    And I select chennai as the location
    When I click the search button
    And I click on Top Agents button
    Then I should get access to the Top Agents page in Chennai

  Scenario: Accessing Ask a Question page
    Given I open Application URL in the Browser
    And I navigate to rent tab
    When I click find an agent to enter agent page
    And I click Ask a Question option
    Then I should get access to the Ask a Question page

  Scenario: Setting Property Alert
    Given I open Application URL in the Browser
    And I enter into the Top Agent page
    When I enter to Set a Property alert
    And I enter the valid details
    Then I should get to the Login Page
