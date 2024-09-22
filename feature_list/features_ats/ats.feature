Feature: ATS Login

  Scenario: Login to ATS home Page
    Given Launch chrome browser
    When Open ATS homepage
    Then Verify that the logo present on page
    And Hover on ACCOUNT button
    And Click on LOGIN button
#    And Enter username "saetbyeol" and password "asd123"
#    And Click on Login button to login
#    Then User must successfully see the MY ACCOUNT web page
