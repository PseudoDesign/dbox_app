Feature: dbox state machine unlatch state

  Scenario: press and release when device is locked enters unlatch failure state
    Given the sample key file does not exist
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    Then the state machine is in the unlatch state

  Scenario: entering unlatch state
    Given the sample key file does not exist
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    Then the LED color is set to pink
    And the LED blink frequency is set to 2
    And the LED fade is enabled
    And the LED is enabled
    And the latch is actuated

  Scenario: exiting unlatch state
    Given the state machine is in the unlatch state
    When the state machine runs the advance transition
    Then the LED is disabled
    And the latch is released

  Scenario Outline: unlatch advances to idle after 3-ish seconds
    Given the sample key file does not exist
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    And the state machine waits for <sec> seconds
    Then the state machine is in the <expected_state> state

    Examples:
    | sec           | expected_state          |
    | 3.25          | idle                    |
    | 2.75          | unlatch                 |

  Scenario Outline: other events don't interrupt unlatch state
    Given the state machine is in the unlatch state
    When the <event_type> event is triggered
    Then the state machine is in the unlatch state

    Examples:
    | event_type                |
    | button_press_and_release  |
    | button_hold               |
    | bluetooth_data            |