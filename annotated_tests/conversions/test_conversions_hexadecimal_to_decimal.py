import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.hexadecimal_to_decimal


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.hexadecimal_to_decimal.hex_to_decimal
    
    # region FUZZER
    
    def test_hex_to_decimal(self):
        """
        hex_string = '-'
        """
        actual = conversions.hexadecimal_to_decimal.hex_to_decimal("-")
        
        self.assertEqual(0, actual)
    
    def test_hex_to_decimal1(self):
        """
        hex_string = 'D'
        """
        actual = conversions.hexadecimal_to_decimal.hex_to_decimal("D")
        
        self.assertEqual(13, actual)
    
    def test_hex_to_decimal2(self):
        """
        hex_string = '-2'
        """
        actual = conversions.hexadecimal_to_decimal.hex_to_decimal("-2")
        
        self.assertEqual(-2, actual)
    
    def test_hex_to_decimal_with_exception(self):
        """
        hex_string = 'py5tön'
        """
        # This test fails because function [conversions.hexadecimal_to_decimal.hex_to_decimal] produces [ValueError]
        conversions.hexadecimal_to_decimal.hex_to_decimal("py5tön")
    
    def test_hex_to_decimal_with_exception1(self):
        """
        hex_string = ''
        """
        # This test fails because function [conversions.hexadecimal_to_decimal.hex_to_decimal] produces [ValueError]
        conversions.hexadecimal_to_decimal.hex_to_decimal("")
    
    def test_hex_to_decimal_with_exception2(self):
        """
        hex_string = '-*'
        """
        # This test fails because function [conversions.hexadecimal_to_decimal.hex_to_decimal] produces [ValueError]
        conversions.hexadecimal_to_decimal.hex_to_decimal("-*")
    # endregion
    
    # endregion

