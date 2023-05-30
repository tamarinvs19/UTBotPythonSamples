import sys
sys.path.append(r'../../..')
import builtins
import matrix
import unittest
import matrix.max_area_of_island


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.max_area_of_island.is_safe
    
    # region FUZZER
    
    def test_is_safe(self):
        """
        row = max
        col = min
        rows = -65 (mutated from -1)
        cols = -1 (mutated from zero)
        """
        actual = matrix.max_area_of_island.is_safe(170141183460469231731687303715884105727, -170141183460469231731687303715884105728, -65, -1)
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.max_area_of_island.depth_first_search
    
    # region FUZZER
    
    def test_depth_first_search(self):
        """
        row = zero
        col = 34 (mutated from 2)
        seen = builtins.set[typing.Any]
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.max_area_of_island.depth_first_search(0, 34, set(), [[-1, -1, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728]])
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search_with_exception(self):
        """
        row = -170141183460469231731687303715884105727 (mutated from positive)
        col = max
        seen = builtins.set[typing.Any]
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.max_area_of_island.depth_first_search] produces [IndexError]
        matrix.max_area_of_island.depth_first_search(-170141183460469231731687303715884105727, 170141183460469231731687303715884105727, set(), [])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.max_area_of_island.find_max_area
    
    # region FUZZER
    
    def test_find_max_area(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.max_area_of_island.find_max_area([[]])
        
        self.assertEqual(0, actual)
    
    def test_find_max_area1(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.max_area_of_island.find_max_area([[-1, 170141183460469231731687303715884105727, -1], [-1, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [-1, -1, 170141183460469231731687303715884105727]])
        
        self.assertEqual(0, actual)
    
    def test_find_max_area2(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.max_area_of_island.find_max_area([])
        
        self.assertEqual(0, actual)
    
    def test_find_max_area3(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.max_area_of_island.find_max_area([[-1], [-170141183460469231731687303715884105728, 2, -1, 1], [1, 3, 36893488147419103233, -170141183460469231731687303715884105727], [-170141183460469231731687303715884105728, -170141183420855150474555134919112130560, 0, -159507359494189904748456847233641349120]])
        
        self.assertEqual(1, actual)
    
    def test_find_max_area_with_exception(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.max_area_of_island.find_max_area] produces [IndexError]
        matrix.max_area_of_island.find_max_area([[1, 3, 36893488147419103233, -170141183460469231731687303715884105727], [-170141183460469231731687303715884105728, 2, -1, 1], [-1], [-170141183460469231731687303715884105728, -170141183420855150474555134919112130560, 0, -159507359494189904748456847233641349120]])
    # endregion
    
    # endregion

