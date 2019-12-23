from unittest import TestCase
from unittest.mock import patch, PropertyMock
from dbox_app.lock_authorization import SecureLock
import yaml


class TestLock(TestCase):
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


