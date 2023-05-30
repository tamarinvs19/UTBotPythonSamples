import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.snake_case_to_camel_pascal_case


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.snake_case_to_camel_pascal_case.snake_to_camel_case
    
    # region FUZZER
    
    def test_snake_to_camel_case(self):
        """
        input_str = 'py5tön'
        """
        actual = strings.snake_case_to_camel_pascal_case.snake_to_camel_case("py5tön")
        
        self.assertEqual('py5tön', actual)
    
    def test_snake_to_camel_case_with_exception(self):
        """
        input_str = 'K_'
        """
        # This test fails because function [strings.snake_case_to_camel_pascal_case.snake_to_camel_case] produces [IndexError]
        strings.snake_case_to_camel_pascal_case.snake_to_camel_case("K_")
    # endregion
    
    # endregion

