import sys
sys.path.append(r'..')
import builtins
import httpie
import unittest
import httpie.manager.cli


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.manager.cli.missing_subcommand

    # region FUZZER

    def test_missing_subcommand(self):
        actual = httpie.manager.cli.missing_subcommand()

        self.assertEqual("Please specify one of these: 'cli', 'plugins'", actual)

    def test_missing_subcommand_with_exception(self):
        """
        args = object()
        """
        args = object()
        # This test fails because function [httpie.manager.cli.missing_subcommand] produces [KeyError]
        httpie.manager.cli.missing_subcommand(args)

        args_modified = object.__new__(object)

        self.assertTrue(isinstance(args, builtins.object))
    # endregion

    # endregion

