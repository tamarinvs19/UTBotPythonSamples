import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import divide_and_conquer
import unittest
import divide_and_conquer.max_difference_pair


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable divide_and_conquer.max_difference_pair.max_difference
    
    # region FUZZER
    
    def test_max_difference(self):
        """
        a = builtins.list[builtins.int]
        """
        actual = divide_and_conquer.max_difference_pair.max_difference([-1, 170141183460469231731687303715884105727, 0, 3])
        
        self.assertEqual((-1, 170141183460469231731687303715884105727), actual)
    
    def test_max_difference1(self):
        """
        a = builtins.list[builtins.int]
        """
        actual = divide_and_conquer.max_difference_pair.max_difference([170141183460469231731687303715884105727])
        
        self.assertEqual((170141183460469231731687303715884105727, 170141183460469231731687303715884105727), actual)
    
    def test_max_difference2(self):
        """
        a = builtins.list[builtins.int]
        """
        actual = divide_and_conquer.max_difference_pair.max_difference([1, 3, -170141183460469231731687303715884105728, 0])
        
        self.assertEqual((-170141183460469231731687303715884105728, 0), actual)
    
    def test_max_difference3(self):
        """
        a = builtins.list[builtins.int]
        """
        actual = divide_and_conquer.max_difference_pair.max_difference([34359738368, 3])
        
        self.assertEqual((34359738368, 34359738368), actual)
    
    def test_max_difference_with_exception(self):
        """
        a = builtins.list[builtins.int]
        """
        # This test fails because function [divide_and_conquer.max_difference_pair.max_difference] produces [RecursionError]
        divide_and_conquer.max_difference_pair.max_difference([])
    # endregion
    
    # endregion

