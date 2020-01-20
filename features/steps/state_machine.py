from behave import *
from unittest.mock import MagicMock
from time import sleep
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
        if not hasattr(context, "test_latch"):
            context.test_latch = MagicMock()
        context.test_state_machine = state_machine.StateMachine(
            context.test_button,
            context.test_led,
            context.test_lock,
            context.test_bluetooth,
            context.test_latch
        )
    context.test_state_machine.machine.set_state(machine_state)


@when("the {event_type} event is triggered")
def step_impl(context, event_type):
    """
    :type context: behave.runner.Context
    """
    if event_type == "button_press_and_release":
        context.test_button.on_press_and_release()
    elif event_type == "button_hold":
        context.test_button.on_hold()
    elif event_type == "bluetooth_data":
        context.test_bluetooth.on_data()
    else:
        raise NotImplementedError(f"unsupported event type {event_type}")


@then("the state machine is in the {target_state} state")
def step_impl(context, target_state):
    """
    :type context: behave.runner.Context
    """
    assert context.test_state_machine.state == target_state


@when("the state machine runs the {transition} transition")
def step_impl(context, transition):
    """
    :type context: behave.runner.Context
    """
    getattr(context.test_state_machine, transition)()


@step("the system waits for {num_seconds} seconds")
def step_impl(context, num_seconds):
    """
    :type context: behave.runner.Context
    :type waits: str
    """
    num_seconds = float(num_seconds)
    sleep(num_seconds)


@when("the state machine exit method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_state_machine.exit()
