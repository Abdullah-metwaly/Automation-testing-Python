Feature: AutomationPractice sign up page test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario Outline: Create a User with missing data
   Given Enter email "<email>"
    When Create an account button is clicked
    And Chosen filed is "<gender>" as gender
    And first name of the user is "<fname>" 
    And last name of the user is "<lname>"
    And Password is "<passwd>"
    And Date of Birth is "<dob>"
    And the Address is "<address>"
    And the city is "<city>"
    And the state is "<state>"
    And zip code is "<zipcode>"	
    And Country is set to default which is United States
    And Mobile Phone is "<mobile>"
    And Address ref. is default: My Address
    Then The "<output>" is shown.
    Examples:
      | email              | gender | fname | lname | output                                                                            | passwd | dob       | address            | city     | state   |zipcode | mobile  |
      | 123kdd@email.com   | Mrs.   | koo   | kdd   | The Zip/Postal code you've entered is invalid. It must follow this format: 00000  | fghfh6 | 6-10-1973 | Example street 15  | Debrecen | Arizona |        | 5876657 |
      | 123kdd@email.com   | Mrs.   | koo   | kdd   | city is required.                                                                 | fghfh6 | 6-11-1974 | Example street 15  |          | Arizona | 01234  | 5876657 |
      | 123kdd@email.com   | Mrs.   |       | kdd   | firstname is required.                                                            | fghfh6 | 6-12-1975 | Example street 15  | szeged   | Arizona | 01234  | 5876657 |
      | 123kdd@email.com   | Mrs.   | koo   |       | lastname is required.                                                             | fghfh6 | 6-10-1976 | Example street 15  | szeged   | Arizona | 01234  | 5876657 |
      | 123kdd@email.com   | Mrs.   | koo   | kdd   | passwd is required.                                                               |        | 6-10-1976 | Example street 15  | szeged   | Arizona | 01234  | 5876657 |