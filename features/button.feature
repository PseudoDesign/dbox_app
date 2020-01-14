Feature: button phy

  Scenario:
    Given the button is not pressed
    When the button is pressed and released
    Then the on_press_and_release method is called

  Scenario:
    Given the button is not pressed
    When the button is held for 3 seconds and released
    Then the on_hold method is called
    And the on_press_and_release method is not called

