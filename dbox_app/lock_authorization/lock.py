class Lock:
    """
    Manages a secure key lock, where the lock is stored on the filesystem.
    """

    def __init__(self, lock_path):
        """
        :param lock_path: filesystem location of the lock file.
        """
        self.__lock_path = lock_path

    @property
    def is_locked(self):
        return self._is_file_valid

    @property
    def _is_file_valid(self):
        """
        Returns if the lock file at self.__lock_path exists and is valid, else false
        :return:
        """
        return False

