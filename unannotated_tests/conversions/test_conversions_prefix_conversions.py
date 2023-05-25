import sys
sys.path.append(r'../../..')
import builtins
import conversions
import unittest
import conversions.prefix_conversions


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.prefix_conversions.convert_si_prefix
    
    # region FUZZER
    
    def test_convert_si_prefix_with_exception(self):
        """
        known_amount = float('inf')
        known_prefix = 'oo'
        unknown_prefix = 'abcdefghijklmnopqrst'
        """
        # This test fails because function [conversions.prefix_conversions.convert_si_prefix] produces [KeyError]
        conversions.prefix_conversions.convert_si_prefix(float('inf'), "oo", "abcdefghijklmnopqrst")
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.prefix_conversions.convert_binary_prefix
    
    # region FUZZER
    
    def test_convert_binary_prefix_with_exception(self):
        """
        known_amount = float('nan')
        known_prefix = 'oo'
        unknown_prefix = 'abcdefghijklmnopqrst'
        """
        known_amount = float('nan')
        # This test fails because function [conversions.prefix_conversions.convert_binary_prefix] produces [KeyError]
        conversions.prefix_conversions.convert_binary_prefix(known_amount, "oo", "abcdefghijklmnopqrst")
        
        self.assertEqual(float('nan'), known_amount)
    # endregion
    
    # endregion

