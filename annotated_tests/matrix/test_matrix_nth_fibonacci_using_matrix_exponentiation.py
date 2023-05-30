import sys
sys.path.append(r'../../..')
import builtins
import types
import matrix
import unittest
import matrix.nth_fibonacci_using_matrix_exponentiation


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.nth_fibonacci_using_matrix_exponentiation.multiply
    
    # region FUZZER
    
    def test_multiply(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.nth_fibonacci_using_matrix_exponentiation.multiply([], [])
        
        self.assertEqual([], actual)
    
    def test_multiply1(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.nth_fibonacci_using_matrix_exponentiation.multiply([[1]], [[170141183460469231731687303715884105727, 170141183460469231731687303715615670271, -1, 170141183460469231731687303714810363903], [1, 0, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 1, -1], [-1]])
        
        self.assertEqual([[170141183460469231731687303715884105727]], actual)
    
    def test_multiply_with_exception(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.nth_fibonacci_using_matrix_exponentiation.multiply] produces [IndexError]
        matrix.nth_fibonacci_using_matrix_exponentiation.multiply([[]], [[170141183460469231731687303715884105727, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [170141183460469231731687303715884105727, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-170141183460469231731687303715884105728, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728]])
    
    def test_multiply_with_exception1(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.nth_fibonacci_using_matrix_exponentiation.multiply] produces [IndexError]
        matrix.nth_fibonacci_using_matrix_exponentiation.multiply([[0, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728, -1, 170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 167482727468899399985879689595323416575, -1], [0, 1024, 32768, 38685626227668133590597632, 9903520314283042199192993792], [-1, -131073], [0, -1, 0, 1, -170141183460469231731687303715884105728]], [[-1, 0], [1], [-1, 170141183460469231731687303715884105727, -2251799813685249, 170141183460469231731687303715884105727, -536870913], [-170141183460469231731687303715884105728, 0, 0, 0, 1], [-170141183460469231731687303715884105728, 0, 0, 0, 0]])
    
    def test_multiply_with_exception2(self):
        """
        matrix_a = builtins.list[builtins.list[builtins.int]]
        matrix_b = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.nth_fibonacci_using_matrix_exponentiation.multiply] produces [IndexError]
        matrix.nth_fibonacci_using_matrix_exponentiation.multiply([[0, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [1], [170141183460469231731687303715884105727, 0, 170141183460469231731687303715884105727, 1, 170141183460469231731687303715884105727], [-1, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, -316912650057057350374175801345, -2305843009213693953], [-1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728, -1, -170141183460469231731687303715884105728]], [[-1, -1073741825, -332306998946228968225951765070086145, -18889465931478580854785, -20769187434139310514121985316880385], [-20769187434139310514121985316880385, -18889465931478580854785, -1, -1073741825, -332306998946228968225951765070086145], [-20769187434139310514121985316880385, -18889465931478580854785, -1073741825, -332306998946228968225951765070086145, -1], [-1, -1073741825, -18889465931478580854785, -20769187434139310514121985316880385, -332306998946228968225951765070086145], [-1073741825, -332306998946228968225951765070086145, -1, -20769187434139310514121985316880385, -18889465931478580854785]])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.nth_fibonacci_using_matrix_exponentiation.identity
    
    # region FUZZER
    
    def test_identity(self):
        """
        n = -134217729 (mutated from -1)
        """
        actual = matrix.nth_fibonacci_using_matrix_exponentiation.identity(-134217729)
        
        self.assertEqual([], actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_identity_with_exception(self):
        """
        n = 170141183460469231731687303715882008575 (mutated from max)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.nth_fibonacci_using_matrix_exponentiation.identity(170141183460469231731687303715882008575)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.nth_fibonacci_using_matrix_exponentiation.nth_fibonacci_matrix
    
    # region FUZZER
    
    def test_nth_fibonacci_matrix(self):
        """
        n = -134217729 (mutated from -1)
        """
        actual = matrix.nth_fibonacci_using_matrix_exponentiation.nth_fibonacci_matrix(-134217729)
        
        self.assertEqual(-134217729, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_nth_fibonacci_matrix_with_exception(self):
        """
        n = 2097152 (mutated from zero)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.nth_fibonacci_using_matrix_exponentiation.nth_fibonacci_matrix(2097152)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_nth_fibonacci_matrix_with_exception1(self):
        """
        n = 170141183460469231731651274918730924031 (mutated from -36028797153181697)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.nth_fibonacci_using_matrix_exponentiation.nth_fibonacci_matrix(170141183460469231731651274918730924031)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.nth_fibonacci_using_matrix_exponentiation.nth_fibonacci_bruteforce
    
    # region FUZZER
    
    def test_nth_fibonacci_bruteforce(self):
        """
        n = -1 (mutated from max)
        """
        actual = matrix.nth_fibonacci_using_matrix_exponentiation.nth_fibonacci_bruteforce(-1)
        
        self.assertEqual(-1, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_nth_fibonacci_bruteforce_with_exception(self):
        """
        n = 2097152 (mutated from zero)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.nth_fibonacci_using_matrix_exponentiation.nth_fibonacci_bruteforce(2097152)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.nth_fibonacci_using_matrix_exponentiation.main
    
    # region FUZZER
    
    def test_main(self):
        actual = matrix.nth_fibonacci_using_matrix_exponentiation.main()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

