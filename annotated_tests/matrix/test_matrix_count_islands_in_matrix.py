import sys
sys.path.append(r'../../..')
import builtins
import matrix.count_islands_in_matrix
import types
import matrix
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.count_islands_in_matrix.is_safe
    
    # region FUZZER
    
    def test_is_safe(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        i = 170141183460469231731687303715884072959 (mutated from -32769)
        j = -1 (mutated from zero)
        visited = builtins.list[builtins.list[builtins.bool]]
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(170141183460469231731687303715884105727, 1, [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]])
        
        actual = matrix1.is_safe(170141183460469231731687303715884072959, -1, [[True]])
        
        self.assertEqual(False, actual)
        
        self.assertEqual(matrix1, matrix1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.count_islands_in_matrix.diffs
    
    # region FUZZER
    
    def test_diffs(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        i = zero (mutated from positive)
        j = zero (mutated from min)
        visited = builtins.list[builtins.list[builtins.bool]]
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(9, 9, [[]])
        
        actual = matrix1.diffs(0, 0, [[True, True, True, True], [True, True, True, True], [True, False, False, True], [True, True, True, True]])
        
        self.assertEqual(None, actual)
        
        self.assertEqual(matrix1, matrix1)
    
    def test_diffs_with_exception(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        i = 32775 (mutated from 7)
        j = zero (mutated from positive)
        visited = builtins.list[builtins.list[builtins.bool]]
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(-2, 9, [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]])
        # This test fails because function [matrix.count_islands_in_matrix.diffs] produces [IndexError]
        matrix1.diffs(32775, 0, [[True]])
        
        self.assertEqual(matrix1, matrix1)
    
    def test_diffs_with_exception1(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        i = zero (mutated from positive)
        j = zero (mutated from min)
        visited = builtins.list[builtins.list[builtins.bool]]
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(9, 9, [[]])
        # This test fails because function [matrix.count_islands_in_matrix.diffs] produces [IndexError]
        matrix1.diffs(0, 0, [[True, False, False, True], [True, True, True, True], [True, True, True, True], [True, True, True, True]])
        
        self.assertEqual(matrix1, matrix1)
    
    def test_diffs_with_exception2(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        i = -1
        j = 2 (mutated from positive)
        visited = builtins.list[builtins.list[builtins.bool]]
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(8, 7, [[True, True], [True, True]])
        visited = [[False, False, False, False], [False, False], [True, True, True]]
        # This test fails because function [matrix.count_islands_in_matrix.diffs] produces [IndexError]
        matrix1.diffs(-1, 2, visited)
        
        self.assertEqual([[True, True, False, False], [True, True], [True, True, True]], visited)
        
        self.assertEqual(matrix1, matrix1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.count_islands_in_matrix.count_islands
    
    # region FUZZER
    
    def test_count_islands(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(0, 170140858941915573304960520559863529471, [[False, False, False, False, False]])
        
        actual = matrix1.count_islands()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(matrix1, matrix1)
    
    def test_count_islands1(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(8, -334660377430272204755635839959057, [[False, False, False, False, False]])
        
        actual = matrix1.count_islands()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(matrix1, matrix1)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_count_islands_with_exception(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(16, 170140858941915573304960450191119351807, [[False, False, False, False, False]])
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.count_islands()
    # endregion
    
    # endregion

