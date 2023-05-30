import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.prefix_function


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.prefix_function.prefix_function
    
    # region FUZZER
    
    def test_prefix_function(self):
        """
        input_string = '€'
        """
        actual = strings.prefix_function.prefix_function("€")
        
        self.assertEqual([0], actual)
    
    def test_prefix_function1(self):
        """
        input_string = 'abcdefBhijklmnopqrst'
        """
        actual = strings.prefix_function.prefix_function("abcdefBhijklmnopqrst")
        
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], actual)
    
    def test_prefix_function2(self):
        """
        input_string = 'o«ow'
        """
        actual = strings.prefix_function.prefix_function("o«ow")
        
        self.assertEqual([0, 0, 1, 0], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.prefix_function.longest_prefix
    
    # region FUZZER
    
    def test_longest_prefix(self):
        """
        input_str = '€'
        """
        actual = strings.prefix_function.longest_prefix("€")
        
        self.assertEqual(0, actual)
    
    def test_longest_prefix_with_exception(self):
        """
        input_str = ''
        """
        # This test fails because function [strings.prefix_function.longest_prefix] produces [ValueError]
        strings.prefix_function.longest_prefix("")
    # endregion
    
    # endregion

