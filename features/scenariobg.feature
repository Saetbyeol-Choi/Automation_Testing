Feature: ATS Login

  # executed before every scenario
  Background: common steps
    Given I launch browser
    When I open application
    Then Enter valid username and password
    And Click on login

  Scenario: Login to ATS with valid parameter
    Then User must login to the My Account page

  Scenario: Search user
    When navigate to search page
    Then search page should display

  Scenario: Advanced Search user
    When navigate to advanced search page
    Then advanced search page should display