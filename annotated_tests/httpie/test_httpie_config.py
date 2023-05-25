import sys
sys.path.append(r'../..')
import builtins
import pathlib
import httpie
import unittest
import httpie.config


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.config.get_default_config_dir

    # region FUZZER

    def test_get_default_config_dir(self):
        actual = httpie.config.get_default_config_dir()

        expected = pathlib.WindowsPath('C:\\', 'Users', 'tWX1238545', 'AppData', 'Roaming', 'httpie')

        self.assertEqual(expected, actual)
    # endregion

    # endregion

    # region Test suites for executable httpie.config.read_raw_config

    # region FUZZER

    def test_read_raw_config_with_exception(self):
        """
        config_type = '-foo'
        path = pathlib.Path
        """
        path = pathlib.Path()
        # This test fails because function [httpie.config.read_raw_config] produces [httpie.config.ConfigFileError]
        httpie.config.read_raw_config("-foo", path)
    # endregion

    # endregion

