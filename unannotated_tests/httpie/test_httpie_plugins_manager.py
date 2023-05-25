import sys
sys.path.append(r'..')
import builtins
import httpie
import unittest
import httpie.plugins.manager


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.plugins.manager.get_auth_plugins

    # region FUZZER

    def test_get_auth_plugins(self):
        """
        self = httpie.plugins.manager.PluginManager
        """
        plugin_manager = httpie.plugins.manager.PluginManager({})

        actual = plugin_manager.get_auth_plugins()

        self.assertEqual([], actual)
    # endregion

    # endregion

    # region Test suites for executable httpie.plugins.manager.get_auth_plugin_mapping

    # region FUZZER

    def test_get_auth_plugin_mapping(self):
        """
        self = httpie.plugins.manager.PluginManager
        """
        plugin_manager = httpie.plugins.manager.PluginManager({})

        actual = plugin_manager.get_auth_plugin_mapping()

        self.assertEqual({}, actual)
    # endregion

    # endregion

