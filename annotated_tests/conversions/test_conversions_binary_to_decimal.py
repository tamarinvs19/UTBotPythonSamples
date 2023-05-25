import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.binary_to_decimal


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.binary_to_decimal.bin_to_decimal
    
    # region FUZZER
    
    def test_bin_to_decimal(self):
        """
        bin_string = '01'
        """
        actual = conversions.binary_to_decimal.bin_to_decimal("01")
        
        self.assertEqual(1, actual)
    
    def test_bin_to_decimal1(self):
        """
        bin_string = '-'
        """
        actual = conversions.binary_to_decimal.bin_to_decimal("-")
        
        self.assertEqual(0, actual)
    
    def test_bin_to_decimal2(self):
        """
        bin_string = '-1'
        """
        actual = conversions.binary_to_decimal.bin_to_decimal("-1")
        
        self.assertEqual(-1, actual)
    
    def test_bin_to_decimal_with_exception(self):
        """
        bin_string = '￸1'
        """
        # This test fails because function [conversions.binary_to_decimal.bin_to_decimal] produces [ValueError]
        conversions.binary_to_decimal.bin_to_decimal("￸1")
    
    def test_bin_to_decimal_with_exception1(self):
        """
        bin_string = ''
        """
        # This test fails because function [conversions.binary_to_decimal.bin_to_decimal] produces [ValueError]
        conversions.binary_to_decimal.bin_to_decimal("")
    
    def test_bin_to_decimal_with_exception2(self):
        """
        bin_string = '-'
        """
        # This test fails because function [conversions.binary_to_decimal.bin_to_decimal] produces [ValueError]
        conversions.binary_to_decimal.bin_to_decimal("-")
    # endregion
    
    # endregion

