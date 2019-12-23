from unittest import TestCase
from unittest.mock import patch, PropertyMock
from dbox_app.lock_authorization import SecureLock
import yaml


class TestLock(TestCase):

# Lock and Unlock testing
    @patch.object(SecureLock, "_is_file_valid", new_callable=PropertyMock)
    def test_lock_is_locked_when_key_file_is_valid(self, mock_is_file_valid):
        mock_is_file_valid.return_value = True
        self.assertTrue(SecureLock("test_path").is_locked)

    @patch.object(SecureLock, "_is_file_valid", new_callable=PropertyMock)
    def test_lock_is_not_locked_when_key_file_is_not_valid(self, mock_is_file_valid):
        mock_is_file_valid.return_value = False
        self.assertFalse(SecureLock("test_path").is_locked)

    @patch.object(SecureLock, "_is_file_valid", new_callable=PropertyMock)
    def test_lock_is_unlocked_when_key_file_not_valid(self, mock_is_file_valid):
        mock_is_file_valid.return_value = False
        self.assertTrue(SecureLock("test_path").is_unlocked)

    @patch.object(SecureLock, "_is_file_valid", new_callable=PropertyMock)
    def test_lock_is_not_unlocked_when_key_file_is_not_valid(self, mock_is_file_valid):
        mock_is_file_valid.return_value = True
        self.assertFalse(SecureLock("test_path").is_unlocked)

    @patch.object(SecureLock, "_load_lock_file")
    def test_lock_is_unlocked_when_key_file_cannot_be_opened(self, mock_load_lock_file):
        mock_load_lock_file.side_effect = IOError()
        self.assertTrue(SecureLock("test_path").is_unlocked)

    @patch.object(SecureLock, "_load_lock_file")
    def test_lock_is_unlocked_when_key_file_yaml_cannot_be_parsed(self, mock_load_lock_file):
        mock_load_lock_file.side_effect = yaml.YAMLError()
        self.assertTrue(SecureLock("test_path").is_unlocked)

    @patch.object(SecureLock, "_check_crc")
    def test_lock_is_unlocked_when_key_file_crc_is_invalid(self, mock_check_crc):
        mock_check_crc.return_value = False
        self.assertTrue(SecureLock("test_path").is_unlocked)

    @patch.object(SecureLock, "_check_crc")
    def test_lock_is_locked_when_key_file_crc_is_valid(self, mock_check_crc):
        mock_check_crc.return_value = True
        self.assertTrue(SecureLock("test_path").is_locked)

# Submethod Testing

    def test_check_crc_returns_false_when_missing_required_value(self):
        # CRC is missing
        keyfile_data = {
            'salt': "salt",
            'hash': "hash",
        }
        self.assertFalse(SecureLock._check_crc(keyfile_data))

    def test_check_crc_returns_false_when_required_value_is_none(self):
        # CRC is None
        keyfile_data = {
            'salt': b'$2b$10$wRbzQ/sxYiu/k7Z0S0P4ku',
            'hash': b'$2b$10$wRbzQ/sxYiu/k7Z0S0P4kukv/mFb/aWrK4lXjcyhgGfAW8TSB3vba',
            'crc': None,
        }
        self.assertFalse(SecureLock._check_crc(keyfile_data))

    def test_check_crc_returns_true_when_values_are_correct(self):
        # CRC is None
        keyfile_data = {
            'salt': b'$2b$10$wRbzQ/sxYiu/k7Z0S0P4ku',
            'hash': b'$2b$10$wRbzQ/sxYiu/k7Z0S0P4kukv/mFb/aWrK4lXjcyhgGfAW8TSB3vba',
            'crc': 3371285754,
        }
        self.assertTrue(SecureLock._check_crc(keyfile_data))
