Feature: dbox state machine unlatch failure state

  Scenario: press and release when device is locked enters unlatch failure state
    Given the sample key file valid-0.yaml
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    Then the state machine is in the unlatch_failure state

  Scenario: entering unlatch failure state
    Given the sample key file valid-0.yaml
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    Then the LED color is set to red
    And the LED blink frequency is set to 4
    And the LED fade is disabled
    And the LED is enabled

  Scenario: exiting unlatch failure state
    Given the state machine is in the unlatch_failure state
    When the state machine runs the advance transition
    Then the LED is disabled

  Scenario Outline: unlatch failure advances to idle after 3-ish seconds
    Given the sample key file valid-0.yaml
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    And the state machine waits for <sec> seconds
    Then the state machine is in the <expected_state> state

    Examples:
    | sec           | expected_state          |
    | 3.25          | idle                    |
    | 2.75          | unlatch_failure         |

  Scenario Outline: other events don't interrupt unlatch failure state
    Given the state machine is in the unlatch_failure state
    When the <event_type> event is triggered
    Then the state machine is in the unlatch_failure state

    Examples:
    | event_type                |
    | button_press_and_release  |
    | button_hold               |
    | bluetooth_data            |