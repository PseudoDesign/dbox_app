from behave import *
from features import utils
import os
from features import samples
from dbox_app import lock_authorization


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


@given("the sample unlocking key {filename}")
def step_impl(context, filename):
    """
        :type context: behave.runner.Context
        """
    if not hasattr(context, "unlocking_key"):
        file = os.path.join(samples.SAMPLES_DIRECTORY, "unlocking_key", filename)
        with open(file, 'r') as fpt:
            context.unlocking_key = fpt.readline()


@given("the provided locking key is valid")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.locking_key = lock_authorization.SecureLock.generate_keyset()


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
    context.test_lock_unlocking_result = context.test_lock.unlock(context.unlocking_key)


@then("the unlock device method indicates a {status}")
def step_impl(context, status):
    """
    :type context: behave.runner.Context
    """
    if status == "failure":
        status = False
    elif status == "success":
        status = True
    assert context.test_lock_unlocking_result is status


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


@then("the lock device method indicates a {status}")
def step_impl(context, status):
    """
    :type context: behave.runner.Context
    """
    if status == "failure":
        status = False
    elif status == "success":
        status = True
    assert context.test_lock_locking_result is status


@then("the key file is unchanged")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Check if the last modified time matches what we started with
    assert os.path.getmtime(context.sample_key_file) == context.sample_key_file_last_modified


@then("the key file contains the provided locking key")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    is_valid, my_hash, crc = context.test_lock.get_file_info()

    assert is_valid is True
    assert my_hash == context.locking_key["hash"]
    assert crc == context.locking_key["crc"]


@then("the key file is removed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert os.path.exists(context.sample_key_file) is False