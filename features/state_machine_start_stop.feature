Feature: State Machine start and stop

  Scenario Outline: Starting the system
    Given the state machine is in the <orig_state_name> state
    When the state machine start method is called
    Then the state machine is in the <new_state_name> state

    Examples:
    | orig_state_name | new_state_name  |
    | idle            | idle            |
    | unlatch_failure | unlatch_failure |
    | unlatch         | unlatch         |
    | exiting         | exiting         |
    | startup         | idle            |

  Scenario Outline: state transitions to exit
    Given the state machine is in the <orig_state_name> state
    When the state machine exit method is called
    Then the state machine is in the <new_state_name> state

    Examples:
    | orig_state_name | new_state_name |
    | idle            | exiting        |
    | unlatch_failure | exiting        |
    | unlatch         | exiting        |
    | exiting         | exiting        |