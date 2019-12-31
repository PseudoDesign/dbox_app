from behave import *
from unittest.mock import MagicMock
from dbox_app import state_machine, rgb_led
from time import sleep


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


@then("the LED color is set to {color}")
def step_impl(context, color):
    """
    :type context: behave.runner.Context
    """
    if color == "red":
        color = rgb_led.Color.RED
    context.test_led.set_color.assert_called_once_with(color)


@step("the LED blink frequency is set to {frequency}")
def step_impl(context, frequency):
    """
    :type context: behave.runner.Context
    """
    frequency = int(frequency)
    context.test_led.set_blink_frequency.assert_called_once_with(frequency)


@step("the LED fade is {fade_state}")
def step_impl(context, fade_state):
    """
    :type context: behave.runner.Context
    """
    if fade_state == "enabled":
        fade_state = True
    elif fade_state == "disabled":
        fade_state = False
    context.test_led.set_fade.assert_called_once_with(fade_state)


@step("the LED is enabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_led.enable.assert_called_once()


@then("the LED is disabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_led.disable.assert_called_once()


@step("the state machine waits for {num_seconds} seconds")
def step_impl(context, num_seconds):
    """
    :type context: behave.runner.Context
    :type waits: str
    """
    num_seconds = float(num_seconds)
    sleep(num_seconds)