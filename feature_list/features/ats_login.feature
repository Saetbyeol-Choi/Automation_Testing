#Feature: ATS Register Account
#
#  Scenario Outline: Create Account - correct info
#    Given Launch chrome browser
#    When Open ATS homepage
#    Then Click ACCOUNT button
#    And Select Login
#    And Click on Continue button
#    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
#    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
#    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
#    And Check on policy
#    And Submit the registration form
#    Then Verify successful registration
##    Then Verify registration error message
#    And Close the browser
#
#    Examples:
#      | firstname | lastname | email                | address1            | city          | state      | zipcode | country       | loginname | password | pwdconfirm |
#      | saetbyeol | choi     | sbyeol0520@gmail.com | 50jones             | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |
##      | Mona      | Lisa     | tryout@gmail.com  | 2311 N Tracy Blvd A | Tracy         | California | 95376   | United States | monalisa1 | tech1  | tech1    |
#
#
#  Scenario Outline: Create Account - correct info
#    Given Launch chrome browser
#    When Open ATS homepage
#    Then Click ACCOUNT button
#    And Select Login
#    And Click on Continue button
#    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
#    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
#    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
#    And Check on policy
#    And Submit the registration form
##    Then Verify successful registration
#    Then Verify registration error message
#    And Close the browser
#
#    Examples:
#      | firstname | lastname | email                | address1            | city          | state      | zipcode | country       | loginname | password | pwdconfirm |
#      | saetbyeol | choi     | sbyeol0520@gmail.com | 50jones             | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |
##      | Mona      | Lisa     | tryout@gmail.com  | 2311 N Tracy Blvd A | Tracy         | California | 95376   | United States | monalisa1 | tech1  | tech1    |


Feature: ATS Register Account

  Background: Common steps
    Given Launch chrome browser
    When Open ATS homepage
    Then Click ACCOUNT button
    And Select Login
    And Click on Continue button

  Scenario Outline: Create Account - Successful Registration
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Check on policy
    And Submit the registration form
    Then Verify successful registration
    And Close the browser

    Examples:
      | firstname | lastname | email                | address1            | city          | state      | zipcode | country       | loginname | password | pwdconfirm |
      | saetbyeol | choi     | sbyeol0520@gmail.com | 50jones             | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |

  Scenario Outline: Create Account - Registration Error
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Check on policy
    And Submit the registration form
    Then Verify registration error message
    And Close the browser

    Examples:
      | firstname | lastname | email                | address1 | city          | state      | zipcode | country       | loginname | password | pwdconfirm |
      | saetbyeol | choi     | sbyeol0520@gmail.com | 50jones  | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |

  Scenario Outline: Create Account - Missing First Name
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Check on policy
    And Submit the registration form
    Then Verify missing first name error message
    And Close the browser

    Examples:
      | firstname | lastname | email                | address1 | city          | state      | zipcode | country       | loginname | password | pwdconfirm |
#      | ""        | choi     | sbyeol0520@gmail.com | 50jones  | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |
      |           | choi     | sbyeol0520@gmail.com | 50jones  | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |

  Scenario Outline: Create Account - Missing Last Name
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Check on policy
    And Submit the registration form
    Then Verify missing last name error message
    And Close the browser

    Examples:
      | firstname | lastname | email                | address1 | city          | state      | zipcode | country       | loginname | password | pwdconfirm |
      | saetbyeol |          | sbyeol0520@gmail.com | 50jones  | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |

  Scenario Outline: Create Account - Invalid Email
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Check on policy
    And Submit the registration form
    Then Verify invalid email error message
    And Close the browser

    Examples:
      | firstname | lastname | email | address1 | city          | state      | zipcode | country       | loginname | password | pwdconfirm |
      | saetbyeol | choi     |       | 50jones  | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |

  Scenario Outline: Create Account - Missing Address 1
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Check on policy
    And Submit the registration form
    Then Verify missing address 1 error message
    And Close the browser

    Examples:
      | firstname | lastname | email                | address1 | city          | state      | zipcode | country       | loginname | password | pwdconfirm |
      | saetbyeol | choi     | sbyeol0520@gmail.com |          | San Francisco | California | 94102   | United States | saetbyeol | asd123   | asd123     |

  Scenario Outline: Create Account - Missing City
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Check on policy
    And Submit the registration form
    Then Verify missing city error message
    And Close the browser

    Examples:
      | firstname | lastname | email                | address1 | city | state      | zipcode | country       | loginname | password | pwdconfirm |
      | saetbyeol | choi     | sbyeol0520@gmail.com | 50jones  |      | California | 94102   | United States | saetbyeol | asd123   | asd123     |

  Scenario Outline: Create Account - Missing State
    And Enter Personal Details "<firstname>", "<lastname>", "<email>"
    And Enter Address "<address1>", "<city>", "<state>", "<zipcode>", "<country>"
    And Enter Login Details "<loginname>", "<password>", "<pwdconfirm>"
    And Check on policy
    And Submit the registration form
    Then Verify missing state error message
    And Close the browser

    Examples:
      | firstname | lastname | email                | address1 | city          | state | zipcode | country       | loginname | password | pwdconfirm |
      | saetbyeol | choi     | sbyeol0520@gmail.com | 50jones  | San Francisco |       | 94102   | United States | saetbyeol | asd123   | asd123     |
