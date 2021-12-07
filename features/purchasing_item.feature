Feature: purchasing item with count
  Background:
    Given The AutomationPractice site is open

  Scenario Outline:
    Given The search input is filled with "<parameter>"
    And The button for search is clicked
    And The product item button is clicked
    And The plus button is clicked
    When The add to cart button is clicked
    Then The item count changes to "<number>"
    Examples:
      | parameter              | number |
      | Printed Summer Dress   |  3     | 
      | Printed Summer Dress   |  5     |
      | Printed Summer Dress   |  8     |
