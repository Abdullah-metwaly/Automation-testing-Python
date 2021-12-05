Feature: purchasing product with extra options

  Background:
    Given The AutomationPractice site is open 

  Scenario Outline:
    Given The product name is "<parameter>" search button is clicked and the item is picked
    And modify the quantity "<number>"
    And choosing the size is "<size>"
    And Color filed is "<color>"
    When Add to cart button is clicked
    Then process the order
    Examples:
      |    parameter   | number | size | color |
      | Casual Dresses |  2     |  M   | White |
