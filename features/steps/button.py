from behave import *
from dbox_app.phy import Button
from gpiozero import Device
from gpiozero.pins.mock import MockFactory
from unittest.mock import MagicMock

Device.pin_factory = MockFactory()


@given("the button is not pressed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_button_phy = Device.pin_factory.pin(1)
    context.test_button_phy.drive_low()
    context.test_button = Button(1)
    context.test_button.on_press_and_release = MagicMock()
    context.test_button.on_hold = MagicMock()


@when("the pin is driven {direction}")
def step_impl(context, direction):
    """
    :type context: behave.runner.Context
    """
    if direction == "high":
        context.test_button_phy.drive_high()
    elif direction == "low":
        context.test_button_phy.drive_low()
    else:
        raise NotImplementedError(u'STEP: When the button is pressed and released')


@then("the on_press_and_release method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_button.on_press_and_release.assert_called()


@then("the on_hold method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_button.on_hold.assert_called()


@step("the on_press_and_release method is not called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_button.on_press_and_release.assert_not_called()
