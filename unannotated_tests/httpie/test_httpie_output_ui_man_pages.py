import sys
sys.path.append(r'..')
import builtins
import httpie
import unittest
import httpie.output.ui.man_pages


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.output.ui.man_pages.is_available

    # region FUZZER

    def test_is_available(self):
        """
        program = 'nt'
        """
        actual = httpie.output.ui.man_pages.is_available("nt")

        self.assertEqual(False, actual)
    # endregion

    # endregion

