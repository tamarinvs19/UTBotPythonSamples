import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import sorts
import unittest
import sorts.counting_sort


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable sorts.counting_sort.counting_sort
    
    # region FUZZER
    
    def test_counting_sort(self):
        """
        collection = builtins.list[typing.Any]
        """
        actual = sorts.counting_sort.counting_sort([])
        
        self.assertEqual([], actual)
    
    def test_counting_sort1(self):
        """
        collection = builtins.list[builtins.int]
        """
        actual = sorts.counting_sort.counting_sort([170141183460469231731687303715884105727])
        
        self.assertEqual([170141183460469231731687303715884105727], actual)
    
    def test_counting_sort2(self):
        """
        collection = builtins.list[builtins.int]
        """
        actual = sorts.counting_sort.counting_sort([2, -1])
        
        self.assertEqual([-1, 2], actual)
    
    def test_counting_sort_with_exception(self):
        """
        collection = builtins.list[builtins.int]
        """
        # This test fails because function [sorts.counting_sort.counting_sort] produces [OverflowError]
        sorts.counting_sort.counting_sort([-1, -1, 1, 170141183460469231731687303715884105727])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_counting_sort_with_exception1(self):
        """
        collection = builtins.list[builtins.int]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        sorts.counting_sort.counting_sort([-170141183460469231731687303715749888000, -170141183460469231731687303715884105728])
    
    def test_counting_sort_with_exception2(self):
        """
        collection = ''
        """
        # This test fails because function [sorts.counting_sort.counting_sort] produces [ValueError]
        sorts.counting_sort.counting_sort("")
    # endregion
    
    # endregion

