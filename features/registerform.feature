Feature: Register account functionality

  @register
  Scenario: Register with mandatory fields
      Given I navigate to register page
      When I entered below details into all mandatory felds
          |first_name|last_name|telephone |password|
          |suhas     |j chandra|1234567890|12345   |
      And select the private policy
      And I click on continue button
      Then Account should get created
  @register
  Scenario: Register with all fields
      Given I navigate to register page
      When I entered below details into all fields
          |first_name|last_name|telephone |password|
          |suhas     |j chandra|1234567890|12345   |
      And select the private policy
      And I click on continue button
      Then Account should get created
  @register
  Scenario: Register with a duplicate email address
      Given I navigate to register page
      When I entered below details into all fields except email field
          |first_name|last_name|telephone |password|
          |suhas     |j chandra|1234567890|12345   |
      And I entered existing accounts email into email filed
      And select the private policy
      And I click on continue button
      Then Proper warning message informing about duplicate account should be displayed
  @register
  Scenario: Register without providing any details
      Given I navigate to register page
      When I dont enter anything into the fields
      And I click on continue button
      Then Proper warning messages for every mandatory fields should be displayed