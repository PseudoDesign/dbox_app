from unittest import TestCase
from unittest.mock import patch, PropertyMock
from dbox_app.lock_authorization import Lock


class TestLock(TestCase):
    @patch.object(Lock, "_is_file_valid", new_callable=PropertyMock)
    def test_lock_is_locked_when_key_file_is_valid(self, mock_is_file_valid):
        mock_is_file_valid.return_value = True
        self.assertTrue(Lock("test_path").is_locked)

    @patch.object(Lock, "_is_file_valid", new_callable=PropertyMock)
    def test_lock_is_not_locked_when_key_file_is_not_valid(self, mock_is_file_valid):
        mock_is_file_valid.return_value = False
        self.assertFalse(Lock("test_path").is_locked)

    @patch.object(Lock, "_is_file_valid", new_callable=PropertyMock)
    def test_lock_is_unlocked_when_key_file_not_valid(self, mock_is_file_valid):
        mock_is_file_valid.return_value = False
        self.assertTrue(Lock("test_path").is_unlocked)

    @patch.object(Lock, "_is_file_valid", new_callable=PropertyMock)
    def test_lock_is_not_unlocked_when_key_file_is_not_valid(self, mock_is_file_valid):
        mock_is_file_valid.return_value = True
        self.assertFalse(Lock("test_path").is_unlocked)

