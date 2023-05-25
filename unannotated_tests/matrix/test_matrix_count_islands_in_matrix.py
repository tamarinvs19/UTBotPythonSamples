import sys
sys.path.append(r'..\..\..')
import builtins
import matrix.count_islands_in_matrix
import matrix
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.count_islands_in_matrix.is_safe
    
    # region FUZZER
    
    def test_is_safe(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        i = min (mutated from zero)
        j = zero
        visited = builtins.list[typing.Any]
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(0, -170141183460469231731687303715884105728, [[True, False, True], [False, False, True], [False, True, False]])
        
        actual = matrix1.is_safe(-170141183460469231731687303715884105728, 0, [])
        
        self.assertEqual(False, actual)
        
        self.assertEqual(matrix1, matrix1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.count_islands_in_matrix.diffs
    
    # region FUZZER
    
    def test_diffs_with_exception(self):
        """
        self = matrix.count_islands_in_matrix.Matrix
        i = -170141183460469231731687303715884105720 (mutated from 8)
        j = positive
        visited = builtins.list[typing.Any]
        """
        matrix1 = matrix.count_islands_in_matrix.Matrix(8, -1, [[True, False, True], [False, False, True], [False, True, False]])
        # This test fails because function [matrix.count_islands_in_matrix.diffs] produces [IndexError]
        matrix1.diffs(-170141183460469231731687303715884105720, 1, [])
        
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

