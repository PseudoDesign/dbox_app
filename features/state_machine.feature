Feature: dbox state machine

  Scenario: press and release when device is locked
    Given the SecureLock is locked
    And the state machine is in the idle state
    When the button is pressed and released
    Then the state machine advances to the unlatch failure state

  Scenario: entering unlatch failure state
    When the state machine enters the unlatch failure state
    Then the LED color is set to red
    And the LED blink frequency is set to 2
    And the LED fade is disabled
    And the LED is enabled

  Scenario: exiting unlatch failure state
    When the state machine exits the unlatch failure state
    Then the LED is disabled

  Scenario Outline: running unlatch failure state
    When the state machine runs the unlatch failure state
    And the state machine <waits> for 3 seconds
    Then the state machine <advances> to the idle state

    Examples:
    | waits         | advances          |
    | waits         | advances          |
    | does not wait | does not advance  |