import sys
sys.path.append(r'..')
import builtins
import httpie
import unittest
import httpie.utils


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.utils.repr_dict

    # region FUZZER

    def test_repr_dict(self):
        """
        d = builtins.dict[typing.Any, typing.Any]
        """
        actual = httpie.utils.repr_dict({})

        self.assertEqual('{}', actual)
    # endregion

    # endregion

