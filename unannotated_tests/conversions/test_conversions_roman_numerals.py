import sys
sys.path.append(r'../../..')
import builtins
import conversions
import unittest
import conversions.roman_numerals


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.roman_numerals.roman_to_int
    
    # region FUZZER
    
    def test_roman_to_int(self):
        """
        roman = 'D'
        """
        actual = conversions.roman_numerals.roman_to_int("D")
        
        self.assertEqual(500, actual)
    
    def test_roman_to_int1(self):
        """
        roman = ''
        """
        actual = conversions.roman_numerals.roman_to_int("")
        
        self.assertEqual(0, actual)
    
    def test_roman_to_int2(self):
        """
        roman = 'DXL'
        """
        actual = conversions.roman_numerals.roman_to_int("DXL")
        
        self.assertEqual(540, actual)
    
    def test_roman_to_int3(self):
        """
        roman = 'XL'
        """
        actual = conversions.roman_numerals.roman_to_int("XL")
        
        self.assertEqual(40, actual)
    
    def test_roman_to_int_with_exception(self):
        """
        roman = '+'
        """
        # This test fails because function [conversions.roman_numerals.roman_to_int] produces [KeyError]
        conversions.roman_numerals.roman_to_int("+")
    
    def test_roman_to_int_with_exception1(self):
        """
        roman = '￲+'
        """
        # This test fails because function [conversions.roman_numerals.roman_to_int] produces [KeyError]
        conversions.roman_numerals.roman_to_int("￲+")
    
    def test_roman_to_int_with_exception2(self):
        """
        roman = 'DXLn'
        """
        # This test fails because function [conversions.roman_numerals.roman_to_int] produces [KeyError]
        conversions.roman_numerals.roman_to_int("DXLn")
    
    def test_roman_to_int_with_exception3(self):
        """
        roman = 'XL7'
        """
        # This test fails because function [conversions.roman_numerals.roman_to_int] produces [KeyError]
        conversions.roman_numerals.roman_to_int("XL7")
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.roman_numerals.int_to_roman
    
    # region FUZZER
    
    def test_int_to_roman(self):
        """
        number = -2097153 (mutated from 170141183460469231731687303715882008575)
        """
        actual = conversions.roman_numerals.int_to_roman(-2097153)
        
        self.assertEqual('DCCCXLVII', actual)
    
    def test_int_to_roman_with_exception(self):
        """
        number = 170141183460469231731687303715882008575 (mutated from max)
        """
        # This test fails because function [conversions.roman_numerals.int_to_roman] produces [OverflowError]
        conversions.roman_numerals.int_to_roman(170141183460469231731687303715882008575)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_int_to_roman_with_exception1(self):
        """
        number = 34359738369 (mutated from positive)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.roman_numerals.int_to_roman(34359738369)
    # endregion
    
    # endregion

