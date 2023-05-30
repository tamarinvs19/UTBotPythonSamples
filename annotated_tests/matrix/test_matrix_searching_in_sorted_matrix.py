import sys
sys.path.append(r'../../..')
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
        mat = builtins.list[builtins.list[builtins.int]]
        m = -36028797018963969 (mutated from -1)
        n = 2 (mutated from positive)
        key = positive
        """
        actual = matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([[]], -36028797018963969, 2, 1)
        
        self.assertEqual(None, actual)
    
    def test_search_in_a_sorted_matrix1(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        m = positive
        n = 158456325028528675187087900673 (mutated from positive)
        key = positive
        """
        actual = matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([[2, -170141183460469231731687303715884105726, 1026, -170141183460469231731687303715884105726, 2475880078570760549798248450], [2475880078570760549798248450, 2, -170141183460469231731687303715884105726, -170141183460469231731687303715884105726, 1026], [2475880078570760549798248450, 2, 1026, -170141183460469231731687303715884105726, -170141183460469231731687303715884105726], [-170141183460469231731687303715884105726, 1026, 2, -170141183460469231731687303715884105726, 2475880078570760549798248450], [2, -170141183460469231731687303715884105726, 1026, -170141183460469231731687303715884105726, 2475880078570760549798510594]], 1, 158456325028528675187087900673, 1.0)
        
        self.assertEqual(None, actual)
    
    def test_search_in_a_sorted_matrix2(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        m = positive
        n = 158456325028528675191382867969 (mutated from 158456325028528675187087900673)
        key = positive
        """
        actual = matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([[-170141183460469231731687303715884105726, 1026, 2, -170141183460469231731687303715884105726, 2475880078570760549798248450], [2, -170141183460469231731687303715884105726, 1026, -170141183460469231731687303715884105726, 2475880078570760549798510594], [2475880078570760549798248450, 2, -170141183460469231731687303715884105726, -170141183460469231731687303715884105726, 1026], [2, -170141183460469231731687303715884105726, 1026, -170141183460469231731687303715884105726, 2475880078570760549798248450], [2475880078570760549798248450, 2, 1026, -170141183460469231731687303715884105726, -170141183460469231731687303715884105726]], 1, 158456325028528675191382867969, 1.0)
        
        self.assertEqual(None, actual)
    
    def test_search_in_a_sorted_matrix3(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        m = positive
        n = 16777217 (mutated from positive)
        key = zero
        """
        actual = matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([[-170141183460469231731687303715884105728, 0, -1, -170141183460469231731687303715884105728], [2, 1180591620717411303426, -170141183460469231731687303715884105726, -170141183460469231731687303715884105726], [170141183460469231731687303715884105727, 2, 2, 0], [170141183460469231731687303715884105727, 2, -170141183460469231731687303715884105728, 170141183460469231731687303715884105727]], 1, 16777217, 0.0)
        
        self.assertEqual(None, actual)
    
    def test_search_in_a_sorted_matrix_with_exception(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        m = max
        n = 2 (mutated from positive)
        key = -170141183460469231731687303713736622080 (mutated from min)
        """
        # This test fails because function [matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix] produces [IndexError]
        matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([[170141183460469231731687303715884105727]], 170141183460469231731687303715884105727, 2, -170141183460469231731687303713736622080)
    
    def test_search_in_a_sorted_matrix_with_exception1(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        m = 2 (mutated from positive)
        n = 32 (mutated from zero)
        key = zero (mutated from positive)
        """
        # This test fails because function [matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix] produces [IndexError]
        matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([[-170141183460469231731687303715884105728, -170141183460469231731687303715884105720, -170141183460469231731687303715884072960], [170141183460469231731687303715884105727, 170141183460391860479231967448702910463, -1], [2, 1099511627778, 16386]], 2, 32, 0)
    
    def test_search_in_a_sorted_matrix_with_exception2(self):
        """
        mat = builtins.list[builtins.list[builtins.int]]
        m = 2 (mutated from positive)
        n = 32 (mutated from zero)
        key = zero (mutated from positive)
        """
        # This test fails because function [matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix] produces [IndexError]
        matrix.searching_in_sorted_matrix.search_in_a_sorted_matrix([[170141183460469231731687303715884105727, 170141183460391860479231967448702910463, -1], [-170141183460469231731687303715884105728, -170141183460469231731687303715884105720, -170141183460469231731687303715884072960], [2, 1099511627778, 16386]], 2, 32, 0)
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

