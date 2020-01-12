Feature: Latch control

  Scenario: unlatch is successful out of reset

    Given a new latch object
    When the unlatch method is called
    Then the latch phy is actuated
    And the unlatch method returns true

  Scenario: unlatch fails when in keep-out time

    Given a new latch object
    When the unlatch method is called
    And

  Scenario: latch releases after timeout

  Scenario: unlatch is successful after keep-out time