import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.hex_to_bin


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.hex_to_bin.hex_to_bin
    
    # region FUZZER
    
    def test_hex_to_bin(self):
        """
        hex_num = 'B'
        """
        actual = conversions.hex_to_bin.hex_to_bin("B")
        
        self.assertEqual(1011, actual)
    
    def test_hex_to_bin1(self):
        """
        hex_num = '-8'
        """
        actual = conversions.hex_to_bin.hex_to_bin("-8")
        
        self.assertEqual(-1000, actual)
    
    def test_hex_to_bin_with_exception(self):
        """
        hex_num = ''
        """
        # This test fails because function [conversions.hex_to_bin.hex_to_bin] produces [ValueError]
        conversions.hex_to_bin.hex_to_bin("")
    
    def test_hex_to_bin_with_exception1(self):
        """
        hex_num = 'abcdefBhijklmnopqrst'
        """
        # This test fails because function [conversions.hex_to_bin.hex_to_bin] produces [ValueError]
        conversions.hex_to_bin.hex_to_bin("abcdefBhijklmnopqrst")
    
    def test_hex_to_bin_with_exception2(self):
        """
        hex_num = '-0'
        """
        # This test fails because function [conversions.hex_to_bin.hex_to_bin] produces [ValueError]
        conversions.hex_to_bin.hex_to_bin("-0")
    # endregion
    
    # endregion

