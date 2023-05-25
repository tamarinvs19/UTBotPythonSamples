import sys
sys.path.append(r'../../..')
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
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_oct_to_decimal_with_exception3(self):
        """
        oct_string = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.octal_to_decimal.oct_to_decimal(bytes(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_oct_to_decimal_with_exception4(self):
        """
        oct_string = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.octal_to_decimal.oct_to_decimal(bytes(33554441))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_oct_to_decimal_with_exception5(self):
        """
        oct_string = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.octal_to_decimal.oct_to_decimal(bytearray(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_oct_to_decimal_with_exception6(self):
        """
        oct_string = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.octal_to_decimal.oct_to_decimal(bytearray(33554441))
    # endregion
    
    # endregion

