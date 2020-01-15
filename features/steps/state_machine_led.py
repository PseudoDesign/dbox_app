from behave import *
from dbox_app.phy import rgb_led


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


@step("the LED {blink_or_fade} is set to {frequency} Hz")
def step_impl(context, blink_or_fade, frequency):
    """
    :type context: behave.runner.Context
    """
    frequency = float(frequency)
    if blink_or_fade == "blink":
        kwargs = {}
    elif blink_or_fade == "fade":
        kwargs = {"fade": True}
    context.test_led.blink.assert_called_once_with(frequency, **kwargs)


@then("the LED is disabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_led.disable.assert_called_once()
