import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import searches
import unittest
import searches.jump_search


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable searches.jump_search.jump_search
    
    # region FUZZER
    
    def test_jump_search(self):
        """
        arr = builtins.list[builtins.int]
        x = -1 (mutated from zero)
        """
        actual = searches.jump_search.jump_search([36028797018963970, -1, -2, 170141183460469231731687303715884105727], -1)
        
        self.assertEqual(-1, actual)
    
    def test_jump_search1(self):
        """
        arr = builtins.list[builtins.int]
        x = max (mutated from -1)
        """
        actual = searches.jump_search.jump_search([36028797018963970, -1, -2, 170141183460469231731687303715884105727], 170141183460469231731687303715884105727)
        
        self.assertEqual(3, actual)
    
    def test_jump_search2(self):
        """
        arr = builtins.list[builtins.int]
        x = 16 (mutated from zero)
        """
        actual = searches.jump_search.jump_search([-1, -1, -1, -1, -1], 16)
        
        self.assertEqual(-1, actual)
    
    def test_jump_search_with_exception(self):
        """
        arr = builtins.list[typing.Any]
        x = -134217729 (mutated from -1)
        """
        # This test fails because function [searches.jump_search.jump_search] produces [IndexError]
        searches.jump_search.jump_search([], -134217729)
    # endregion
    
    # endregion

