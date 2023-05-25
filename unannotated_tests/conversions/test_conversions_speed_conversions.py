import sys
sys.path.append(r'../../..')
import builtins
import conversions
import unittest
import conversions.speed_conversions


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.speed_conversions.convert_speed
    
    # region FUZZER
    
    def test_convert_speed_with_exception(self):
        """
        speed = float('inf')
        unit_from = 'oo'
        unit_to = 'abcdefghijklmnopqrst'
        """
        # This test fails because function [conversions.speed_conversions.convert_speed] produces [ValueError]
        conversions.speed_conversions.convert_speed(float('inf'), "oo", "abcdefghijklmnopqrst")
    # endregion
    
    # endregion

