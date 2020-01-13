from behave import *
from dbox_app.phy import Latch
from unittest.mock import MagicMock
from datetime import datetime, timedelta


@given("a {latch_state} latch object")
def step_impl(context, latch_state):
    """
    :type context: behave.runner.Context
    """
    if latch_state == "new":
        context.latch_gpio = MagicMock()
        context.latch_object = Latch(context.latch_gpio)
    elif latch_state == "latched and released":
        context.latch_gpio = MagicMock()
        context.latch_object = Latch(context.latch_gpio)
        context.latch_object.unlatch()
        context.latch_object.release()
        context.latch_gpio.reset_mock()
    elif latch_state == "stale":
        context.latch_gpio = MagicMock()
        context.latch_object = Latch(
            context.latch_gpio,
            last_disabled=(datetime.now() - timedelta(minutes=60)))
    else:
        raise NotImplementedError()


@when("the unlatch method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.unlatch_result = context.latch_object.unlatch()


@then("the latch phy is actuated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.latch_gpio.on.assert_called_once()


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


@then("the latch phy {is_actuated} actuated")
def step_impl(context, is_actuated):
    """
    :type context: behave.runner.Context
    """
    if is_actuated == "is":
        is_actuated = True
    elif is_actuated == "is not":
        is_actuated = False
    assert is_actuated == context.latch_gpio.on.called


@then("the latch phy {is_released} released")
def step_impl(context, is_released):
    """
    :type context: behave.runner.Context
    :type is_released: str
    """
    if is_released == "is":
        is_released = True
    elif is_released == "is not":
        is_released = False
    assert is_released == context.latch_gpio.off.called


@when("and the unlatch method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.latch.unlatch()
