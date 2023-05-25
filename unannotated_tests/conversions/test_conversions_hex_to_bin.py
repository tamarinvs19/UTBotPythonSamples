import sys
sys.path.append(r'../../..')
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
        hex_num = '-'
        """
        # This test fails because function [conversions.hex_to_bin.hex_to_bin] produces [ValueError]
        conversions.hex_to_bin.hex_to_bin("-")
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_hex_to_bin_with_exception3(self):
        """
        hex_num = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.hex_to_bin.hex_to_bin(bytes(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_hex_to_bin_with_exception4(self):
        """
        hex_num = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.hex_to_bin.hex_to_bin(bytes(33554435))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_hex_to_bin_with_exception5(self):
        """
        hex_num = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.hex_to_bin.hex_to_bin(bytearray(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_hex_to_bin_with_exception6(self):
        """
        hex_num = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.hex_to_bin.hex_to_bin(bytearray(33554435))
    # endregion
    
    # endregion

