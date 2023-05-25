import sys
sys.path.append(r'..\..\..')
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
        matrix_a = builtins.list[typing.Any]
        matrix_b = builtins.list[typing.Any]
        """
        actual = matrix.nth_fibonacci_using_matrix_exponentiation.multiply([], [])
        
        self.assertEqual([], actual)
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

