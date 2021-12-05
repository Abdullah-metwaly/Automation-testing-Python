Feature: AutomationPractice sign up page test

  Background:
    Given The AutomationPractice site is open
    And The Sign In link is clicked

  Scenario: Create a User using valid data
    Given email "134example_email1982@email.com"
    When account button is clicked
    And user wants to create a record with "Mr." as gender
    And user record has a first name of "Abdullah" same as address
    And user record has a last name of "Hussein" same as address
    And Password "12345"
    And Date of birth "4-12-1990"
    And Address is "Street Example 1"
    And City "Debrecen"
    And State "Washington"
    And zip code "11111"
    And Mobile num is "12345567"
    Then User must successfully create and account with "Abdullah  Hussein" as account 