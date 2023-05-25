import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.decimal_to_hexadecimal


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.decimal_to_hexadecimal.decimal_to_hexadecimal
    
    # region FUZZER
    
    def test_decimal_to_hexadecimal(self):
        """
        decimal = -16.0 (mutated from 16.0)
        """
        actual = conversions.decimal_to_hexadecimal.decimal_to_hexadecimal(-16.0)
        
        self.assertEqual('-0x10', actual)
    
    def test_decimal_to_hexadecimal1(self):
        """
        decimal = zero (mutated from -1.1125369292536007E-308)
        """
        actual = conversions.decimal_to_hexadecimal.decimal_to_hexadecimal(0.0)
        
        self.assertEqual('0x', actual)
    
    def test_decimal_to_hexadecimal_with_exception(self):
        """
        decimal = -1.1125369292536007E-308 (mutated from zero)
        """
        # This test fails because function [conversions.decimal_to_hexadecimal.decimal_to_hexadecimal] produces [AssertionError]
        conversions.decimal_to_hexadecimal.decimal_to_hexadecimal(-1.1125369292536007E-308)
    # endregion
    
    # endregion

