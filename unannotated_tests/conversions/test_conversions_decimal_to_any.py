import sys
sys.path.append(r'../../..')
import builtins
import conversions
import unittest
import conversions.decimal_to_any


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.decimal_to_any.decimal_to_any
    
    # region FUZZER
    
    def test_decimal_to_any(self):
        """
        num = 10 (mutated from 11)
        base = 34 (mutated from 2)
        """
        actual = conversions.decimal_to_any.decimal_to_any(10, 34)
        
        self.assertEqual('A', actual)
    
    def test_decimal_to_any1(self):
        """
        num = 1032 (mutated from 8)
        base = -170141183460469231731687303715884105726 (mutated from 2)
        """
        actual = conversions.decimal_to_any.decimal_to_any(1032, -170141183460469231731687303715884105726)
        
        self.assertEqual('1-496401488517303786137132964064381141071-', actual)
    
    def test_decimal_to_any2(self):
        """
        num = 67108866 (mutated from 2)
        base = 34 (mutated from 2)
        """
        actual = conversions.decimal_to_any.decimal_to_any(67108866, 34)
        
        self.assertEqual('1G7EM6', actual)
    
    def test_decimal_to_any_with_exception(self):
        """
        num = -170141183460468929500232400058590429174 (mutated from 302231454903657293676554)
        base = 34 (mutated from 2)
        """
        # This test fails because function [conversions.decimal_to_any.decimal_to_any] produces [ValueError]
        conversions.decimal_to_any.decimal_to_any(-170141183460468929500232400058590429174, 34)
    
    def test_decimal_to_any_with_exception1(self):
        """
        num = 10 (mutated from 11)
        base = 162 (mutated from 34)
        """
        # This test fails because function [conversions.decimal_to_any.decimal_to_any] produces [ValueError]
        conversions.decimal_to_any.decimal_to_any(10, 162)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_decimal_to_any_with_exception2(self):
        """
        num = 170141183460469231731687303715884105215 (mutated from max)
        base = -1 (mutated from zero)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.decimal_to_any.decimal_to_any(170141183460469231731687303715884105215, -1)
    
    def test_decimal_to_any_with_exception3(self):
        """
        num = 10 (mutated from 11)
        base = zero (mutated from min)
        """
        # This test fails because function [conversions.decimal_to_any.decimal_to_any] produces [ValueError]
        conversions.decimal_to_any.decimal_to_any(10, True)
    # endregion
    
    # endregion

