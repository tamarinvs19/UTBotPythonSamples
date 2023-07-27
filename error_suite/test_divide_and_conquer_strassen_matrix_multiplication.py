import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import divide_and_conquer
import unittest
import divide_and_conquer.strassen_matrix_multiplication


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable divide_and_conquer.strassen_matrix_multiplication.default_matrix_multiplication
    
    # region FUZZER
    
    def test_default_matrix_multiplication_with_exception(self):
        """
        a = builtins.list[typing.Any]
        b = builtins.list[typing.Any]
        """
        # This test fails because function [divide_and_conquer.strassen_matrix_multiplication.default_matrix_multiplication] produces [Exception]
        divide_and_conquer.strassen_matrix_multiplication.default_matrix_multiplication([], [])
    # endregion
    
    # endregion
    
    # region Test suites for executable divide_and_conquer.strassen_matrix_multiplication.matrix_addition
    
    # region FUZZER
    
    def test_matrix_addition(self):
        """
        matrix_a = builtins.list[typing.Any]
        matrix_b = builtins.list[typing.Any]
        """
        actual = divide_and_conquer.strassen_matrix_multiplication.matrix_addition([], [])
        
        self.assertEqual([], actual)
    
    def test_matrix_addition1(self):
        """
        matrix_a = builtins.list[builtins.list[typing.Any]]
        matrix_b = builtins.list[builtins.list[typing.Any]]
        """
        actual = divide_and_conquer.strassen_matrix_multiplication.matrix_addition([[], [], [], []], [[], [], [], []])
        
        self.assertEqual([[], [], [], []], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable divide_and_conquer.strassen_matrix_multiplication.matrix_subtraction
    
    # region FUZZER
    
    def test_matrix_subtraction(self):
        """
        matrix_a = builtins.list[typing.Any]
        matrix_b = builtins.list[typing.Any]
        """
        actual = divide_and_conquer.strassen_matrix_multiplication.matrix_subtraction([], [])
        
        self.assertEqual([], actual)
    
    def test_matrix_subtraction1(self):
        """
        matrix_a = builtins.list[builtins.list[typing.Any]]
        matrix_b = builtins.list[builtins.list[typing.Any]]
        """
        actual = divide_and_conquer.strassen_matrix_multiplication.matrix_subtraction([[], [], [], []], [[], [], [], []])
        
        self.assertEqual([[], [], [], []], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable divide_and_conquer.strassen_matrix_multiplication.split_matrix
    
    # region FUZZER
    
    def test_split_matrix_with_exception(self):
        """
        a = builtins.list[typing.Any]
        """
        # This test fails because function [divide_and_conquer.strassen_matrix_multiplication.split_matrix] produces [IndexError]
        divide_and_conquer.strassen_matrix_multiplication.split_matrix([])
    
    def test_split_matrix_with_exception1(self):
        """
        a = builtins.list[builtins.int]
        """
        # This test fails because function [divide_and_conquer.strassen_matrix_multiplication.split_matrix] produces [Exception]
        divide_and_conquer.strassen_matrix_multiplication.split_matrix([-1, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 170141183460469231731687303715884105727])
    # endregion
    
    # endregion
    
    # region Test suites for executable divide_and_conquer.strassen_matrix_multiplication.matrix_dimensions
    
    # region FUZZER
    
    def test_matrix_dimensions(self):
        """
        matrix = builtins.list[builtins.list[typing.Any]]
        """
        actual = divide_and_conquer.strassen_matrix_multiplication.matrix_dimensions([[], [], [], []])
        
        self.assertEqual((4, 0), actual)
    
    def test_matrix_dimensions_with_exception(self):
        """
        matrix = builtins.list[typing.Any]
        """
        # This test fails because function [divide_and_conquer.strassen_matrix_multiplication.matrix_dimensions] produces [IndexError]
        divide_and_conquer.strassen_matrix_multiplication.matrix_dimensions([])
    # endregion
    
    # endregion
    
    # region Test suites for executable divide_and_conquer.strassen_matrix_multiplication.print_matrix
    
    # region FUZZER
    
    def test_print_matrix(self):
        """
        matrix = builtins.list[typing.Any]
        """
        actual = divide_and_conquer.strassen_matrix_multiplication.print_matrix([])
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable divide_and_conquer.strassen_matrix_multiplication.actual_strassen
    
    # region FUZZER
    
    def test_actual_strassen_with_exception(self):
        """
        matrix_a = builtins.list[typing.Any]
        matrix_b = builtins.list[typing.Any]
        """
        # This test fails because function [divide_and_conquer.strassen_matrix_multiplication.actual_strassen] produces [IndexError]
        divide_and_conquer.strassen_matrix_multiplication.actual_strassen([], [])
    # endregion
    
    # endregion
    
    # region Test suites for executable divide_and_conquer.strassen_matrix_multiplication.strassen
    
    # region FUZZER
    
    def test_strassen_with_exception(self):
        """
        matrix1 = builtins.list[typing.Any]
        matrix2 = builtins.list[typing.Any]
        """
        # This test fails because function [divide_and_conquer.strassen_matrix_multiplication.strassen] produces [IndexError]
        divide_and_conquer.strassen_matrix_multiplication.strassen([], [])
    # endregion
    
    # endregion

