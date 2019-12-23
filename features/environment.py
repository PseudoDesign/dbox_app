from features.utils import TempUtils


def before_scenario(context, scenario):
    TempUtils.set_up()


def after_scenario(context, scenario):
    TempUtils.tear_down()
