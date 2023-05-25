import sys
sys.path.append(r'../../..')
import builtins
import conversions
import unittest
import conversions.length_conversion


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.length_conversion.length_conversion
    
    # region FUZZER
    
    def test_length_conversion_with_exception(self):
        """
        value = float('inf')
        from_type = 's'
        to_type = 's'
        """
        # This test fails because function [conversions.length_conversion.length_conversion] produces [ValueError]
        conversions.length_conversion.length_conversion(float('inf'), "s", "s")
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_length_conversion_with_exception1(self):
        """
        value = builtins.bytes
        from_type = 'foo'
        to_type = 's'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.length_conversion.length_conversion(bytes(33554432), "foo", "s")
    
    def test_length_conversion_with_exception2(self):
        """
        value = builtins.bytes
        from_type = '€ₔ'
        to_type = 'pyth9n'
        """
        # This test fails because function [conversions.length_conversion.length_conversion] produces [ValueError]
        conversions.length_conversion.length_conversion(bytes(9), "€ₔ", "pyth9n")
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_length_conversion_with_exception3(self):
        """
        value = builtins.bytearray
        from_type = 'foo'
        to_type = 's'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.length_conversion.length_conversion(bytearray(33554432), "foo", "s")
    # endregion
    
    # endregion

