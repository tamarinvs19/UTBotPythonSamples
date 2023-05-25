import sys
sys.path.append(r'..\..\..')
import builtins
import data_structures.arrays.prefix_sum
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.arrays.prefix_sum.get_sum
    
    # region FUZZER
    
    def test_get_sum(self):
        """
        self = data_structures.arrays.prefix_sum.PrefixSum
        start = -1 (mutated from zero)
        end = zero
        """
        prefix_sum = data_structures.arrays.prefix_sum.PrefixSum([2, -1, -1, 170141183460469231731687303715884105727, -1])
        
        actual = prefix_sum.get_sum(-1, 0)
        
        self.assertEqual(-170141183460469231731687303715884105725, actual)
        
        self.assertEqual(prefix_sum, prefix_sum)
    
    def test_get_sum1(self):
        """
        self = data_structures.arrays.prefix_sum.PrefixSum
        start = zero (mutated from 2)
        end = zero (mutated from min)
        """
        prefix_sum = data_structures.arrays.prefix_sum.PrefixSum([170141183460469231731687303715884105727, 170141183460469231731687303711589138431, -1])
        
        actual = prefix_sum.get_sum(0, 0)
        
        self.assertEqual(170141183460469231731687303715884105727, actual)
        
        self.assertEqual(prefix_sum, prefix_sum)
    
    def test_get_sum_with_exception(self):
        """
        self = data_structures.arrays.prefix_sum.PrefixSum
        start = -562949953421313 (mutated from -1)
        end = zero
        """
        prefix_sum = data_structures.arrays.prefix_sum.PrefixSum([2, -1, -1, 170141183460469231731687303715884105727, -1])
        # This test fails because function [data_structures.arrays.prefix_sum.get_sum] produces [IndexError]
        prefix_sum.get_sum(-562949953421313, 0)
        
        self.assertEqual(prefix_sum, prefix_sum)
    
    def test_get_sum_with_exception1(self):
        """
        self = data_structures.arrays.prefix_sum.PrefixSum
        start = zero (mutated from 2)
        end = min (mutated from zero)
        """
        prefix_sum = data_structures.arrays.prefix_sum.PrefixSum([170141183460469231731687303715884105727, 170141183460469231731687303711589138431, -1])
        # This test fails because function [data_structures.arrays.prefix_sum.get_sum] produces [IndexError]
        prefix_sum.get_sum(0, -170141183460469231731687303715884105728)
        
        self.assertEqual(prefix_sum, prefix_sum)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.arrays.prefix_sum.contains_sum
    
    # region FUZZER
    
    def test_contains_sum(self):
        """
        self = data_structures.arrays.prefix_sum.PrefixSum
        target_sum = -170141183460469231731687303715884105727 (mutated from positive)
        """
        prefix_sum = data_structures.arrays.prefix_sum.PrefixSum([1])
        
        actual = prefix_sum.contains_sum(-170141183460469231731687303715884105727)
        
        self.assertEqual(False, actual)
        
        self.assertEqual(prefix_sum, prefix_sum)
    
    def test_contains_sum1(self):
        """
        self = data_structures.arrays.prefix_sum.PrefixSum
        target_sum = -1 (mutated from max)
        """
        prefix_sum = data_structures.arrays.prefix_sum.PrefixSum([170141183460469231731687303715884105727, 0, -1])
        
        actual = prefix_sum.contains_sum(-1)
        
        self.assertEqual(True, actual)
        
        self.assertEqual(prefix_sum, prefix_sum)
    # endregion
    
    # endregion

