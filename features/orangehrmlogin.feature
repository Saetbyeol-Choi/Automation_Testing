Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameter
    Given I launch chrome browser
    When I open orange HRM Homepage
    Then Enter username "saetbyeol" and password "asd123"
    And Click on login button
    Then User must successfully login to the My Account page

  Scenario Outline: Login to OrangeHRM with Multiple parameters
    Given I launch chrome browser
    When I open orange HRM Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the My Account page

    Examples:
      | username   | password  |
      | saetbyeol  | asd123    |
      | asd123     | saetbyeol |
      | saetbyeolc | asd123    |
      | saetbyeol  | asd123fg  |




