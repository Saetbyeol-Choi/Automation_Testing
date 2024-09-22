Feature: ATS Login

  Scenario Outline: Login to ATS with Multiple parameters
    Given Launch chrome browser
    When Open ATS homepage
    Then Verify that the logo present on page
    And Hover on ACCOUNT button
    And Click on LOGIN button
    And Enter username "<username>" and password "<password>"
    And Click on Login button to login
    Then User must successfully see the MY ACCOUNT web page
    And close browser

    Examples:
      | username   | password  |
      | saetbyeol  | asd123    |
      | asd123     | saetbyeol |
      | saetbyeolc | asd123    |
      | saetbyeol  | asd123fg  |
