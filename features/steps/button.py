from behave import *

use_step_matcher("re")


@given("the button is not pressed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the button is not pressed')


@when("the button is pressed and released")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the button is pressed and released')


@then("the on_press_and_release method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the on_press_and_release method is called')


@when("the button is held for 3 seconds and released")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the button is held for 3 seconds and released')


@then("the on_hold method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the on_hold method is called')


@step("the on_press_and_release method is not called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the on_press_and_release method is not called')