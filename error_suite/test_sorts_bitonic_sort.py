import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import sorts
import unittest
import sorts.bitonic_sort


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable sorts.bitonic_sort.bitonic_sort
    
    # region FUZZER
    
    def test_bitonic_sort(self):
        """
        array = builtins.list[builtins.int]
        low = zero (mutated from positive)
        length = zero (mutated from min)
        direction = positive
        """
        actual = sorts.bitonic_sort.bitonic_sort([3, 0, -1, 170141183460469231731687303715884105727], 0, 0, 1)
        
        self.assertEqual(None, actual)
    
    def test_bitonic_sort1(self):
        """
        array = builtins.list[builtins.int]
        low = -1 (mutated from max)
        length = 3 (mutated from 2)
        direction = 3 (mutated from 2)
        """
        actual = sorts.bitonic_sort.bitonic_sort([-1, -170141183460469231731687303715884105728], -1, 3, 3)
        
        self.assertEqual(None, actual)
    
    def test_bitonic_sort_with_exception(self):
        """
        array = builtins.list[builtins.int]
        low = -1 (mutated from max)
        length = 67 (mutated from 3)
        direction = 3 (mutated from 2)
        """
        # This test fails because function [sorts.bitonic_sort.bitonic_sort] produces [IndexError]
        sorts.bitonic_sort.bitonic_sort([-1, -170141183460469231731687303715884105728], -1, 67, 3)
    # endregion
    
    # endregion

