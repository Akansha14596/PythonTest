Feature: Testing the Hello text on a webpage

  Scenario: Check if the page contains "Hello" text 
    Given the user open "index.html" page
    Then the "Hello" text should be displayed on the page
    And close browser

    