from behave import *

use_step_matcher("re")


@given("a new latch object")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given a new latch object')


@when("the unlatch method is called")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the unlatch method is called')


@then("the latch phy is actuated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the latch phy is actuated')


@step("the unlatch method returns true")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the unlatch method returns true')


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