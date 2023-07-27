import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import strings
import unittest
import strings.prefix_function


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.prefix_function.prefix_function
    
    # region FUZZER
    
    def test_prefix_function(self):
        """
        input_string = 'pfoo' (mutated from 'foo')
        """
        actual = strings.prefix_function.prefix_function("pfoo")
        
        self.assertEqual([0, 0, 0, 0], actual)
    
    def test_prefix_function1(self):
        """
        input_string = 'oopf'
        """
        actual = strings.prefix_function.prefix_function("oopf")
        
        self.assertEqual([0, 1, 0, 0], actual)
    
    def test_prefix_function2(self):
        """
        input_string = ''
        """
        actual = strings.prefix_function.prefix_function("")
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.prefix_function.longest_prefix
    
    # region FUZZER
    
    def test_longest_prefix(self):
        """
        input_str = 'pfoo' (mutated from 'foo')
        """
        actual = strings.prefix_function.longest_prefix("pfoo")
        
        self.assertEqual(0, actual)
    
    def test_longest_prefix_with_exception(self):
        """
        input_str = ''
        """
        # This test fails because function [strings.prefix_function.longest_prefix] produces [ValueError]
        strings.prefix_function.longest_prefix("")
    # endregion
    
    # endregion

