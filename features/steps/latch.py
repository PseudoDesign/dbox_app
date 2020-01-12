from behave import *
from dbox_app.phy import Latch
from unittest.mock import MagicMock


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
    raise NotImplementedError(u'STEP: Then the latch phy is actuated')


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


@given("a latched and released latch object")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given a latched and released latch object')


@then("the latch phy is no actuated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the latch phy is no actuated')


@step("the unlatch method returns false")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the unlatch method returns false')


@then("the latch phy (?P<is_released>.+) released")
def step_impl(context, is_released):
    """
    :type context: behave.runner.Context
    :type is_released: str
    """
    raise NotImplementedError(u'STEP: Then the latch phy <is_released> released')


@step("and the unlatch is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And and the unlatch is called')