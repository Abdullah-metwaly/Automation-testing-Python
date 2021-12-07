Feature: Tesint the search input main page

  Background:
    Given The AutomationPractice site is open

  Scenario Outline: Testing search field
    Given The search field is filled with "<parameter>"
    When The search button is clicked
    Then The "<msg>" search error message is shown
    Examples:
      | parameter               | msg                                                                                        |
      |  invalid searchdasdsdd  | No results were found for your search "invalid searchdasdsdd"                              |
      |                         | Please enter a search keyword                                                              |
      |  phkjhekjhj jdhkjh      | No results were found for your search "invalid searchdasdsdd"                              |

