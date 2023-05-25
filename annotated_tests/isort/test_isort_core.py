import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.core


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.core._has_changed
    
    # region FUZZER
    
    def test__has_changed(self):
        """
        before = 'foo'
        after = 'abcdefghijklmnopqrst'
        line_separator = ''
        ignore_whitespace = zero
        """
        actual = isort.core._has_changed("foo", "abcdefghijklmnopqrst", "", False)
        
        self.assertEqual(True, actual)
    
    def test__has_changed1(self):
        """
        before = '€'
        after = 'abcdefghijklmnopqrst'
        line_separator = 'abcdefghijklmnopqrst'
        ignore_whitespace = min
        """
        actual = isort.core._has_changed("€", "abcdefghijklmnopqrst", "abcdefghijklmnopqrst", True)
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion

