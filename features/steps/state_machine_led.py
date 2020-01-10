from behave import *
from dbox_app import rgb_led


@then("the LED color is set to {color}")
def step_impl(context, color):
    """
    :type context: behave.runner.Context
    """
    if color == "red":
        color = rgb_led.Color.RED
    elif color == "pink":
        color = rgb_led.Color.PINK
    elif color == "green":
        color = rgb_led.Color.GREEN
    else:
        raise NotImplementedError(f"Unsupported color {color}")
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
