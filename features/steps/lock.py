from behave import *
from features import utils
import os

use_step_matcher("re")


@given("the provided locking key is valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the provided locking key is valid')


@given("the device key is invalid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the device key is invalid')


@given("the device is locked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the device is locked')


@given("the device is unlocked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the device is locked')


@given("erasing the key file fails")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And erasing the key file fails')


@given("the provided unlocking key is invalid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the provided unlocking key is invalid')


@given("device is unlocked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given device is unlocked')


@given("writing the key file fails due to (?P<reason>.+)")
def step_impl(context, reason):
    """
    :type context: behave.runner.Context
    :type reason: str
    """
    if reason == "Write I/O Error":
        raise NotImplementedError(u'STEP: Given the key file is invalid due to <reason>')
    elif reason == "Invalid Readback":
        raise NotImplementedError(u'STEP: Given the key file is invalid due to <reason>')
    else:
        raise NotImplementedError(u'STEP: Given the key file is invalid due to <reason>')


@given("the provided unlocking key is valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the provided unlocking key is valid')


@when("the device is locked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the the device is locked')


@when("the device is unlocked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the device is unlocked')


@then("the key file is removed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the key file is removed')


@then("the unlock device method indicates a success")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the unlock device method indicates a success')


@then("the unlock device method indicates a failure")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the unlock device method indicates a failure')


@then("the device is locked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the device is locked')


@then("the device is unlocked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the device is unlocked')


@then("the lock device method indicates a failure")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the lock device method indicates a failure')


@then("the key file is unchanged")
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


@then("the key file contains the provided locking key")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the key file contains the provided locking key')
