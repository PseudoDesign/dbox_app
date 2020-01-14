Feature: Latch control

  Scenario: idle object succeeds when unlatched
    Given a stale latch object
    When the unlatch method is called
    Then the latch pin is driven high
    And the unlatch method returns true

  Scenario: new object is driven low
    Given a new latch object
    Then the latch pin is driven low

  Scenario: fails when immediately unlatched

    Given a new latch object
    When the unlatch method is called
    Then the latch pin is driven low
    And the unlatch method returns false

  Scenario Outline: unlatch fails when in keep-out time

    Given a latched and released latch object
    When the system waits for <time_seconds> seconds
    And the unlatch method is called
    Then the latch pin is driven low
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
    Then the latch pin is driven <value>

    Examples:
    | time_seconds | value         |
    | 2.75         | high          |
    | 3.25         | low           |

  Scenario Outline: multiple calls to unlatch don't reset timeout
    Given a stale latch object
    When the unlatch method is called
    And the system waits for <first_wait> seconds
    And the unlatch method is called
    And the system waits for <second_wait> seconds
    Then the latch pin is driven <value>

    Examples:
    | first_wait | second_wait | value        |
    | 1          | 1.75        | high         |
    | 1          | 2.25        | low          |
    | 2.5        | .25         | high         |
    | 2.75       | .5          | low          |


  Scenario: unlatch is successful after keep-out time

    Given a latched and released latch object
    When the system waits for 10.25 seconds
    And the unlatch method is called
    Then the latch pin is driven high
    And the unlatch method returns true

