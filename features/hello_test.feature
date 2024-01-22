Feature: Testing the Hello text on a webpage

    Scenario Outline: Using dynamic values
    Given the user open "index.html" page
    When I check if the HTML page contains the string "<string_value>"
    Then the result should be "<expected_result>"
    And close browser

    Examples: 
    | string_value | expected_result |
    | Hello 1 | Present |
    | Hello 2 | Present |
    | Hello 3 | Present |
    | DummyData | NotPresent |

    

    