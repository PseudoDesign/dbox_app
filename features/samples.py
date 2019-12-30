"""
Manages sample key files, matching the following statements:

Given the sample {subtype} file {filename}

The sample files should be placed at .../features/samples/{subtype}/{filename}
The file name is available at `context.sample_{subtype}_file`
"""

import os
from features.utils import TempUtils
from datetime import timedelta, datetime

STEPS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def load_file(context, subtype, filename, last_modified=timedelta(days=-7)):
    """
        sets the "context.sample_{subtype}_file" attribute to "{filename}"
        Sets the last modified timestamp of the file to last_modified
        :param filename:
        :param subtype:
        :type context: behave.runner.Context
        """
    if filename == "does not exist" or filename == "None":
        setattr(context, "sample_{}_file".format(subtype), None)
    else:
        file = os.path.join(STEPS_DIRECTORY, "samples", subtype, filename)
        tmp_file = TempUtils.copy_file_to_temp(file, target_subpath=os.path.join(context.feature.name, subtype))
        setattr(context, "sample_{}_file".format(subtype), tmp_file)
        setattr(context, "sample_{}_file_last_modified".format(subtype), os.path.getmtime(tmp_file))
