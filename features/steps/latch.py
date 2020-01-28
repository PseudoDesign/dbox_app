from behave import *
from dbox_app.phy import Latch
from time import sleep
from datetime import datetime, timedelta
from gpiozero import Device
from gpiozero.pins.mock import MockFactory

Device.pin_factory = MockFactory()


@given("a {latch_state} latch object")
def step_impl(context, latch_state):
    """
    :type context: behave.runner.Context
    """
    if latch_state == "new":
        context.test_latch_pin = Device.pin_factory.pin(1)
        context.test_latch = Latch(1)
        sleep(.5)
    elif latch_state == "latched and released":
        context.test_latch_pin = Device.pin_factory.pin(1)
        context.test_latch = Latch(1)
        sleep(.5)
        context.test_latch.unlatch()
        context.test_latch.release()
    elif latch_state == "stale":
        context.test_latch_pin = Device.pin_factory.pin(1)
        context.test_latch = Latch(
            1,
            last_disabled=(datetime.now() - timedelta(minutes=60)))
        sleep(.5)
    else:
        raise NotImplementedError()


@when("the test latch {method} method is called")
def step_impl(context, method):
    """
    :type context: behave.runner.Context
    """
    if method == "release":
        context.unlatch_result = context.test_latch.release()
    elif method == "unlatch":
        context.unlatch_result = context.test_latch.unlatch()
    else:
        raise NotImplementedError()


@then("the unlatch method returns {bool_result}")
def step_impl(context, bool_result):
    """
    :type context: behave.runner.Context
    """
    if bool_result == "true":
        bool_result = True
    elif bool_result == "false":
        bool_result = False
    assert bool_result == context.unlatch_result


@when("and the unlatch method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_latch.unlatch()


@then("the latch pin is driven {value}")
def step_impl(context, value):
    """
    :type context: behave.runner.Context
    :type value: str
    """
    if value == "high":
        assert context.test_latch_pin.state == 1
    elif value == "low":
        assert context.test_latch_pin.state == 0
    else:
        raise NotImplementedError()
