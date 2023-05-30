import sys
sys.path.append(r'../../..')
import builtins
import types
import matrix
import unittest
import matrix.matrix_operation


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.matrix_operation.add
    
    # region FUZZER
    
    def test_add(self):
        actual = matrix.matrix_operation.add()
        
        self.assertEqual([], actual)
    
    def test_add_with_exception(self):
        """
        matrix_s = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.add] produces [IndexError]
        matrix.matrix_operation.add([])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation.subtract
    
    # region FUZZER
    
    def test_subtract(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation.subtract([[0]], [[1]])
        
        self.assertEqual([[-1]], actual)
    
    def test_subtract_with_exception(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.subtract] produces [ValueError]
        matrix.matrix_operation.subtract([[]], [[170141183460469231731687303715884105727, 1, 1], [170141183460469231731687303715884105727, 1, 1], [1, 170141183460469231731687303715884105727, 1]])
    
    def test_subtract_with_exception1(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.subtract] produces [IndexError]
        matrix.matrix_operation.subtract([[0, 256], [0, -170141183460469231731687303715884105728]], [])
    
    def test_subtract_with_exception2(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.subtract] produces [IndexError]
        matrix.matrix_operation.subtract([], [[-1]])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation.scalar_multiply
    
    # region FUZZER
    
    def test_scalar_multiply(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        n = -170141183460469231731651274918865141760 (mutated from min)
        """
        actual = matrix.matrix_operation.scalar_multiply([[]], -170141183460469231731651274918865141760)
        
        self.assertEqual([[]], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation.multiply
    
    # region FUZZER
    
    def test_multiply(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation.multiply([[1]], [[1]])
        
        self.assertEqual([[1]], actual)
    
    def test_multiply_with_exception(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.multiply] produces [ValueError]
        matrix.matrix_operation.multiply([[]], [[-1, -1, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728]])
    
    def test_multiply_with_exception1(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.multiply] produces [IndexError]
        matrix.matrix_operation.multiply([[170141183460469231731687303715884105727, 170141183460469231731687303715884105471], [0, -170141183460469231731687303715884105728]], [])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation.identity
    
    # region FUZZER
    
    def test_identity(self):
        """
        n = -134217729 (mutated from -1)
        """
        actual = matrix.matrix_operation.identity(-134217729)
        
        self.assertEqual([], actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_identity_with_exception(self):
        """
        n = 170141183460469231731687303715882008575 (mutated from max)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.matrix_operation.identity(170141183460469231731687303715882008575)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation.minor
    
    # region FUZZER
    
    def test_minor(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        row = zero (mutated from min)
        column = 2 (mutated from positive)
        """
        actual = matrix.matrix_operation.minor([[]], 0, 2)
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation.determinant
    
    # region FUZZER
    
    def test_determinant(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation.determinant([[0, -170141183460469231731687303715884105728, 0], [0, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [0, 0, -170141183460469231731687303715884105728]])
        
        self.assertEqual(0, actual)
    
    def test_determinant1(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation.determinant([[], [1, -170141183460469231731687303715884105727, 664613997892457936451903530140172289], [2, 1048578, 18, 4722366482869645213698]])
        
        self.assertEqual(0, actual)
    
    def test_determinant_with_exception(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.determinant] produces [IndexError]
        matrix.matrix_operation.determinant([[]])
    
    def test_determinant_with_exception1(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.determinant] produces [IndexError]
        matrix.matrix_operation.determinant([])
    
    def test_determinant_with_exception2(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.determinant] produces [IndexError]
        matrix.matrix_operation.determinant([[2, 1048578, 18, 4722366482869645213698], [1, -170141183460469231731687303715884105727, 664613997892457936451903530140172289], []])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation.inverse
    
    # region FUZZER
    
    def test_inverse(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation.inverse([[-1, 170141183460469231731687303715884105727, -1], [-1, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [-1, -1, 170141183460469231731687303715884105727]])
        
        self.assertEqual([[-1.0, 1.0, -1.0], [-0.0, 5.877471754111438e-39, -5.877471754111438e-39], [-5.877471754111438e-39, 5.877471754111438e-39, -0.0]], actual)
    
    def test_inverse1(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation.inverse([[0, -170141183460469231731687303715884105728, 664613997892457936451903530140172288], [], [1, 1048577, 17, 4722366482869645213697]])
        
        self.assertEqual(None, actual)
    
    def test_inverse_with_exception(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.inverse] produces [IndexError]
        matrix.matrix_operation.inverse([[]])
    
    def test_inverse_with_exception1(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation.inverse] produces [IndexError]
        matrix.matrix_operation.inverse([[170141183460469231731687303715884105727]])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation._check_not_integer
    
    # region FUZZER
    
    def test__check_not_integer(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation._check_not_integer([[]])
        
        self.assertEqual(True, actual)
    
    def test__check_not_integer_with_exception(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation._check_not_integer] produces [IndexError]
        matrix.matrix_operation._check_not_integer([])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation._shape
    
    # region FUZZER
    
    def test__shape(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation._shape([[]])
        
        self.assertEqual((1, 0), actual)
    
    def test__shape_with_exception(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation._shape] produces [IndexError]
        matrix.matrix_operation._shape([])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation._verify_matrix_sizes
    
    # region FUZZER
    
    def test__verify_matrix_sizes(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.matrix_operation._verify_matrix_sizes([[-1]], [[0]])
        
        self.assertEqual(((1, 1), (1, 1)), actual)
    
    def test__verify_matrix_sizes_with_exception(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation._verify_matrix_sizes] produces [ValueError]
        matrix.matrix_operation._verify_matrix_sizes([[]], [[0, 0, 4], [0, 0, 4], [0, 0, 4]])
    
    def test__verify_matrix_sizes_with_exception1(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.matrix_operation._verify_matrix_sizes] produces [IndexError]
        matrix.matrix_operation._verify_matrix_sizes([[4, 260], [0, -170141183460469231731687303715884105728]], [])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_operation.main
    
    # region FUZZER
    
    def test_main(self):
        actual = matrix.matrix_operation.main()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

