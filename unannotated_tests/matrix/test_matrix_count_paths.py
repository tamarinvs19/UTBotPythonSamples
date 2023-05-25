import sys
sys.path.append(r'..\..\..')
import builtins
import matrix
import unittest
import matrix.count_paths


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.count_paths.depth_first_search
    
    # region FUZZER
    
    def test_depth_first_search(self):
        """
        grid = builtins.list[builtins.list[typing.Any]]
        row = 20769187434139310514121985316880386 (mutated from 2)
        col = -170141183460469231731687303715884105727 (mutated from positive)
        visit = builtins.set[builtins.int]
        """
        actual = matrix.count_paths.depth_first_search([[]], 20769187434139310514121985316880386, -170141183460469231731687303715884105727, {-1})
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search1(self):
        """
        grid = builtins.list[builtins.list[typing.Any]]
        row = max
        col = zero (mutated from min)
        visit = builtins.set[builtins.int]
        """
        actual = matrix.count_paths.depth_first_search([[], [], []], 170141183460469231731687303715884105727, 0, set())
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search2(self):
        """
        grid = builtins.list[builtins.list[typing.Any]]
        row = positive (mutated from zero)
        col = 170141183460314489226776631181521715199 (mutated from max)
        visit = builtins.set[builtins.int]
        """
        actual = matrix.count_paths.depth_first_search([[]], 1, 170141183460314489226776631181521715199, set())
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search3(self):
        """
        grid = builtins.list[builtins.list[builtins.int]]
        row = zero
        col = zero
        visit = builtins.set[builtins.int]
        """
        actual = matrix.count_paths.depth_first_search([[1, -170141183460469231731687303715884105727, -170141183460469231731687303715884105727], [-170141183460469231731687303715884105727, 1, -170141183460469231731687303715884105727], [-170141183460469231731687303715884105727, 1, -170141183460469231731687303715884105727]], 0, 0, {170141183460469231731687303715884105727})
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search_with_exception(self):
        """
        grid = builtins.list[typing.Any]
        row = 2 (mutated from positive)
        col = zero
        visit = builtins.set[typing.Any]
        """
        # This test fails because function [matrix.count_paths.depth_first_search] produces [IndexError]
        matrix.count_paths.depth_first_search([], 2, 0, set())
    
    def test_depth_first_search_with_exception1(self):
        """
        grid = builtins.list[builtins.list[typing.Any]]
        row = 20769187434139310514121985316880386 (mutated from 2)
        col = positive (mutated from zero)
        visit = builtins.set[builtins.int]
        """
        # This test fails because function [matrix.count_paths.depth_first_search] produces [IndexError]
        matrix.count_paths.depth_first_search([[]], 20769187434139310514121985316880386, 1, {-1})
    # endregion
    
    # endregion

