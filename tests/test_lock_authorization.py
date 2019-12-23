from unittest import TestCase
from unittest.mock import patch, PropertyMock
from dbox_app.lock_authorization import SecureLock
import yaml


class TestLock(TestCase):

    EXAMPLE_HASH = b'$2b$10$wRbzQ/sxYiu/k7Z0S0P4kukv/mFb/aWrK4lXjcyhgGfAW8TSB3vba'
    EXAMPLE_VALID_CRC = 65473797
    EXAMPLE_VALID_UNLOCKING_KEY = '''qp3D3oS@"5u>&s;ctt"=5ilT~+{rFo'''

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

    @patch.object(SecureLock, "_get_file_info")
    def test_lock_method_fails_when_existing_file_is_valid_and_is_not_the_same_data(self, mock_get_file_info):
        mock_get_file_info.return_value = True, self.EXAMPLE_HASH, self.EXAMPLE_VALID_CRC
        lock = SecureLock("lock file")
        self.assertFalse(lock.lock(b'', 1))

    @patch.object(SecureLock, "_get_file_info")
    def test_lock_method_fails_when_existing_file_is_invalid_and_new_crc_is_invalid(self, mock_get_file_info):
        mock_get_file_info.return_value = False, None, None
        lock = SecureLock("lock file")
        self.assertFalse(lock.lock(self.EXAMPLE_HASH, 1))

    @patch.object(SecureLock, "_get_file_info")
    def test_lock_method_passes_when_existing_file_is_valid_and_data_matches(self, mock_get_file_info):
        mock_get_file_info.return_value = True, self.EXAMPLE_HASH, self.EXAMPLE_VALID_CRC
        lock = SecureLock("lock file")
        self.assertTrue(lock.lock(self.EXAMPLE_HASH, self.EXAMPLE_VALID_CRC))

    @patch.object(SecureLock, "_get_file_info")
    @patch.object(SecureLock, "_save_lock_file")
    def test_lock_method_does_not_call_save_lock_file_when_existing_file_is_valid(self, mock_save_lock_file,
                                                                                  mock_get_file_info):
        mock_get_file_info.return_value = True, self.EXAMPLE_HASH, self.EXAMPLE_VALID_CRC
        lock = SecureLock("lock file")
        lock.lock(b'', self.EXAMPLE_VALID_CRC)
        mock_save_lock_file.assert_not_called()

    @patch.object(SecureLock, "_get_file_info")
    @patch.object(SecureLock, "_save_lock_file")
    def test_lock_method_does_not_call_save_lock_file_when_new_crc_is_invalid(self, mock_save_lock_file,
                                                                                  mock_get_file_info):
        mock_get_file_info.return_value = False, None, None
        lock = SecureLock("lock file")
        lock.lock(self.EXAMPLE_HASH, 1)
        mock_save_lock_file.assert_not_called()

    @patch.object(SecureLock, "_get_file_info")
    @patch.object(SecureLock, "_save_lock_file")
    def test_lock_method_fails_when_readback_of_saved_data_fails(self, mock_save_lock_file,
                                                                              mock_get_file_info):
        mock_get_file_info.return_value = False, None, None
        lock = SecureLock("lock file")
        self.assertFalse(lock.lock(self.EXAMPLE_HASH, self.EXAMPLE_VALID_CRC))

    @patch.object(SecureLock, "_get_file_info")
    @patch.object(SecureLock, "_save_lock_file")
    def test_lock_method_fails_when_readback_of_saved_data_passes(self, mock_save_lock_file,
                                                                 mock_get_file_info):
        mock_get_file_info.side_effect = [(False, None, None), (True, self.EXAMPLE_HASH, self.EXAMPLE_VALID_CRC)]
        lock = SecureLock("lock file")
        self.assertTrue(lock.lock(self.EXAMPLE_HASH, self.EXAMPLE_VALID_CRC))

    # Submethod Testing

    @patch.object(SecureLock, "_check_crc")
    @patch.object(SecureLock, "_load_lock_file")
    def test_get_file_info_returns_none_for_hash_and_crc_when_file_is_invalid(self, mock_lock_file, mock_check_crc):
        mock_check_crc.return_value = False
        mock_lock_file.return_value = b'', 1
        is_valid, my_hash, crc = SecureLock("test_path")._get_file_info()
        self.assertFalse(is_valid)
        self.assertIsNone(my_hash)
        self.assertIsNone(crc)

    def test_check_crc_returns_true_when_values_are_correct(self):
        self.assertTrue(SecureLock._check_crc(
            self.EXAMPLE_HASH,
            self.EXAMPLE_VALID_CRC
        ))

    def test_check_crc_returns_false_when_values_are_incorrect(self):
        self.assertFalse(SecureLock._check_crc(
            self.EXAMPLE_HASH,
            1
        ))

    def test_check_crc_returns_false_when_types_are_incorrect(self):
        self.assertFalse(SecureLock._check_crc(
            self.EXAMPLE_HASH,
            None
        ))
