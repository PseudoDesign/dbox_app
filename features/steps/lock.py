from behave import *
from features import utils
import os
from features import samples
from dbox_app import lock_authorization
import bcrypt
from binascii import crc32


@given("the sample key file {filename}")
def step_impl(context, filename):
    """
    :type context: behave.runner.Context
    """
    if filename == "does not exist":
        context.sample_key_file = os.path.join(utils.TEMP_DIRECTORY, "key", "sample_key_file.yaml")
    else:
        samples.load_file(context, "key", filename)
    if not hasattr(context, "test_lock"):
        context.test_lock = lock_authorization.SecureLock(context.sample_key_file)


@given("the provided locking key is valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    unlocking_key = utils.random_string(30)
    example_hash = bcrypt.hashpw(unlocking_key.encode("utf-8"), bcrypt.gensalt())
    context.locking_key = {
        "hash": example_hash,
        "crc": crc32(example_hash),
        "unlocking_key": unlocking_key
    }


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


@when("the state of the lock is queried")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.lock_state = context.test_lock.is_locked


@when("the device is locked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.test_lock_locking_result = context.test_lock.lock(
        context.locking_key['hash'],
        context.locking_key['crc'],
    )


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


@then("the device is {lock_state}")
def step_impl(context, lock_state):
    """
    :type context: behave.runner.Context
    """
    if lock_state == "locked":
        lock_state = True
    elif lock_state == "unlocked":
        lock_state = False
    assert context.lock_state is lock_state


@then("the lock device method indicates a failure")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.test_lock_locking_result is False


@then("the key file is unchanged")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Check if the last modified time matches what we started with
    assert os.path.getmtime(context.sample_key_file) == context.sample_key_file_last_modified


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
