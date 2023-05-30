import sys
sys.path.append(r'../../..')
import builtins
import matrix
import unittest
import matrix.count_paths


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.count_paths.depth_first_search
    
    # region FUZZER
    
    def test_depth_first_search(self):
        """
        grid = builtins.list[builtins.list[builtins.int]]
        row = 2 (mutated from positive)
        col = min (mutated from zero)
        visit = builtins.set[typing.Any]
        """
        actual = matrix.count_paths.depth_first_search([[]], 2, -170141183460469231731687303715884105728, set())
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search1(self):
        """
        grid = builtins.list[builtins.list[builtins.int]]
        row = max (mutated from -1)
        col = zero
        visit = builtins.set[typing.Any]
        """
        actual = matrix.count_paths.depth_first_search([[]], 170141183460469231731687303715884105727, 0, set())
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search2(self):
        """
        grid = builtins.list[builtins.list[builtins.int]]
        row = zero
        col = zero
        visit = builtins.set[builtins.int]
        """
        actual = matrix.count_paths.depth_first_search([[1, -170141183460469231731687303715884105727, -170141183460469231731687303715884105727], [-170141183460469231731687303715884105727, 1, -170141183460469231731687303715884105727], [-170141183460469231731687303715884105727, 1, -170141183460469231731687303715884105727]], 0, 0, {170141183460469231731687303715884105727})
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search3(self):
        """
        grid = builtins.list[builtins.list[builtins.int]]
        row = 2 (mutated from positive)
        col = 68719476738 (mutated from 2)
        visit = builtins.set[builtins.list[typing.Any]]
        """
        actual = matrix.count_paths.depth_first_search([[2, 34], [2, 34]], 2, 68719476738, {[]})
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search4(self):
        """
        grid = builtins.list[builtins.list[builtins.int]]
        row = 2 (mutated from positive)
        col = 2 (mutated from positive)
        visit = builtins.set[typing.Union[builtins.int, builtins.list[typing.Any], builtins.str, builtins.bool, builtins.float, builtins.dict[typing.Any, typing.Any]]]
        """
        actual = matrix.count_paths.depth_first_search([[0, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-1, -147573952589676412929, -2475880078570760549798248449], [170141183460469231731687303715884105727, 2, 170141183460469231731687303715884105727]], 2, 2, {False})
        
        self.assertEqual(1, actual)
    
    def test_depth_first_search_with_exception(self):
        """
        grid = builtins.list[builtins.list[builtins.int]]
        row = max
        col = 2 (mutated from positive)
        visit = builtins.set[typing.Any]
        """
        # This test fails because function [matrix.count_paths.depth_first_search] produces [IndexError]
        matrix.count_paths.depth_first_search([[170141183460469231731687303715884105727, 170141183460469231731687303715883843583, 170141183460469231731687303715615670271, -1, -1], [170141183460469231731687303715884105727, 170141183460469231731687303715883843583, 170141183460469231731687303715615668223, -1, -1], [170141183460469231731687303715883843583, 170141183460469231731687303715615670271, -1, -1, 170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 170141183460469231731687303715883843583, 170139885386254598024780171091533365247, -1, -1], [-1, 170141183460469231731687303715884105727, -1, 170141183460469231731687303715883843583, 170141183460469231731687303715615670271]], 170141183460469231731687303715884105727, 2, set())
    
    def test_depth_first_search_with_exception1(self):
        """
        grid = builtins.list[builtins.list[builtins.int]]
        row = -170141183460469231731687303715884105726 (mutated from 2)
        col = -1 (mutated from zero)
        visit = builtins.set[typing.Any]
        """
        # This test fails because function [matrix.count_paths.depth_first_search] produces [IndexError]
        matrix.count_paths.depth_first_search([], -170141183460469231731687303715884105726, -1, set())
    # endregion
    
    # endregion

