import sys
sys.path.append(r'../..')
import types
import contextlib
import builtins
import httpie
import unittest
import httpie.plugins.manager


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.plugins.manager.enable_plugins

    # region FUZZER

    def test_enable_plugins(self):
        """
        plugins_dir = None
        """
        actual = httpie.plugins.manager.enable_plugins(None)

        expected = object.__new__(contextlib.nullcontext)
        expected.enter_result = None
        actual_enter_result = actual.enter_result
        expected_enter_result = expected.enter_result

        self.assertEqual(expected_enter_result, actual_enter_result)
    # endregion

    # endregion

