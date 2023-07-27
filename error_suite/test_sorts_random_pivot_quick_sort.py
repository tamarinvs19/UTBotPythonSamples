import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import sorts
import unittest
import sorts.random_pivot_quick_sort


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable sorts.random_pivot_quick_sort.quick_sort_random
    
    # region FUZZER
    
    def test_quick_sort_random(self):
        """
        a = builtins.list[typing.Any]
        left = 2 (mutated from positive)
        right = -170140858941915573304960520559863529472 (mutated from min)
        """
        actual = sorts.random_pivot_quick_sort.quick_sort_random([], 2, -170140858941915573304960520559863529472)
        
        self.assertEqual(None, actual)
    
    def test_quick_sort_random1(self):
        """
        a = builtins.list[builtins.int]
        left = positive
        right = 2 (mutated from -170141183460469231731687303715884105726)
        """
        actual = sorts.random_pivot_quick_sort.quick_sort_random([-1, 0, 0, -1], 1, 2)
        
        self.assertEqual(None, actual)
    
    def test_quick_sort_random_with_exception(self):
        """
        a = builtins.list[typing.Any]
        left = -170141183460469231731687303715884105727 (mutated from positive)
        right = max
        """
        # This test fails because function [sorts.random_pivot_quick_sort.quick_sort_random] produces [IndexError]
        sorts.random_pivot_quick_sort.quick_sort_random([], -170141183460469231731687303715884105727, 170141183460469231731687303715884105727)
    
    def test_quick_sort_random_with_exception1(self):
        """
        a = builtins.list[builtins.int]
        left = positive
        right = max
        """
        # This test fails because function [sorts.random_pivot_quick_sort.quick_sort_random] produces [IndexError]
        sorts.random_pivot_quick_sort.quick_sort_random([-170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 1, 170141183460469231731687303715884105727], 1, 170141183460469231731687303715884105727)
    
    def test_quick_sort_random_with_exception2(self):
        """
        a = builtins.list[builtins.int]
        left = -1
        right = 16 (mutated from zero)
        """
        # This test fails because function [sorts.random_pivot_quick_sort.quick_sort_random] produces [IndexError]
        sorts.random_pivot_quick_sort.quick_sort_random([-170141183460469231731687303715884105728], -1, 16)
    # endregion
    
    # endregion

