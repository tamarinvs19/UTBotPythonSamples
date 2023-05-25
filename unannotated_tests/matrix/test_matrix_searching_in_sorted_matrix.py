import sys
sys.path.append(r'..\..\..')
import builtins
import types
import matrix
import unittest
import matrix.searching_in_sorted_matrix


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix
    
    # region FUZZER
    
    def test_search_in_a_sorted_matrix(self):
        """
        mat = builtins.list[typing.Any]
        m = -1 (mutated from zero)
        n = positive
        key = builtins.object
        """
        key = builtins.object()
        key1 = key
        
        actual = matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([], -1, 1, key1)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(key, key1)
    
    def test_search_in_a_sorted_matrix_with_exception(self):
        """
        mat = builtins.list[typing.Any]
        m = max (mutated from -1)
        n = positive
        key = builtins.object
        """
        key = builtins.object()
        key1 = key
        # This test fails because function [matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix] produces [IndexError]
        matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([], 170141183460469231731687303715884105727, 1, key1)
        
        self.assertEqual(key, key1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.searching_in_sorted_matrix.main
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_main_with_exception(self):
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.searching_in_sorted_matrix.main()
    # endregion
    
    # endregion

