import sys
sys.path.append(r'..')
import builtins
import httpie
import unittest
import httpie.context


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.context.__repr__

    # region FUZZER

    def test___repr__(self):
        """
        self = 'oo6'
        """
        actual = "oo6".__repr__()

        self.assertEqual('<str oo6>', actual)
    # endregion

    # endregion

