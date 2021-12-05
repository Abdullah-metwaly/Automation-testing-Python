Feature: AutomationPractice contact us page test

  Background:
    Given The AutomationPractice site is open
    And The Contact us link is clicked

  Scenario Outline: Successfully contacting AutomationPracitce.
    Given The "<msg>" is written in Message field.
    And The Email is  "<parameter>"
    And Subject is "<subject>"
    And Attached file is "<attached>"
    When Send button is clicked
    Then The "<output>" message is shown.
    Examples:
      | parameter           | msg                 | attached    | subject          | output                                               |
      | customer@gmail.com  | Hi Customer Service | \file1.pdf  | Customer service | Your message has been successfully sent to our team. |
      | webmail@gmail.com   | Hi WebMaster        | \file2.pdf  | Webmaster        | Your message has been successfully sent to our team. |
      | customer@gmail.com  | Hi Customer Service | \file3.pdf  | Customer service | Your message has been successfully sent to our team. |
      | Webmaster@mail.com  | Hi WebMaster        | \file4.pdf  | Webmaster        | Your message has been successfully sent to our team. |

  Scenario Outline: Failed to contact AutomationPracitce.
    Given The "<msg>" is written in Message field.
    And The Email is  "<parameter>"
    And Subject is "<subject>"
    When Send button is clicked
    Then The "<output>" message is shown.
    Examples:
      | parameter         | msg      | subject          | output                                          |
      | invalid.email.com | Hi there!| customer         | Invalid email address.                          |