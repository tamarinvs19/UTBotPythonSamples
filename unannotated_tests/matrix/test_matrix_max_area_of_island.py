import sys
sys.path.append(r'..\..\..')
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
        col = 32 (mutated from zero)
        seen = builtins.set[builtins.int]
        mat = builtins.list[builtins.list[typing.Any]]
        """
        actual = matrix.max_area_of_island.depth_first_search(0, 32, set(), [[], [], [], [], []])
        
        self.assertEqual(0, actual)
    
    def test_depth_first_search_with_exception(self):
        """
        row = min (mutated from zero)
        col = zero
        seen = builtins.set[typing.Any]
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.max_area_of_island.depth_first_search] produces [IndexError]
        matrix.max_area_of_island.depth_first_search(-170141183460469231731687303715884105728, 0, set(), [])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.max_area_of_island.find_max_area
    
    # region FUZZER
    
    def test_find_max_area(self):
        """
        mat = builtins.list[typing.Any]
        """
        actual = matrix.max_area_of_island.find_max_area([])
        
        self.assertEqual(0, actual)
    
    def test_find_max_area1(self):
        """
        mat = builtins.list[builtins.list[typing.Any]]
        """
        actual = matrix.max_area_of_island.find_max_area([[]])
        
        self.assertEqual(0, actual)
    # endregion
    
    # endregion

