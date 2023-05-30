import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.manacher


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.manacher.palindromic_string
    
    # region FUZZER
    
    def test_palindromic_string(self):
        """
        input_string = '|'
        """
        actual = strings.manacher.palindromic_string("|")
        
        self.assertEqual('', actual)
    
    def test_palindromic_string1(self):
        """
        input_string = '￲+'
        """
        actual = strings.manacher.palindromic_string("￲+")
        
        self.assertEqual('\ufff2', actual)
    
    def test_palindromic_string_with_exception(self):
        """
        input_string = ''
        """
        # This test fails because function [strings.manacher.palindromic_string] produces [IndexError]
        strings.manacher.palindromic_string("")
    # endregion
    
    # endregion

