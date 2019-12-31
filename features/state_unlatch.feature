Feature: dbox state machine unlatch state

  Scenario: press and release when device is locked enters unlatch failure state
    Given the sample key file does not exist
    And the state machine is in the idle state
    When the button_press_and_release event is triggered
    Then the state machine is in the unlatch state