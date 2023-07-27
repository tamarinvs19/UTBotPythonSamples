import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import sorts
import unittest
import sorts.recursive_bubble_sort


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable sorts.recursive_bubble_sort.bubble_sort
    
    # region FUZZER
    
    def test_bubble_sort(self):
        """
        list_data = builtins.list[typing.Any]
        """
        actual = sorts.recursive_bubble_sort.bubble_sort([])
        
        self.assertEqual([], actual)
    
    def test_bubble_sort1(self):
        """
        list_data = builtins.list[builtins.int]
        """
        actual = sorts.recursive_bubble_sort.bubble_sort([-170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 1, 170141183460469231731687303715884105727])
        
        self.assertEqual([-170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 1, 170141183460469231731687303715884105727], actual)
    
    def test_bubble_sort2(self):
        """
        list_data = builtins.list[builtins.int]
        """
        list_data = [170141183460469231731687303715884105727, 0, 2, 0, -170141183460469231731687303715884105728]
        
        actual = sorts.recursive_bubble_sort.bubble_sort(list_data)
        
        self.assertEqual([-170141183460469231731687303715884105728, 0, 0, 2, 170141183460469231731687303715884105727], actual)
    
    def test_bubble_sort_with_exception(self):
        """
        list_data = builtins.list[typing.Any]
        length = 134217729 (mutated from positive)
        """
        # This test fails because function [sorts.recursive_bubble_sort.bubble_sort] produces [IndexError]
        sorts.recursive_bubble_sort.bubble_sort([], 134217729)
    
    def test_bubble_sort_with_exception1(self):
        """
        list_data = builtins.list[builtins.int]
        length = 18 (mutated from 2)
        """
        list_data = [170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715615670271, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727]
        # This test fails because function [sorts.recursive_bubble_sort.bubble_sort] produces [IndexError]
        sorts.recursive_bubble_sort.bubble_sort(list_data, 18)
    # endregion
    
    # endregion

