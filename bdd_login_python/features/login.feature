Feature: As a user,  i want to be able to log in and access the account page

  Scenario: Given a user, when i fill login form with valid credentials,
  i can access account page when i submit the form
    Given the login page is open
    When i fill "username" on Login page with value "Willy"
    And i fill "password" on Login page with value "password"
    And i click "submit" button on the login page
    Then the next page is "Account" page
    And the welcome text on Account page contains the value "Willy"

