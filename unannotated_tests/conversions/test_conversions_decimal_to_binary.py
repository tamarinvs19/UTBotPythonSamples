import sys
sys.path.append(r'../../..')
import builtins
import conversions
import unittest
import conversions.decimal_to_binary


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.decimal_to_binary.decimal_to_binary
    
    # region FUZZER
    
    def test_decimal_to_binary(self):
        """
        num = -2097153 (mutated from -1)
        """
        actual = conversions.decimal_to_binary.decimal_to_binary(-2097153)
        
        self.assertEqual('-0b1000000000000000000001', actual)
    
    def test_decimal_to_binary1(self):
        """
        num = 170141183460469231731687303715882008575 (mutated from -2097153)
        """
        actual = conversions.decimal_to_binary.decimal_to_binary(170141183460469231731687303715882008575)
        
        self.assertEqual('0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110111111111111111111111', actual)
    
    def test_decimal_to_binary2(self):
        """
        num = zero (mutated from min)
        """
        actual = conversions.decimal_to_binary.decimal_to_binary(0)
        
        self.assertEqual('0b0', actual)
    # endregion
    
    # endregion

