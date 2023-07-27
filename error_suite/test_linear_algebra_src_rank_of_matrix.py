import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import linear_algebra
import unittest
import linear_algebra.src.rank_of_matrix


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable linear_algebra.src.rank_of_matrix.rank_of_matrix
    
    # region FUZZER
    
    def test_rank_of_matrix(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        matrix = [[170141183460469231731687303715884105727, 1.0, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 0, -1, float('inf')], [170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [float('-inf'), float('-inf'), -170141183460469231731687303715884105728, 1]]
        
        actual = linear_algebra.src.rank_of_matrix.rank_of_matrix(matrix)
        
        self.assertEqual(4, actual)
    
    def test_rank_of_matrix1(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        actual = linear_algebra.src.rank_of_matrix.rank_of_matrix([[0.0]])
        
        self.assertEqual(0, actual)
    
    def test_rank_of_matrix2(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        actual = linear_algebra.src.rank_of_matrix.rank_of_matrix([[1.0, float('-inf'), 0, 1.0, 0.0]])
        
        self.assertEqual(1, actual)
    
    def test_rank_of_matrix3(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        matrix = [[1.0, 1.0, 1, float('-inf'), -170141183460469231731687303715884105728], [1.0, 1.0, 1, float('-inf'), -170141183460469231731687303715884105728], [1.0, 1.0, 1, float('-inf'), -170141183460469231731687303715884105728], [1.0, 1.0, 1, float('-inf'), -170141183460469231731687303715884105728], [1.0, 1.0, 1, float('-inf'), -170141183460469231731687303715884105728]]
        
        actual = linear_algebra.src.rank_of_matrix.rank_of_matrix(matrix)
        
        self.assertEqual(3, actual)
    
    def test_rank_of_matrix4(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        matrix = [[2, 2, 2, 2], [1.0, 1.0, 1.0, 1.0], [0.0, float('nan'), 0.0, 170141183460469231731687303715884105727], [0.0, 0.0, 0.0, 0.0]]
        
        actual = linear_algebra.src.rank_of_matrix.rank_of_matrix(matrix)
        
        self.assertEqual(2, actual)
    
    def test_rank_of_matrix5(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        matrix = [[0.0, 1.0, float('-inf'), 0, 1.0], [1, 1]]
        
        actual = linear_algebra.src.rank_of_matrix.rank_of_matrix(matrix)
        
        self.assertEqual(2, actual)
    
    def test_rank_of_matrix6(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        actual = linear_algebra.src.rank_of_matrix.rank_of_matrix([[], [0.0, float('inf'), -1, 2, 0], [1.0, 0.0, 0, 2, -170141183460469231731687303715884105728], [0.0, 0.0, -1.1125369292536007E-308, 0.0, 0.0], [0, 2, 170141183460469231731687303715884105727, float('inf'), 2]])
        
        self.assertEqual(0, actual)
    
    def test_rank_of_matrix_with_exception(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        matrix = [[1.0, 1.0, -170141183460469231731687303715884105728, 1.0, 0.0], [1, 1.0, float('inf'), 0, 1.0], [-170141183460469231731687303715884105728, 0.0, -1, 170141183460469231731687303715884105727, 2], [0, 170141183460469231731687303715884105727, 1.0, 0.0, 1.0], [-1]]
        # This test fails because function [linear_algebra.src.rank_of_matrix.rank_of_matrix] produces [IndexError]
        linear_algebra.src.rank_of_matrix.rank_of_matrix(matrix)
    
    def test_rank_of_matrix_with_exception1(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        # This test fails because function [linear_algebra.src.rank_of_matrix.rank_of_matrix] produces [IndexError]
        linear_algebra.src.rank_of_matrix.rank_of_matrix([])
    
    def test_rank_of_matrix_with_exception2(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        matrix = [[0.0, 0, -1, 1.0, 170141183460469231731687303715884105727], [float('inf'), 0.0, 1.0, 1, 170141183460469231731687303715884105727], [float('nan'), -170141183460469231731687303715884105728, 1.0, 2, float('nan')], [1.0, 0], [0.0, 1.0, -1, 2, 0.0]]
        # This test fails because function [linear_algebra.src.rank_of_matrix.rank_of_matrix] produces [IndexError]
        linear_algebra.src.rank_of_matrix.rank_of_matrix(matrix)
    
    def test_rank_of_matrix_with_exception3(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        # This test fails because function [linear_algebra.src.rank_of_matrix.rank_of_matrix] produces [IndexError]
        linear_algebra.src.rank_of_matrix.rank_of_matrix([[0, 2, 170141183460469231731687303715884105727, float('inf'), 2], [], [-170141183460469231731687303715884105728, 2, 0.0, 1.0, 0], [0.0, float('inf'), -1, 2, 0], [0.0, 0.0, 0.0, 0.0, 0.0]])
    
    def test_rank_of_matrix_with_exception4(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        # This test fails because function [linear_algebra.src.rank_of_matrix.rank_of_matrix] produces [IndexError]
        linear_algebra.src.rank_of_matrix.rank_of_matrix([[-170141183460469231731687303715884105728, 1.0, 0, 0.0, 2], [], [0.0, 0.0, -1.1125369292536007E-308, 0.0, 0.0], [-1, float('inf'), 2, 0.0, 0], [0, 2, 170141183460469231731687303715884105727, float('inf'), 2]])
    
    def test_rank_of_matrix_with_exception5(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        matrix = [[0.0, 0.0, 0.0], [0.0, 1.0, 2], [1.0]]
        # This test fails because function [linear_algebra.src.rank_of_matrix.rank_of_matrix] produces [IndexError]
        linear_algebra.src.rank_of_matrix.rank_of_matrix(matrix)
    
    def test_rank_of_matrix_with_exception6(self):
        """
        matrix = builtins.list[builtins.list[typing.Union[builtins.int, builtins.float]]]
        """
        matrix = [[0.0, 1.0, 1], [0.0], [0, float('-inf'), 1.0, float('inf'), 2], [0.0, -1, 0.0, 2, -170141183460469231731687303715884105728], [0.0, -170141183460469231731687303715884105728, 1.0, -1, 170141183460469231731687303715884105727]]
        # This test fails because function [linear_algebra.src.rank_of_matrix.rank_of_matrix] produces [IndexError]
        linear_algebra.src.rank_of_matrix.rank_of_matrix(matrix)
    # endregion
    
    # endregion

