import sys
sys.path.append(r'..')
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

