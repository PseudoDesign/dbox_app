import yaml

class Lock:
    """
    Manages a secure key lock, where the lock is stored on the filesystem.
    """

    def __init__(self, lock_path: str):
        """
        :param lock_path: filesystem location of the lock file.
        """
        self.__lock_path = lock_path

    @property
    def is_locked(self) -> bool:
        """
        :return: True if the device is locked, else false
        """
        return self._is_file_valid

    @property
    def is_unlocked(self) -> bool:
        """
        :return: True if the device is unlocked, else false
        """
        return not self.is_locked

    @property
    def _is_file_valid(self) -> bool:
        """
        Returns if the lock file at self.__lock_path exists and is valid, else false
        :return:
        """
        try:
            lock_info = self._load_lock_file()
        except (IOError, yaml.YAMLError):
            return False
        return lock_info

    def _load_lock_file(self) -> {}:
        return {}
