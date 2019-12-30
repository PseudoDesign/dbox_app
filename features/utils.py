import os
import shutil
import string
import random


LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))
TEMP_DIRECTORY = os.path.join(LOCAL_DIR, "..", "..", ".tmp")
SCRIPTS_DIR = os.path.join(LOCAL_DIR, "..", "scripts")


def random_string(string_length=10):
    """Generate a random string of fixed length """



class TempUtils:
    """
        Manages temporary file storage needed by the unit tests.
    """
    @staticmethod
    def set_up():
        os.makedirs(TEMP_DIRECTORY, exist_ok=True)

    @staticmethod
    def tear_down():
        shutil.rmtree(TEMP_DIRECTORY)

    @staticmethod
    def copy_file_to_temp(path, target_subpath=""):
        """
        Copy the file at "path" to TEMP_DIRECTORY
        :param path:
        :param target_subpath: Add folders between TEMP_DIRECTORY and the copied file
        :return: the path of the new file
        """
        filename = os.path.basename(path)
        target_dir = os.path.join(TEMP_DIRECTORY, target_subpath)
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, filename)
        shutil.copy2(path, target_path)
        return target_path
