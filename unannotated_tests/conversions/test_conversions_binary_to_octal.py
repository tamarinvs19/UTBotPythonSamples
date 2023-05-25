import sys
sys.path.append(r'../../..')
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
        bin_string = builtins.list[builtins.str]
        """
        actual = conversions.binary_to_octal.bin_to_octal(["01", "01", "01"])
        
        self.assertEqual('7', actual)
    
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
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_bin_to_octal_with_exception2(self):
        """
        bin_string = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.binary_to_octal.bin_to_octal(bytes(268435460))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_bin_to_octal_with_exception3(self):
        """
        bin_string = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.binary_to_octal.bin_to_octal(bytearray(268435460))
    # endregion
    
    # endregion

