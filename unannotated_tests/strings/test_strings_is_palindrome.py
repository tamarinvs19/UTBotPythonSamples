import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.is_palindrome


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.is_palindrome.is_palindrome
    
    # region FUZZER
    
    def test_is_palindrome(self):
        """
        s = ''
        """
        actual = strings.is_palindrome.is_palindrome("")
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion

