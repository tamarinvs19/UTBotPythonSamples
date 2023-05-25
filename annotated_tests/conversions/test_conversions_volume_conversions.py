import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.volume_conversions


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.volume_conversions.volume_conversion
    
    # region FUZZER
    
    def test_volume_conversion_with_exception(self):
        """
        value = float('inf')
        from_type = ', '
        to_type = ', '
        """
        # This test fails because function [conversions.volume_conversions.volume_conversion] produces [ValueError]
        conversions.volume_conversions.volume_conversion(float('inf'), ", ", ", ")
    # endregion
    
    # endregion

