import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.palindrome


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.palindrome.is_palindrome
    
    # region FUZZER
    
    def test_is_palindrome(self):
        """
        s = '€'
        """
        actual = strings.palindrome.is_palindrome("€")
        
        self.assertEqual(True, actual)
    
    def test_is_palindrome1(self):
        """
        s = 'abcdefBhijklmnopqrst'
        """
        actual = strings.palindrome.is_palindrome("abcdefBhijklmnopqrst")
        
        self.assertEqual(False, actual)
    
    def test_is_palindrome2(self):
        """
        s = 'oo'
        """
        actual = strings.palindrome.is_palindrome("oo")
        
        self.assertEqual(True, actual)
    
    def test_is_palindrome3(self):
        """
        s = 'o9«o'
        """
        actual = strings.palindrome.is_palindrome("o9«o")
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.palindrome.is_palindrome_recursive
    
    # region FUZZER
    
    def test_is_palindrome_recursive(self):
        """
        s = 'abcdefBhijklmnopqrst'
        """
        actual = strings.palindrome.is_palindrome_recursive("abcdefBhijklmnopqrst")
        
        self.assertEqual(False, actual)
    
    def test_is_palindrome_recursive1(self):
        """
        s = 'oo'
        """
        actual = strings.palindrome.is_palindrome_recursive("oo")
        
        self.assertEqual(True, actual)
    
    def test_is_palindrome_recursive2(self):
        """
        s = 'o9«o'
        """
        actual = strings.palindrome.is_palindrome_recursive("o9«o")
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.palindrome.is_palindrome_slice
    
    # region FUZZER
    
    def test_is_palindrome_slice(self):
        """
        s = '€'
        """
        actual = strings.palindrome.is_palindrome_slice("€")
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion

