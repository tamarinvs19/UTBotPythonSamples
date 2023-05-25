import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.is_isogram


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.is_isogram.is_isogram
    
    # region FUZZER
    
    def test_is_isogram(self):
        """
        string = ''
        """
        actual = strings.is_isogram.is_isogram("")
        
        self.assertEqual(True, actual)
    
    def test_is_isogram_with_exception(self):
        """
        string = 'String must onl contain alphabetic characters.'
        """
        # This test fails because function [strings.is_isogram.is_isogram] produces [ValueError]
        strings.is_isogram.is_isogram("String must onl contain alphabetic characters.")
    # endregion
    
    # endregion

