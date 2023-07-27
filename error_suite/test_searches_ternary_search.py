import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import searches
import unittest
import searches.ternary_search


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable searches.ternary_search.lin_search
    
    # region FUZZER
    
    def test_lin_search(self):
        """
        left = 36028797018963968 (mutated from zero)
        right = 2 (mutated from positive)
        array = builtins.list[builtins.int]
        target = min
        """
        actual = searches.ternary_search.lin_search(36028797018963968, 2, [-2, 170141183460469231731687303715884105727, -1], -170141183460469231731687303715884105728)
        
        self.assertEqual(-1, actual)
    
    def test_lin_search1(self):
        """
        left = zero (mutated from positive)
        right = 2 (mutated from positive)
        array = builtins.list[builtins.int]
        target = max (mutated from -1)
        """
        actual = searches.ternary_search.lin_search(0, 2, [-170141183460469231731687303715884105728, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], 170141183460469231731687303715884105727)
        
        self.assertEqual(-1, actual)
    
    def test_lin_search2(self):
        """
        left = zero (mutated from positive)
        right = 1073741825 (mutated from positive)
        array = builtins.list[builtins.int]
        target = min
        """
        actual = searches.ternary_search.lin_search(0, 1073741825, [-2, 1, -170141183460469231731687303715884105728, 0], -170141183460469231731687303715884105728)
        
        self.assertEqual(2, actual)
    
    def test_lin_search_with_exception(self):
        """
        left = -170141183460469231731687303715884105726 (mutated from 2)
        right = -1 (mutated from max)
        array = builtins.list[builtins.int]
        target = max
        """
        # This test fails because function [searches.ternary_search.lin_search] produces [IndexError]
        searches.ternary_search.lin_search(-170141183460469231731687303715884105726, -1, [-1, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728, 1, -1], 170141183460469231731687303715884105727)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.ternary_search.ite_ternary_search
    
    # region FUZZER
    
    def test_ite_ternary_search(self):
        """
        array = builtins.list[builtins.int]
        target = zero
        """
        actual = searches.ternary_search.ite_ternary_search([-36028797018963970, 0, 2, -2], 0)
        
        self.assertEqual(1, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.ternary_search.rec_ternary_search
    
    # region FUZZER
    
    def test_rec_ternary_search(self):
        """
        left = 36028797018963969 (mutated from positive)
        right = 3
        array = builtins.list[builtins.int]
        target = 2 (mutated from 3)
        """
        actual = searches.ternary_search.rec_ternary_search(36028797018963969, 3, [-1, -2, -170141183460469231731687303715884105728], 2)
        
        self.assertEqual(-1, actual)
    
    def test_rec_ternary_search1(self):
        """
        left = -1
        right = zero (mutated from min)
        array = builtins.list[builtins.int]
        target = 170141183460469231731687303715884103679 (mutated from max)
        """
        actual = searches.ternary_search.rec_ternary_search(-1, 0, [4], 170141183460469231731687303715884103679)
        
        self.assertEqual(-1, actual)
    
    def test_rec_ternary_search2(self):
        """
        left = min
        right = 170141183460469231731687303715884105726 (mutated from -2)
        array = builtins.list[builtins.int]
        target = 4 (mutated from 3)
        """
        actual = searches.ternary_search.rec_ternary_search(-170141183460469231731687303715884105728, 170141183460469231731687303715884105726, [4, 4, -2, -1], 4)
        
        self.assertEqual(0, actual)
    
    def test_rec_ternary_search3(self):
        """
        left = min
        right = 170141183460469231731687303715884105726 (mutated from -2)
        array = builtins.list[builtins.int]
        target = 4 (mutated from 3)
        """
        actual = searches.ternary_search.rec_ternary_search(-170141183460469231731687303715884105728, 170141183460469231731687303715884105726, [-1, 4, -2, 4], 4)
        
        self.assertEqual(-1, actual)
    
    def test_rec_ternary_search4(self):
        """
        left = min
        right = 170141183460469231731687303715884105726 (mutated from -2)
        array = builtins.list[builtins.int]
        target = 4 (mutated from 3)
        """
        actual = searches.ternary_search.rec_ternary_search(-170141183460469231731687303715884105728, 170141183460469231731687303715884105726, [-8796093022209, -2, 16777220, 134217732], 4)
        
        self.assertEqual(-1, actual)
    
    def test_rec_ternary_search_with_exception(self):
        """
        left = min
        right = 170141183460469231731686740765930684415 (mutated from max)
        array = builtins.list[builtins.int]
        target = -2 (mutated from -1)
        """
        # This test fails because function [searches.ternary_search.rec_ternary_search] produces [IndexError]
        searches.ternary_search.rec_ternary_search(-170141183460469231731687303715884105728, 170141183460469231731686740765930684415, [0, 0, 0], -2)
    
    def test_rec_ternary_search_with_exception1(self):
        """
        left = -1
        right = 8 (mutated from zero)
        array = builtins.list[builtins.int]
        target = 170141183460469231731687303715884103679 (mutated from -2049)
        """
        # This test fails because function [searches.ternary_search.rec_ternary_search] produces [IndexError]
        searches.ternary_search.rec_ternary_search(-1, 8, [67108868], 170141183460469231731687303715884103679)
    
    def test_rec_ternary_search_with_exception2(self):
        """
        left = min
        right = max
        array = builtins.list[builtins.int]
        target = 2 (mutated from 3)
        """
        # This test fails because function [searches.ternary_search.rec_ternary_search] produces [IndexError]
        searches.ternary_search.rec_ternary_search(-170141183460469231731687303715884105728, 170141183460469231731687303715884105727, [0], 2)
    
    def test_rec_ternary_search_with_exception3(self):
        """
        left = min
        right = max
        array = builtins.list[builtins.int]
        target = 2 (mutated from 3)
        """
        # This test fails because function [searches.ternary_search.rec_ternary_search] produces [IndexError]
        searches.ternary_search.rec_ternary_search(-170141183460469231731687303715884105728, 170141183460469231731687303715884105727, [4294967296], 2)
    
    def test_rec_ternary_search_with_exception4(self):
        """
        left = -170141183460469231731687303715884105727 (mutated from min)
        right = 170141183460469231731687303715884105722 (mutated from 170141183460469231731687303715884105726)
        array = builtins.list[builtins.int]
        target = 2574915281713590971799305242754 (mutated from 2574915281713590971790715308162)
        """
        # This test fails because function [searches.ternary_search.rec_ternary_search] produces [IndexError]
        searches.ternary_search.rec_ternary_search(-170141183460469231731687303715884105727, 170141183460469231731687303715884105722, [147573952593971380224], 2574915281713590971799305242754)
    # endregion
    
    # endregion

