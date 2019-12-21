from behave import *

use_step_matcher("re")


@given("the key file is valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the key file is valid')


@then("the device is locked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the device is locked')


@given("the key file is invalid due to (?P<reason>.+)")
def step_impl(context, reason):
    """
    :type context: behave.runner.Context
    :type reason: str
    """
    raise NotImplementedError(u'STEP: Given the key file is invalid due to <reason>')


@then("the device is unlocked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the device is unlocked')


@step("the provided locking key is valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the provided locking key is valid')


@when("the the device is locked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the the device is locked')


@then("the lock device method indicates a failure")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the lock device method indicates a failure')


@step("the key file is unchanged")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the key file is unchanged')


@then("the lock device method indicates a success")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the lock device method indicates a success')


@step("the key file contains the provided locking key")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the key file contains the provided locking key')


@given("device is unlocked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given device is unlocked')


@step("writing the key file fails due to (?P<reason>.+)")
def step_impl(context, reason):
    """
    :type context: behave.runner.Context
    :type reason: str
    """
    raise NotImplementedError(u'STEP: And writing the key file fails due to <reason>')


@step("the provided unlocking key is valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the provided unlocking key is valid')


@then("the key file is removed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the key file is removed')


@step("the unlock device method indicates a success")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the unlock device method indicates a success')


@given("the device key is invalid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the device key is invalid')


@step("erasing the key file fails")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And erasing the key file fails')


@step("the provided unlocking key is invalid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the provided unlocking key is invalid')


@then("the unlock device method indicates a failure")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the unlock device method indicates a failure')