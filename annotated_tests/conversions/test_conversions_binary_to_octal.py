import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.binary_to_octal


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.binary_to_octal.bin_to_octal
    
    # region FUZZER
    
    def test_bin_to_octal(self):
        """
        bin_string = '01'
        """
        actual = conversions.binary_to_octal.bin_to_octal("01")
        
        self.assertEqual('1', actual)
    
    def test_bin_to_octal1(self):
        """
        bin_string = '010'
        """
        actual = conversions.binary_to_octal.bin_to_octal("010")
        
        self.assertEqual('2', actual)
    
    def test_bin_to_octal_with_exception(self):
        """
        bin_string = ''
        """
        # This test fails because function [conversions.binary_to_octal.bin_to_octal] produces [ValueError]
        conversions.binary_to_octal.bin_to_octal("")
    
    def test_bin_to_octal_with_exception1(self):
        """
        bin_string = '+'
        """
        # This test fails because function [conversions.binary_to_octal.bin_to_octal] produces [ValueError]
        conversions.binary_to_octal.bin_to_octal("+")
    # endregion
    
    # endregion

