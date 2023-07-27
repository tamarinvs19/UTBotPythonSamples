import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import searches
import unittest
import searches.double_linear_search_recursion


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable searches.double_linear_search_recursion.search
    
    # region FUZZER
    
    def test_search(self):
        """
        list_data = builtins.list[typing.Any]
        key = 134217728 (mutated from zero)
        """
        actual = searches.double_linear_search_recursion.search([], 134217728)
        
        self.assertEqual(-1, actual)
    
    def test_search1(self):
        """
        list_data = builtins.list[builtins.int]
        key = zero (mutated from positive)
        """
        actual = searches.double_linear_search_recursion.search([-36028797018963969, 0, -2, 170141183460469231731687303715884105727], 0)
        
        self.assertEqual(1, actual)
    
    def test_search2(self):
        """
        list_data = builtins.list[builtins.int]
        key = min (mutated from zero)
        """
        actual = searches.double_linear_search_recursion.search([-36028797018963969, 0, -2, 170141183460469231731687303715884105727], -170141183460469231731687303715884105728)
        
        self.assertEqual(-1, actual)
    
    def test_search3(self):
        """
        list_data = builtins.list[builtins.int]
        key = zero (mutated from positive)
        """
        actual = searches.double_linear_search_recursion.search([-36028797018963969, 170141183460469231731687303715884105727, 0, -268435458], 0)
        
        self.assertEqual(2, actual)
    
    def test_search4(self):
        """
        list_data = builtins.list[builtins.int]
        key = zero (mutated from positive)
        """
        actual = searches.double_linear_search_recursion.search([0, 170141183460469231731687303715884105727, -36028797018963969, -268435458], 0)
        
        self.assertEqual(0, actual)
    
    def test_search5(self):
        """
        list_data = builtins.list[builtins.int]
        key = zero (mutated from positive)
        """
        actual = searches.double_linear_search_recursion.search([-36028797018963969, 170141183460469231731687303715884105727, -268435458, 0], 0)
        
        self.assertEqual(3, actual)
    
    def test_search_with_exception(self):
        """
        list_data = builtins.list[typing.Any]
        key = min (mutated from zero)
        left = -2 (mutated from -1)
        right = max
        """
        # This test fails because function [searches.double_linear_search_recursion.search] produces [IndexError]
        searches.double_linear_search_recursion.search([], -170141183460469231731687303715884105728, -2, 170141183460469231731687303715884105727)
    
    def test_search_with_exception1(self):
        """
        list_data = builtins.list[builtins.int]
        key = zero (mutated from positive)
        left = zero (mutated from min)
        right = 9 (mutated from positive)
        """
        # This test fails because function [searches.double_linear_search_recursion.search] produces [IndexError]
        searches.double_linear_search_recursion.search([-1, 0, -2, 170141183460469231731687303715884105727], 0, 0, 9)
    # endregion
    
    # endregion

