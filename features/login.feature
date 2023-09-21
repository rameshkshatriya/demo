Feature: Login functionality
  @login
  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on login button
    Then I should get logged in
    Examples:
      |email                |password   |
      |awsramesh8@gmail.com |Ramesh@123 |
      |awsramesh9@gmail.com |Ramesh@1234|
      |awsramesh10@gmail.com|Ramesh@12  |


  @login
  Scenario: Login with invalid email and valid password
    Given I navigated to login page
    When I enter invalid email and valid password say "Ramesh@123" into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I navigated to login page
    When I entered valid email say "awsramesh8@gmail.com" and invalid password say "12345" into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login with invalid credentials
    Given I navigated to login page
    When I enter invalid email and invalid password say "12345" into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
    Given I navigated to login page
    When I dont enter anything into email and password fields
    And I click on login button
    Then I should get a proper warning message