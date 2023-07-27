import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import sorts
import unittest
import sorts.pigeonhole_sort


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable sorts.pigeonhole_sort.pigeonhole_sort
    
    # region FUZZER
    
    def test_pigeonhole_sort(self):
        """
        a = builtins.list[builtins.int]
        """
        actual = sorts.pigeonhole_sort.pigeonhole_sort([170141183460469231731687303715884105727])
        
        self.assertEqual(None, actual)
    
    def test_pigeonhole_sort_with_exception(self):
        """
        a = builtins.list[typing.Any]
        """
        # This test fails because function [sorts.pigeonhole_sort.pigeonhole_sort] produces [ValueError]
        sorts.pigeonhole_sort.pigeonhole_sort([])
    
    def test_pigeonhole_sort_with_exception1(self):
        """
        a = builtins.list[builtins.int]
        """
        # This test fails because function [sorts.pigeonhole_sort.pigeonhole_sort] produces [OverflowError]
        sorts.pigeonhole_sort.pigeonhole_sort([-1, -1, 1, 170141183460469231731687303715884105727])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_pigeonhole_sort_with_exception2(self):
        """
        a = builtins.list[builtins.int]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        sorts.pigeonhole_sort.pigeonhole_sort([-170141183460469231731687303715749888000, -170141183460469231731687303715884105728])
    # endregion
    
    # endregion

