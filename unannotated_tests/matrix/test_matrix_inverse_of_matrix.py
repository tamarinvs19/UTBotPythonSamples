import sys
sys.path.append(r'..\..\..')
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
        actual = matrix.inverse_of_matrix.inverse_of_matrix([[2.0, 3.6893488147419103E19, 1.37438953472E11], [2.0, 3.6893488147419103E19, 8.589934592E9], [2.0, 4.9466080294620907E173, 8.589934592E9]])
        
        self.assertEqual([[-0.03333333333333333, 0.0, 7.761021455128988e-12], [0.5333333333333333, -2.0215873059760975e-174, -7.761021455128988e-12], [-3.7291703656001034e-155, 2.0215873059760975e-174, 0.0]], actual)
    
    def test_inverse_of_matrix1(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        actual = matrix.inverse_of_matrix.inverse_of_matrix([[1.0, 1.0], [1.0, -1.0]])
        
        self.assertEqual([[0.5, 0.5], [0.5, -0.5]], actual)
    
    def test_inverse_of_matrix_with_exception(self):
        """
        matrix = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([])
    
    def test_inverse_of_matrix_with_exception1(self):
        """
        matrix = builtins.list[builtins.list[typing.Any]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[], [], []])
    
    def test_inverse_of_matrix_with_exception2(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[0.0, 1.0], [0.0, 1.0]])
    
    def test_inverse_of_matrix_with_exception3(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[2.0, 6.805647338418769E38, 2.00048828125], [0.0, -1.1125369292536007E-308, 1.1125454172367646E-308, 1.1125369292536086E-308], []])
    
    def test_inverse_of_matrix_with_exception4(self):
        """
        matrix = builtins.list[builtins.list[builtins.float]]
        """
        # This test fails because function [matrix.inverse_of_matrix.inverse_of_matrix] produces [ValueError]
        matrix.inverse_of_matrix.inverse_of_matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, 0.0]])
    # endregion
    
    # endregion

