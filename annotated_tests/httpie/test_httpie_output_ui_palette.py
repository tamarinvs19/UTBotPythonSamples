import sys
sys.path.append(r'../..')
import httpie.output.ui.palette
import builtins
import httpie
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.ui.palette.boldify

    # region FUZZER

    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_boldify_with_exception(self):
        """
        color = httpie.output.ui.palette.PieColor
        """
        color = httpie.output.ui.palette.PieColor(bytes(67108864))
        color.PRIMARY = "€"
        color.PURPLE = "foo"
        color.PINK = "€"
        color.BLUE = "foo"
        color.GREY = "foo"
        color.SECONDARY = "pythön"
        color.ORANGE = "foo"
        color.AQUA = "€"

        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        httpie.output.ui.palette.boldify(color)
    # endregion

    # endregion

