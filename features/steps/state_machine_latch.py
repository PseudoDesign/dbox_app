from behave import *


@then("the latch is {state}")
def step_impl(context, state):
    """
    :type context: behave.runner.Context
    """
    if state == "unlatched":
        context.test_latch.unlatch.assert_called_once()
    elif state == "released":
        context.test_latch.release.assert_called_once()
    else:
        raise NotImplementedError(u'STEP: And the latch is actuated')


@given("the latch actuation {is_successful} successful")
def step_impl(context, is_successful):
    """
    :type context: behave.runner.Context
    :type is_successful: str
    """
    if is_successful == "is":
        context.test_latch.unlatch.return_value = True
    elif is_successful == "is not":
        context.test_latch.unlatch.return_value = False
    else:
        raise NotImplementedError(u'STEP: And the latch actuation <is_successful> successful')