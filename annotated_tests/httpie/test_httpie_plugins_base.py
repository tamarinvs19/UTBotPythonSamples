import sys
sys.path.append(r'../..')
import types
import httpie.plugins.base
import builtins
import httpie
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.plugins.base.get_auth

    # region FUZZER

    def test_get_auth_with_exception(self):
        """
        self = httpie.plugins.base.AuthPlugin
        """
        auth_plugin = httpie.plugins.base.AuthPlugin()
        # This test fails because function [httpie.plugins.base.get_auth] produces [NotImplementedError]
        auth_plugin.get_auth(None, None)

        self.assertEqual(auth_plugin, auth_plugin)
    # endregion

    # endregion

    # region Test suites for executable httpie.plugins.base.get_adapter

    # region FUZZER

    def test_get_adapter_with_exception(self):
        """
        self = httpie.plugins.base.TransportPlugin
        """
        transport_plugin = httpie.plugins.base.TransportPlugin()
        # This test fails because function [httpie.plugins.base.get_adapter] produces [NotImplementedError]
        transport_plugin.get_adapter()

        self.assertEqual(transport_plugin, transport_plugin)
    # endregion

    # endregion

    # region Test suites for executable httpie.plugins.base.convert

    # region FUZZER

    def test_convert_with_exception(self):
        """
        self = httpie.plugins.base.ConverterPlugin
        body = builtins.bytes
        """
        converter_plugin = httpie.plugins.base.ConverterPlugin("pyythön")
        # This test fails because function [httpie.plugins.base.convert] produces [NotImplementedError]
        converter_plugin.convert(bytes(1))

        self.assertEqual(converter_plugin, converter_plugin)

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_convert_with_exception1(self):
        """
        self = httpie.plugins.base.ConverterPlugin
        body = builtins.bytes
        """
        converter_plugin = httpie.plugins.base.ConverterPlugin("ptöFnT")

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        converter_plugin.convert(bytes(8589934597))
    # endregion

    # endregion

