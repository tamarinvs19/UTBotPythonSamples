import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.weight_conversion


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.weight_conversion.weight_conversion
    
    # region FUZZER
    
    def test_weight_conversion_with_exception(self):
        """
        from_type = '€'
        to_type = 'oo'
        value = float('-inf')
        """
        # This test fails because function [conversions.weight_conversion.weight_conversion] produces [ValueError]
        conversions.weight_conversion.weight_conversion("€", "oo", float('-inf'))
    # endregion
    
    # endregion

