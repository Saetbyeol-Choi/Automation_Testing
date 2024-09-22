Feature: ATS Register Account

  Scenario Outline: Create Account
    Given Launch chrome browser
    When Open ATS homepage
    Then Click ACCOUNT button
    And Select Login
    And Click on Continue botton
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Submit the registration form
    Then Verify successful registration
    And Close the browser



    Examples:
      | firstname | lastname | email                | address1 | city | state      | zipcode | country       | loginname | password | pwdconfirm |
      | saetbyeol | choi     | sbyeol0520@gmail.com | 50jones  | sf   | California | 94102   | United States | saetbyeol | asd123   | asd123     |


    Scenario Outline: Your Personal Details Validation
    Given Launch chrome browser
    When Open ATS homepage
    Then Click ACCOUNT button
    And Select Login
    And Click on Continue button
    And Enter Personal Details "<firstname>", "<lastname>", "<invalid_email>"
    And Submit the registration form
    Then Verify email validation error
    And Close the browser

    Examples:
      | firstname | lastname | invalid_email |
      | John      | Doe      | invalidemail  |