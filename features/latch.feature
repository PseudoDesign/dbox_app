Feature: Latch control

  Scenario: idle object succeeds when unlatched
    Given a stale latch object
    When the unlatch method is called
    Then the latch phy is actuated
    And the unlatch method returns true

  Scenario: fails when immediately unlatched

    Given a new latch object
    When the unlatch method is called
    Then the latch phy is not actuated
    And the unlatch method returns false

  Scenario Outline: unlatch fails when in keep-out time

    Given a latched and released latch object
    When the system waits for <time_seconds> seconds
    And the unlatch method is called
    Then the latch phy is not actuated
    And the unlatch method returns false

    Examples:
    | time_seconds   |
    | 0.0            |
    | 1.0            |
    | 5.0            |
    | 9.0            |

  Scenario Outline: latch releases after timeout
    Given a stale latch object
    When the unlatch method is called
    And the system waits for <time_seconds> seconds
    Then the latch phy <is_released> released

    Examples:
    | time_seconds | is_released  |
    | 2.75         | is not       |
    | 3.25         | is           |


  Scenario: unlatch is successful after keep-out time

    Given a latched and released latch object
    When the system waits for 10.25 seconds
    And the unlatch method is called
    Then the latch phy is actuated
    And the unlatch method returns true

