import sys
sys.path.append(r'../..')
import builtins
import types
import pathlib
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

    # region Test suites for executable httpie.utils.get_expired_cookies

    # region FUZZER

    def test_get_expired_cookies(self):
        """
        cookies = '/'
        """
        actual = httpie.utils.get_expired_cookies("/")

        self.assertEqual([], actual)

    def test_get_expired_cookies1(self):
        """
        cookies = ''
        now = None
        """
        actual = httpie.utils.get_expired_cookies("", None)

        self.assertEqual([], actual)
    # endregion

    # endregion

    # region Test suites for executable httpie.utils.as_site

    # region FUZZER

    def test_as_site(self):
        """
        path = pathlib.Path
        """
        path = pathlib.Path()

        actual = httpie.utils.as_site(path)

        expected = pathlib.WindowsPath('Lib', 'site-packages')

        self.assertEqual(expected, actual)
    # endregion

    # endregion

