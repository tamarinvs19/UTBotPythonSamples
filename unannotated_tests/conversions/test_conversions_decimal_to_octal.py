import sys
sys.path.append(r'../../..')
import builtins
import types
import conversions
import unittest
import conversions.decimal_to_octal


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.decimal_to_octal.decimal_to_octal
    
    # region FUZZER
    
    def test_decimal_to_octal(self):
        """
        num = 170141183460469231731687303715882008575 (mutated from max)
        """
        actual = conversions.decimal_to_octal.decimal_to_octal(170141183460469231731687303715882008575)
        
        self.assertEqual('0o2000000000000000089771425356151833571098631', actual)
    
    def test_decimal_to_octal1(self):
        """
        num = -2097153 (mutated from 170141183460469231731687303715882008575)
        """
        actual = conversions.decimal_to_octal.decimal_to_octal(-2097153)
        
        self.assertEqual('0o0', actual)
    
    def test_decimal_to_octal_with_exception(self):
        """
        num = float('inf')
        """
        # This test fails because function [conversions.decimal_to_octal.decimal_to_octal] produces [OverflowError]
        conversions.decimal_to_octal.decimal_to_octal(float('inf'))
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.decimal_to_octal.main
    
    # region FUZZER
    
    def test_main(self):
        actual = conversions.decimal_to_octal.main()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

