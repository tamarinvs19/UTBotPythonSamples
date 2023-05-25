import sys
sys.path.append(r'..\..\..')
import builtins
import matrix
import unittest
import matrix.binary_search_matrix


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.binary_search_matrix.binary_search
    
    # region FUZZER
    
    def test_binary_search(self):
        """
        array = builtins.list[builtins.int]
        lower_bound = -2 (mutated from -1)
        upper_bound = 2
        value = -70368744177665 (mutated from 170141183460469231731687233347139928063)
        """
        actual = matrix.binary_search_matrix.binary_search([-1, -10384593717069655257060992658440193, -1048577, -17179869185], -2, 2, -70368744177665)
        
        self.assertEqual(-1, actual)
    
    def test_binary_search1(self):
        """
        array = builtins.list[builtins.int]
        lower_bound = -2 (mutated from -1)
        upper_bound = 2
        value = -70368744177665 (mutated from 170141183460469231731687233347139928063)
        """
        actual = matrix.binary_search_matrix.binary_search([-1048577, -17179869185, -10384593717069655257060992658440193, -1], -2, 2, -70368744177665)
        
        self.assertEqual(-1, actual)
    
    def test_binary_search_with_exception(self):
        """
        array = builtins.list[typing.Any]
        lower_bound = -2 (mutated from -1)
        upper_bound = -2 (mutated from -1)
        value = 3 (mutated from 2)
        """
        # This test fails because function [matrix.binary_search_matrix.binary_search] produces [IndexError]
        matrix.binary_search_matrix.binary_search([], -2, -2, 3)
    
    def test_binary_search_with_exception1(self):
        """
        array = builtins.list[builtins.int]
        lower_bound = -2 (mutated from -1)
        upper_bound = 2
        value = -170141183460469231731687303715850551296 (mutated from min)
        """
        # This test fails because function [matrix.binary_search_matrix.binary_search] produces [IndexError]
        matrix.binary_search_matrix.binary_search([-2], -2, 2, -170141183460469231731687303715850551296)
    
    def test_binary_search_with_exception2(self):
        """
        array = builtins.list[builtins.int]
        lower_bound = -2 (mutated from -1)
        upper_bound = 2
        value = 33554432 (mutated from -170141183460469231731687303715850551296)
        """
        # This test fails because function [matrix.binary_search_matrix.binary_search] produces [IndexError]
        matrix.binary_search_matrix.binary_search([-2], -2, 2, 33554432)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.binary_search_matrix.mat_bin_search
    
    # region FUZZER
    
    def test_mat_bin_search_with_exception(self):
        """
        value = -65 (mutated from -1)
        matrix = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.binary_search_matrix.mat_bin_search] produces [IndexError]
        matrix.binary_search_matrix.mat_bin_search(-65, [])
    # endregion
    
    # endregion

