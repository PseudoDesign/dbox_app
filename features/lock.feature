Feature: device software lock

  Scenario: locks when key is valid
    Given the key file is valid
    Then the device is locked

  Scenario Outline: unlocks when key is invalid (CRC error, etc)
    Given the key file is invalid due to <reason>
    Then the device is unlocked

    Examples:
      | reason            |
      | Invalid CRC       |
      | I/O Error         |
      | Length Invalid    |

  Scenario: locking cannot overwrite existing valid key
    Given the key file is valid
    And the provided locking key is valid
    When the the device is locked
    Then the lock device method indicates a failure
    And the key file is unchanged

  Scenario: locking saves valid key to key file when device is unlocked
    Given the device is unlocked
    And the provided locking key is valid
    When the device is locked
    Then the lock device method indicates a success
    And the key file contains the provided locking key

  Scenario Outline: lock enable fails when key file cannot be validated
    Given device is unlocked
    And the provided locking key is valid
    And writing the key file fails due to <reason>
    When the device is locked
    Then the lock device method indicates a failure

  Examples:
    | reason              |
    | Write I/O Error     |
    | Invalid Readback    |

  Scenario: unlocking with valid key when locked
    Given the device is locked
    And the provided unlocking key is valid
    When the device is unlocked
    Then the key file is removed
    And the unlock device method indicates a success

  Scenario: unlocking when key file is invalid
    Given the device key is invalid
    When the device is unlocked
    Then the key file is removed
    And the unlock device method indicates a success

  Scenario: unlocking when the key file cannot be removed
    Given the device is locked
    And the provided unlocking key is valid
    And erasing the key file fails
    When the device is unlocked
    Then the unlock device method indicates a success

  Scenario: unlocking with invalid key when locked
    Given the device is locked
    And the key file is valid
    And the provided unlocking key is invalid
    When the device is unlocked
    Then the unlock device method indicates a failure
    And the key file is unchanged
