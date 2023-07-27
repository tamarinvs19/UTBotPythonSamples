import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import sorts
import unittest
import sorts.pigeon_sort


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable sorts.pigeon_sort.pigeon_sort
    
    # region FUZZER
    
    def test_pigeon_sort(self):
        """
        array = builtins.list[builtins.int]
        """
        actual = sorts.pigeon_sort.pigeon_sort([170141183460469231731687303715884105727])
        
        self.assertEqual([170141183460469231731687303715884105727], actual)
    
    def test_pigeon_sort1(self):
        """
        array = builtins.list[builtins.int]
        """
        actual = sorts.pigeon_sort.pigeon_sort([])
        
        self.assertEqual([], actual)
    
    def test_pigeon_sort_with_exception(self):
        """
        array = builtins.list[builtins.int]
        """
        # This test fails because function [sorts.pigeon_sort.pigeon_sort] produces [OverflowError]
        sorts.pigeon_sort.pigeon_sort([2, 2, 0, 170141183460469231731687303715884105727])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_pigeon_sort_with_exception1(self):
        """
        array = builtins.list[builtins.int]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        sorts.pigeon_sort.pigeon_sort([-170141183460469231731687303715749888000, -170141183460469231731687303715884105728])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_pigeon_sort_with_exception2(self):
        """
        array = builtins.list[builtins.int]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        sorts.pigeon_sort.pigeon_sort([-268435457, 1, 2, 1, 2])
    # endregion
    
    # endregion

