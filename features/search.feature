Feature: Search functionality

  @search
  Scenario: Search fo valid product
    Given I got navigated to home page
    When I enter valid product say "iphone" into the search box field
    And I click on search button
    Then Valid product should get displayed in search results

  @search
  Scenario: Search for an invalid product
    Given I got navigated to home page
    When I entered invalid product say "car" into the search box field
    And I click on search button
    Then Proper message should be displayed in search results

  @search
  Scenario: Search without entering any product
    Given I got navigated to home page
    When I dont enter anything into search box field
    And I click on search button
    Then Proper message should be displayed in search results