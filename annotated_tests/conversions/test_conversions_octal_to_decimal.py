import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.octal_to_decimal


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.octal_to_decimal.oct_to_decimal
    
    # region FUZZER
    
    def test_oct_to_decimal(self):
        """
        oct_string = '3'
        """
        actual = conversions.octal_to_decimal.oct_to_decimal("3")
        
        self.assertEqual(3, actual)
    
    def test_oct_to_decimal1(self):
        """
        oct_string = '-3 '
        """
        actual = conversions.octal_to_decimal.oct_to_decimal("-3 ")
        
        self.assertEqual(-3, actual)
    
    def test_oct_to_decimal_with_exception(self):
        """
        oct_string = 'py5tön'
        """
        # This test fails because function [conversions.octal_to_decimal.oct_to_decimal] produces [ValueError]
        conversions.octal_to_decimal.oct_to_decimal("py5tön")
    
    def test_oct_to_decimal_with_exception1(self):
        """
        oct_string = ''
        """
        # This test fails because function [conversions.octal_to_decimal.oct_to_decimal] produces [ValueError]
        conversions.octal_to_decimal.oct_to_decimal("")
    
    def test_oct_to_decimal_with_exception2(self):
        """
        oct_string = '-*'
        """
        # This test fails because function [conversions.octal_to_decimal.oct_to_decimal] produces [ValueError]
        conversions.octal_to_decimal.oct_to_decimal("-*")
    # endregion
    
    # endregion

