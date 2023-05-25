import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.can_string_be_rearranged_as_palindrome


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.can_string_be_rearranged_as_palindrome.can_string_be_rearranged_as_palindrome_counter
    
    # region FUZZER
    
    def test_can_string_be_rearranged_as_palindrome_counter(self):
        actual = strings.can_string_be_rearranged_as_palindrome.can_string_be_rearranged_as_palindrome_counter()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.can_string_be_rearranged_as_palindrome.can_string_be_rearranged_as_palindrome
    
    # region FUZZER
    
    def test_can_string_be_rearranged_as_palindrome(self):
        actual = strings.can_string_be_rearranged_as_palindrome.can_string_be_rearranged_as_palindrome()
        
        self.assertEqual(True, actual)
    
    def test_can_string_be_rearranged_as_palindrome1(self):
        """
        input_str = 'fo'
        """
        actual = strings.can_string_be_rearranged_as_palindrome.can_string_be_rearranged_as_palindrome("fo")
        
        self.assertEqual(False, actual)
    
    def test_can_string_be_rearranged_as_palindrome2(self):
        """
        input_str = ' '
        """
        actual = strings.can_string_be_rearranged_as_palindrome.can_string_be_rearranged_as_palindrome(" ")
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion

