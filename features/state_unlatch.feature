Feature: dbox state machine unlatch state

  Scenario: press and release when device is locked enters unlatch failure state
    Given the sample key file does not exist
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    Then the state machine is in the unlatch state

  Scenario Outline: entering unlatch state
    Given the sample key file does not exist
    And the state machine is in the idle state
    And the latch actuation <is_successful> successful
    When the button_press_and_release event is triggered
    Then the LED color is set to <led_color>
    And the LED blink frequency is set to 2
    And the LED fade is enabled
    And the LED is enabled
    And the latch is <latch_call>

    Examples:
    | is_successful | led_color | latch_call  |
    | is            | green     | actuated    |
    | is not        | pink      | actuated    |

  Scenario: exiting unlatch state
    Given the state machine is in the unlatch state
    When the state machine runs the advance transition
    Then the LED is disabled
    And the latch is released

  Scenario Outline: unlatch advances to idle after 3-ish seconds
    Given the sample key file does not exist
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    And the system waits for <sec> seconds
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