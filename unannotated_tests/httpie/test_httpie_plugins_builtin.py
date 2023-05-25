import sys
sys.path.append(r'..')
import builtins
import httpie.plugins.builtin
import typing
import httpie
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.plugins.builtin.get_auth

    # region FUZZER

    def test_get_auth(self):
        """
        self = httpie.plugins.builtin.BasicAuthPlugin
        username = 'foo'
        password = '€'
        """
        basic_auth_plugin = httpie.plugins.builtin.BasicAuthPlugin()

        actual = basic_auth_plugin.get_auth("foo", "€")

        expected = object.__new__(httpie.plugins.builtin.HTTPBasicAuth)
        expected.username = 'foo'
        expected.password = '€'

        self.assertEqual(expected, actual)

        self.assertEqual(basic_auth_plugin, basic_auth_plugin)
    # endregion

    # endregion

