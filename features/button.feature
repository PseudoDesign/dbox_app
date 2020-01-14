Feature: button phy

  Scenario: press and release
    Given the button is not pressed
    When the pin is driven high
    And the system waits for .25 seconds
    And the pin is driven low
    Then the on_press_and_release method is called

  Scenario: press, hold, and release
    Given the button is not pressed
    When the pin is driven high
    And the system waits for 3.25 seconds
    And the pin is driven low
    Then the on_hold method is called
    And the on_press_and_release method is not called

  Scenario: press and hold
    Given the button is not pressed
    When the pin is driven high
    And the system waits for 3.25 seconds
    Then the on_hold method is called
    And the on_press_and_release method is not called
