import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.binary_to_hexadecimal


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.binary_to_hexadecimal.bin_to_hexadecimal
    
    # region FUZZER
    
    def test_bin_to_hexadecimal(self):
        """
        binary_str = '-'
        """
        actual = conversions.binary_to_hexadecimal.bin_to_hexadecimal("-")
        
        self.assertEqual('-0x0', actual)
    
    def test_bin_to_hexadecimal_with_exception(self):
        """
        binary_str = ''
        """
        # This test fails because function [conversions.binary_to_hexadecimal.bin_to_hexadecimal] produces [ValueError]
        conversions.binary_to_hexadecimal.bin_to_hexadecimal("")
    
    def test_bin_to_hexadecimal_with_exception1(self):
        """
        binary_str = 'foco'
        """
        # This test fails because function [conversions.binary_to_hexadecimal.bin_to_hexadecimal] produces [ValueError]
        conversions.binary_to_hexadecimal.bin_to_hexadecimal("foco")
    # endregion
    
    # endregion

