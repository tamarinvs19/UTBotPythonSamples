import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import strings
import unittest
import strings.snake_case_to_camel_pascal_case


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.snake_case_to_camel_pascal_case.snake_to_camel_case
    
    # region FUZZER
    
    def test_snake_to_camel_case(self):
        """
        input_str = '' (mutated from '')
        """
        actual = strings.snake_case_to_camel_pascal_case.snake_to_camel_case("")
        
        self.assertEqual('\x84', actual)
    
    def test_snake_to_camel_case_with_exception(self):
        """
        input_str = '_'
        """
        # This test fails because function [strings.snake_case_to_camel_pascal_case.snake_to_camel_case] produces [IndexError]
        strings.snake_case_to_camel_pascal_case.snake_to_camel_case("_")
    # endregion
    
    # endregion

