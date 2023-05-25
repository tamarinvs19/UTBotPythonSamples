import sys
sys.path.append(r'../..')
import builtins
import httpie.cookies
import types
import httpie
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable httpie.cookies._is_local_host

    # region FUZZER

    def test__is_local_host(self):
        """
        self = httpie.cookies.HTTPieCookiePolicy
        hostname = 'abcdefghijk6lmnopqrst'
        """
        h_t_t_pie_cookie_policy = httpie.cookies.HTTPieCookiePolicy()

        actual = h_t_t_pie_cookie_policy._is_local_host("abcdefghijk6lmnopqrst")

        self.assertEqual(False, actual)

        self.assertEqual(h_t_t_pie_cookie_policy, h_t_t_pie_cookie_policy)
    # endregion

    # endregion

