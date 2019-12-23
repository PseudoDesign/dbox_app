import yaml
from binascii import crc32


class SecureLock:
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
            my_hash, crc = self._load_lock_file()
            # If the CRC is valid...
            if self._check_crc(my_hash, crc):
                return True
            else:
                return False
        except (IOError, yaml.YAMLError, KeyError, TypeError):
            return False

    @staticmethod
    def _check_crc(my_hash: b'', crc: int) -> bool:
        """
        Verify the CRC on the keyfile data
        :param my_hash:
        :param crc: crc32 of hash
        :return: true if the CRC is valid, else false
        """
        return crc == crc32(my_hash)

    def _load_lock_file(self) -> (b'', int):
        """
        Load the lock file; return the yaml-parsed data that's inside
        :return: hash, crc
        """
        with open(self.__lock_path, 'r') as fpt:
            data = yaml.safe_load(fpt)
        return data['hash'], data['crc']
