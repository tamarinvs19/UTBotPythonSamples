import sys
sys.path.append(r'../..')
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
    
    def test_length_conversion_with_exception1(self):
        """
        value = float('nan')
        from_type = 'M'
        to_type = 'foo'
        """
        value = float('nan')
        # This test fails because function [conversions.length_conversion.length_conversion] produces [ValueError]
        conversions.length_conversion.length_conversion(value, "M", "foo")
        
        self.assertEqual(float('nan'), value)
    # endregion
    
    # endregion

