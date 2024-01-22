Feature: Testing the Hello text on a webpage

  Scenario: Check if the page contains following text 
    Given the user open "index.html" page
    And I have the following items in an array:
    """ 
    Hello 1,Hello 2,Hello 3,
    """
    Then the array should be displayed on the page
    And the "DummyData" should not be displayed on the page
    And close browser

    

    