import sys
sys.path.append(r'../../..')
import builtins
import matrix
import unittest
import matrix.inverse_of_matrix


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.inverse_of_matrix.inverse_of_matrix
    
    # region FUZZER
    
    def test_inverse_of_matrix(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        actual = matrix.inverse_of_matrix.inverse_of_matrix([[1.0, 1.0], [1.0, -1.0]])
        
        self.assertEqual([[0.5, 0.5], [0.5, -0.5]], actual)
    
    def test_inverse_of_matrix1(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        actual = matrix.inverse_of_matrix.inverse_of_matrix([[3.0, -3.0, 3.001953125], [0.0, -1.1125369292536007E-308, -1.1125369292536007E-308], [0.0, 1.0, 2.0]])
        
        self.assertEqual([[0.3333333333333333, 0.0, 0.0], [float('-inf'), float('-inf'), 8.98846567431158e+307], [-2.0006510416666665, -1.0, 1.0]], actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_inverse_of_matrix_with_exception(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.inverse_of_matrix.inverse_of_matrix([[]])
    
    def test_inverse_of_matrix_with_exception1(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[1.0]])
    
    def test_inverse_of_matrix_with_exception2(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[0.0, 2.0], [0.0, 1.113080160176088E-308]])
    
    def test_inverse_of_matrix_with_exception3(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[0.0, 1.113080160176088E-308], [0.0, 2.0]])
    
    def test_inverse_of_matrix_with_exception4(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [0.0, 0.0, -1.0]])
    
    def test_inverse_of_matrix_with_exception5(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[2.0, 2.125], [float('inf'), 1.0, -1.1125369292536007E-308], [1.0, 0.0, 1.0]])
    
    def test_inverse_of_matrix_with_exception6(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[1.0, float('inf'), -2.2250738585072014E-308], [1.0, 7.2911220195563975E-304, 1.0], [2.125, 2.0]])
    
    def test_inverse_of_matrix_with_exception7(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [decimal.InvalidOperation]
        matrix.inverse_of_matrix.inverse_of_matrix([[float('-inf'), float('-inf'), float('-inf')], [1.0, 1.0000000000000004, 1.03125], [1.0, 0.0, 2.0]])
    
    def test_inverse_of_matrix_with_exception8(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [decimal.InvalidOperation]
        matrix.inverse_of_matrix.inverse_of_matrix([[1.0, 1.0000000000000004, 1.03125], [float('-inf'), float('-inf'), float('-inf')], [1.0, 0.0, 2.0]])
    
    def test_inverse_of_matrix_with_exception9(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[2.0, 0.0, 1.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]])
    
    def test_inverse_of_matrix_with_exception10(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [decimal.InvalidOperation]
        matrix.inverse_of_matrix.inverse_of_matrix([[float('inf'), float('inf')], [float('inf'), float('inf')]])
    
    def test_inverse_of_matrix_with_exception11(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [decimal.InvalidOperation]
        matrix.inverse_of_matrix.inverse_of_matrix([[-2.0, 0.0, -1.0], [2.0, 3.0, float('-inf')], [2.0, 2.5, 2.0000000000000036]])
    
    def test_inverse_of_matrix_with_exception12(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[]])
    
    def test_inverse_of_matrix_with_exception13(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [decimal.InvalidOperation]
        matrix.inverse_of_matrix.inverse_of_matrix([[-2.0, 0.0, -1.0], [2.0, 3.0, float('-inf')], [2.315841784746324E77, 2.0000000000000036, 2.5]])
    # endregion
    
    # endregion

