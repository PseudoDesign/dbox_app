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

    @patch.object(SecureLock, "_load_lock_file")
    def test_lock_is_unlocked_when_key_file_yaml_file_is_missing_required_parameters(self, mock_load_lock_file):
        mock_load_lock_file.side_effect = KeyError()
        self.assertTrue(SecureLock("test_path").is_unlocked)

    @patch.object(SecureLock, "_check_crc")
    def test_lock_is_unlocked_when_key_file_crc_is_invalid(self, mock_check_crc):
        mock_check_crc.return_value = False
        self.assertTrue(SecureLock("test_path").is_unlocked)

    @patch.object(SecureLock, "_check_crc")
    @patch.object(SecureLock, "_load_lock_file")
    def test_lock_is_locked_when_key_file_crc_is_valid(self, mock_lock_file, mock_check_crc):
        mock_check_crc.return_value = True
        mock_lock_file.return_value = b'', 1
        self.assertTrue(SecureLock("test_path").is_locked)

    @patch.object(SecureLock, "_check_crc")
    @patch.object(SecureLock, "_load_lock_file")
    def test_file_is_not_valid_when_crc_has_bad_type(self, mock_lock_file, mock_check_crc):
        mock_check_crc.side_effect = TypeError
        mock_lock_file.return_value = b'', 1
        self.assertFalse(SecureLock("test_path")._is_file_valid)

    @patch.object(SecureLock, "_check_crc")
    @patch.object(SecureLock, "_load_lock_file")
    def test_get_file_info_returns_none_for_hash_and_crc_when_file_is_invalid(self, mock_lock_file, mock_check_crc):
        mock_check_crc.side_effect = TypeError
        mock_lock_file.return_value = b'', 1
        is_valid, my_hash, crc = SecureLock("test_path")._get_file_info()
        self.assertFalse(is_valid)
        self.assertIsNone(my_hash)
        self.assertIsNone(crc)

# Submethod Testing

    def test_check_crc_returns_true_when_values_are_correct(self):
        self.assertTrue(SecureLock._check_crc(
            b'$2b$10$wRbzQ/sxYiu/k7Z0S0P4kukv/mFb/aWrK4lXjcyhgGfAW8TSB3vba',
            65473797
        ))

    def test_check_crc_returns_false_when_values_are_incorrect(self):
        self.assertFalse(SecureLock._check_crc(
            b'$2b$10$wRbzQ/sxYiu/k7Z0S0P4kukv/mFb/aWrK4lXjcyhgGfAW8TSB3vba',
            1
        ))
