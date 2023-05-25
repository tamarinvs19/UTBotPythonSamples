import sys
sys.path.append(r'../../..')
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
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_bin_to_hexadecimal_with_exception2(self):
        """
        binary_str = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.binary_to_hexadecimal.bin_to_hexadecimal(bytearray(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_bin_to_hexadecimal_with_exception3(self):
        """
        binary_str = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.binary_to_hexadecimal.bin_to_hexadecimal(bytearray(33554433))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_bin_to_hexadecimal_with_exception4(self):
        """
        binary_str = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.binary_to_hexadecimal.bin_to_hexadecimal(bytes(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_bin_to_hexadecimal_with_exception5(self):
        """
        binary_str = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.binary_to_hexadecimal.bin_to_hexadecimal(bytes(33554433))
    # endregion
    
    # endregion

