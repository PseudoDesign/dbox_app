from features.utils import TempUtils
from time import sleep


def before_scenario(context, scenario):
    TempUtils.set_up()


def after_scenario(context, scenario):
    TempUtils.tear_down()
    if hasattr(context, "test_button"):
        context.test_button.close()
    if hasattr(context, "test_latch"):
        context.test_latch.close()
