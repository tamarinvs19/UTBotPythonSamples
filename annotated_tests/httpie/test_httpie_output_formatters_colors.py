import sys
sys.path.append(r'../..')
import builtins
import httpie
import unittest
import httpie.output.formatters.colors


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.formatters.colors.get_available_styles

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_available_styles_with_exception(self):
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.colors.get_available_styles()
    # endregion

    # endregion

    # region Test suites for executable httpie.output.formatters.colors.get_lexer

    # region FUZZER

    def test_get_lexer_with_exception(self):
        """
        mime = 'so:n'
        """
        # This test fails because function [httpie.output.formatters.colors.get_lexer] produces [ValueError]
        httpie.output.formatters.colors.get_lexer("so:n")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_lexer_with_exception1(self):
        """
        mime = '/1'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.colors.get_lexer("/1")

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_lexer_with_exception2(self):
        """
        mime = '/￵'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.formatters.colors.get_lexer("/￵")
    # endregion

    # endregion

