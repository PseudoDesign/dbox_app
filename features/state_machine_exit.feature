Feature: State Machine exit

  Scenario Outline: state transitions
    Given the state machine is in the <orig_state_name> state
    When the state machine exit method is called
    Then the state machine is in the <new_state_name> state

    Examples:
    | orig_state_name | new_state_name |
    | idle            | exiting        |
    | unlatch_failure | exiting        |
    | unlatch         | exiting        |
    | exiting         | exiting        |