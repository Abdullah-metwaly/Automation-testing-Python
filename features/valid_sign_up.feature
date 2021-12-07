Feature: AutomationPractice sign up page test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario: Create a User using valid data
    Given email "<email>"
    When account button is clicked
    And user wants to create a record with "<gender>" as gender
    And user record has a first name of "<fname>" same as address
    And user record has a last name of "<lname>" same as address
    And Password "<passwd>"
    And Date of birth "<dob>"
    And Address is "<address>"
    And City "<city>"
    And State "<state>"
    And zip code "<zipcode>"
    And Mobile num is "<mobile>"
    Then User must successfully create and account with "<output>" as account 

 Examples: 
      | email              		  | gender | fname      | lname	   | output                                                                         | passwd | dob       | address            | city     | state     |zipcode | mobile  |
      | 134example_email1982@email.com    | Mrs.   | Abdullah   | Hussein  | User must successfully create and account with "Abdullah  Hussein" as account  | fghfh6 | 6-10-1973 | Example street 15  | Debrecen | Washington| 11111  | 5876657 |
      | 14example_email1982@email.com     | Mrs.   | Abdullah   | Hussein  | User must successfully create and account with "Abdullah  Hussein" as account  | fghfh6 | 6-10-1973 | Example street 14  | Szeged   | Washington| 12111  | 5876657 |
      | 13example_email1982@email.com     | Mrs.   | Abdullah   | Hussein  | User must successfully create and account with "Abdullah  Hussein" as account  | fghfh6 | 6-10-1973 | Example street 18  | Cairo    | Washington| 13111  | 5876657 |