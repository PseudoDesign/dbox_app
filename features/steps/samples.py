"""
Manages sample key files, matching the following statements:

Given the sample {subtype} file {filename}

The sample files should be placed at .../features/samples/{subtype}/{filename}
The file name is available at `context.sample_{subtype}_file`
"""

from behave import *
import os
from features.utils import TempUtils

STEPS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


@given("the sample {subtype} file {filename}")
def step_impl(context, subtype, filename):
    """
    sets the "context.sample_{subtype}_file" attribute to "{filename}"
    :param filename:
    :param subtype:
    :type context: behave.runner.Context
    """
    if filename == "does not exist" or filename == "None":
        setattr(context, "sample_{}_file".format(subtype), None)
    else:
        file = os.path.join(STEPS_DIRECTORY, "..", "samples", subtype, filename)
        tmp_file = TempUtils.copy_file_to_temp(file, target_subpath=os.path.join(context.feature.name, subtype))
        setattr(context, "sample_{}_file".format(subtype), tmp_file)
