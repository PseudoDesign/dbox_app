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

    def lock(self, new_hash: b'', new_crc: int) -> bool:
        """
        Attempt to lock the device with the provided hash
        :param new_hash:
        :param new_crc:
        :return: True if the device is locked with the provided info, else false
        """
        is_locked, old_hash, old_crc = self._get_file_info()
        if is_locked:
            if old_hash == new_hash and old_crc == new_crc:
                return True
            else:
                return False
        if self._check_crc(new_hash, new_crc):
            self._save_lock_file(new_hash, new_crc)
            if self._is_file_valid:
                return True
            else:
                return False
        else:
            return False

    @property
    def _is_file_valid(self) -> bool:
        """
        Returns if the lock file at self.__lock_path exists and is valid, else false
        :return:
        """
        is_valid, my_hash, crc = self._get_file_info()
        return is_valid

    def _get_file_info(self) -> (bool, b'', int):
        """
        Returns information about the lock file
        :return: is_valid, hash, crc
        """
        try:
            my_hash, crc = self._load_lock_file()
            # If the CRC is valid...
            if self._check_crc(my_hash, crc):
                return True, my_hash, crc
            else:
                return False, None, None
        except (IOError, yaml.YAMLError, KeyError):
            return False, None, None

    @staticmethod
    def _check_crc(my_hash: b'', crc: int) -> bool:
        """
        Verify the CRC on the keyfile data
        :param my_hash:
        :param crc: crc32 of hash
        :return: true if the CRC is valid, else false
        """
        try:
            return crc == crc32(my_hash)
        except TypeError:
            return False

    def _load_lock_file(self) -> (b'', int):
        """
        Load the lock file; return the yaml-parsed data that's inside
        :return: hash, crc
        """
        with open(self.__lock_path, 'r') as fpt:
            data = yaml.safe_load(fpt)
        return data['hash'], data['crc']

    def _save_lock_file(self, my_hash: b'', crc: int):
        """
        save the provided data to a lock file
        :return:
        """
        with open(self.__lock_path, 'w') as fpt:
            yaml.safe_dump({"hash": my_hash, "crc": crc}, fpt)
