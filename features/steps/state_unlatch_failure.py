from behave import *
from unittest.mock import MagicMock
from dbox_app import state_machine


@step("the state machine is in the {machine_state} state")
def step_impl(context, machine_state):
    """
    :type context: behave.runner.Context
    """
    if not hasattr(context, "test_state_machine"):
        if not hasattr(context, "test_led"):
            context.test_led = MagicMock()
        if not hasattr(context, "test_button"):
            context.test_button = MagicMock()
        if not hasattr(context, "test_lock"):
            context.test_lock = MagicMock()
        if not hasattr(context, "test_bluetooth"):
            context.test_bluetooth = MagicMock()
        context.test_state_machine = state_machine.StateMachine(
            context.test_button,
            context.test_led,
            context.test_lock,
            context.test_bluetooth
        )
    context.test_state_machine.machine.set_state(machine_state)


@when("the button press and release event is triggered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_button.on_press_and_release()


@then("the state machine is in the {target_state} state")
def step_impl(context, target_state):
    """
    :type context: behave.runner.Context
    """
    assert context.test_state_machine.state == target_state


@when("the state machine enters the unlatch failure state")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the state machine enters the unlatch failure state')


@then("the LED color is set to red")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the LED color is set to red')


@step("the LED blink frequency is set to 2")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the LED blink frequency is set to 2')


@step("the LED fade is disabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the LED fade is disabled')


@step("the LED is enabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the LED is enabled')


@when("the state machine exits the unlatch failure state")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the state machine exits the unlatch failure state')


@then("the LED is disabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the LED is disabled')


@when("the state machine runs the unlatch failure state")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the state machine runs the unlatch failure state')


@step("the state machine (?P<waits>.+) for 3 seconds")
def step_impl(context, waits):
    """
    :type context: behave.runner.Context
    :type waits: str
    """
    raise NotImplementedError(u'STEP: And the state machine <waits> for 3 seconds')


@then("the state machine (?P<advances>.+) to the idle state")
def step_impl(context, advances):
    """
    :type context: behave.runner.Context
    :type advances: str
    """
    raise NotImplementedError(u'STEP: Then the state machine <advances> to the idle state')


@given("the state machine is in the unlatch failure state")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the state machine is in the unlatch failure state')


@then("the state machine remains in the unlatch failure state")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the state machine remains in the unlatch failure state')