import sys
sys.path.append(r'..\..\..')
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
    
    def test_snake_to_camel_case_with_exception1(self):
        """
        input_str = object()
        """
        input_str = object()
        # This test fails because function [strings.snake_case_to_camel_pascal_case.snake_to_camel_case] produces [ValueError]
        strings.snake_case_to_camel_pascal_case.snake_to_camel_case(input_str)
        
        input_str_modified = object.__new__(object)
        
        self.assertTrue(isinstance(input_str, builtins.object))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_snake_to_camel_case_with_exception2(self):
        """
        input_str = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.snake_case_to_camel_pascal_case.snake_to_camel_case(bytes(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_snake_to_camel_case_with_exception3(self):
        """
        input_str = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.snake_case_to_camel_pascal_case.snake_to_camel_case(bytes(33554433))
    
    def test_snake_to_camel_case_with_exception4(self):
        """
        input_str = '_'
        use_pascal = zero (mutated from min)
        """
        # This test fails because function [strings.snake_case_to_camel_pascal_case.snake_to_camel_case] produces [IndexError]
        strings.snake_case_to_camel_pascal_case.snake_to_camel_case("_", False)
    # endregion
    
    # endregion

