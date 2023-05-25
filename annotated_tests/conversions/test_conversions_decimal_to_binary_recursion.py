import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.decimal_to_binary_recursion


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.decimal_to_binary_recursion.binary_recursive
    
    # region FUZZER
    
    def test_binary_recursive(self):
        """
        decimal = 170141183460469231731687303715882008575 (mutated from -2097153)
        """
        actual = conversions.decimal_to_binary_recursion.binary_recursive(170141183460469231731687303715882008575)
        
        self.assertEqual('1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110111111111111111111111', actual)
    
    def test_binary_recursive_with_exception(self):
        """
        decimal = -2097153 (mutated from -1)
        """
        # This test fails because function [conversions.decimal_to_binary_recursion.binary_recursive] produces [RecursionError]
        conversions.decimal_to_binary_recursion.binary_recursive(-2097153)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.decimal_to_binary_recursion.main
    
    # region FUZZER
    
    def test_main(self):
        """
        number = '6'
        """
        actual = conversions.decimal_to_binary_recursion.main("6")
        
        self.assertEqual('0b110', actual)
    
    def test_main_with_exception(self):
        """
        number = '€'
        """
        # This test fails because function [conversions.decimal_to_binary_recursion.main] produces [ValueError]
        conversions.decimal_to_binary_recursion.main("€")
    
    def test_main_with_exception1(self):
        """
        number = ''
        """
        # This test fails because function [conversions.decimal_to_binary_recursion.main] produces [ValueError]
        conversions.decimal_to_binary_recursion.main("")
    # endregion
    
    # endregion

