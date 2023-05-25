import sys
sys.path.append(r'..')
import builtins
import httpie
import unittest
import httpie.output.ui.palette


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.ui.palette.boldify

    # region FUZZER

    def test_boldify(self):
        """
        color = 'oo6'
        """
        actual = httpie.output.ui.palette.boldify("oo6")

        self.assertEqual('bold oo6', actual)
    # endregion

    # endregion

