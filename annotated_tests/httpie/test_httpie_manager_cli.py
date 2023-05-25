import sys
sys.path.append(r'../..')
import httpie
import unittest
import httpie.manager.cli


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.manager.cli.missing_subcommand

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_missing_subcommand_with_exception(self):
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.manager.cli.missing_subcommand()
    # endregion

    # endregion

