import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.pressure_conversions


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.pressure_conversions.pressure_conversion
    
    # region FUZZER
    
    def test_pressure_conversion_with_exception(self):
        """
        value = float('inf')
        from_type = ', '
        to_type = ', '
        """
        # This test fails because function [conversions.pressure_conversions.pressure_conversion] produces [ValueError]
        conversions.pressure_conversions.pressure_conversion(float('inf'), ", ", ", ")
    # endregion
    
    # endregion

