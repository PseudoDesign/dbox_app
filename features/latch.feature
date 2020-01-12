Feature: Latch control

  Scenario: unlatch is successful out of reset

    Given a new latch object
    When the unlatch method is called
    Then the latch phy is actuated
    And the unlatch method returns true

  Scenario Outline: unlatch fails when in keep-out time

    Given a latched and released latch object
    When the system waits for <time_seconds> seconds
    And the unlatch method is called
    Then the latch phy is no actuated
    And the unlatch method returns false

    Examples:
    | time_seconds |
    | 0            |
    | 1            |
    | 5            |
    | 9            |

  Scenario Outline: latch releases after timeout
    Given a new latch object
    When the unlatch method is called
    And the system waits for <time_seconds> seconds
    Then the latch phy <is_released> released

    Examples:
    | time_seconds | is_released  |
    | 2.75         | is not       |
    | 3.25         | is           |


  Scenario: unlatch is successful after keep-out time

    Given a latched and released latch object
    When the system waits for <time_seconds> seconds
    And and the unlatch is called
    Then the latch phy is actuated
    And the unlatch method returns true

