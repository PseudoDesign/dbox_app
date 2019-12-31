from behave import *


@step("the latch is {state}")
def step_impl(context, state):
    """
    :type context: behave.runner.Context
    """
    if state == "actuated":
        context.test_latch.actuate.assert_called_once()
    elif state == "released":
        context.test_latch.release.assert_called_once()
    else:
        raise NotImplementedError(u'STEP: And the latch is actuated')
