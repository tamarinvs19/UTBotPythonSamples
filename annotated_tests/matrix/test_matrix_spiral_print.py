import sys
sys.path.append(r'../../..')
import builtins
import types
import matrix
import unittest
import matrix.spiral_print


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.spiral_print.check_matrix
    
    # region FUZZER
    
    def test_check_matrix(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.spiral_print.check_matrix([[]])
        
        self.assertEqual(True, actual)
    
    def test_check_matrix1(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.spiral_print.check_matrix([[1, -170141183460469231731687303715884105727, 1], [1, -170141183460469231731687303715884105727, -170141183460469231731687303715884105727], [1, 1, -170141183460469231731687303715884105727]])
        
        self.assertEqual(True, actual)
    
    def test_check_matrix2(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.spiral_print.check_matrix([])
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.spiral_print.spiral_print_clockwise
    
    # region FUZZER
    
    def test_spiral_print_clockwise(self):
        """
        a = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.spiral_print.spiral_print_clockwise([[]])
        
        self.assertEqual(None, actual)
    
    def test_spiral_print_clockwise1(self):
        """
        a = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.spiral_print.spiral_print_clockwise([[0, -170141183460469231731687303715884105728, 0], [0, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [0, 0, -170141183460469231731687303715884105728]])
        
        self.assertEqual(None, actual)
    
    def test_spiral_print_clockwise2(self):
        """
        a = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.spiral_print.spiral_print_clockwise([[-170141183460469231731687303715884105728, 0, -169476569462576773795235400185743933440], [], [-2, -1048578, -18, -4722366482869645213698]])
        
        self.assertEqual(None, actual)
    
    def test_spiral_print_clockwise3(self):
        """
        a = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.spiral_print.spiral_print_clockwise([[170141183460469231731687303715884105727], [170141183460469231731687303715884105727], [170141183460469231731687303715884105727]])
        
        self.assertEqual(None, actual)
    
    def test_spiral_print_clockwise_with_exception(self):
        """
        a = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.spiral_print.spiral_print_clockwise] produces [IndexError]
        matrix.spiral_print.spiral_print_clockwise([[170141183460469231731687303715884105727, 170141183460469231731687303715884105725], [170141183460469231731687303715884105727, 170141183460469231731687303715884105725], [170141183460469231727075617697456717823, 170141183460469231731687303715884105725], [170141183460469231731687303715884105727, 170141183460469231731687303715884105725]])
    
    def test_spiral_print_clockwise_with_exception1(self):
        """
        a = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.spiral_print.spiral_print_clockwise] produces [IndexError]
        matrix.spiral_print.spiral_print_clockwise([[1], [1], [1], [1], [17]])
    
    def test_spiral_print_clockwise_with_exception2(self):
        """
        a = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.spiral_print.spiral_print_clockwise] produces [IndexError]
        matrix.spiral_print.spiral_print_clockwise([[], [], [], [], []])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.spiral_print.spiral_traversal
    
    # region FUZZER
    
    def test_spiral_traversal(self):
        """
        matrix = builtins.list[builtins.list[typing.Any]]
        """
        matrix1 = [[]]
        
        actual = matrix.spiral_print.spiral_traversal(matrix1)
        
        self.assertEqual([], actual)
        
        self.assertEqual([], matrix1)
    
    def test_spiral_traversal1(self):
        """
        matrix = builtins.list[builtins.list[typing.Any]]
        """
        actual = matrix.spiral_print.spiral_traversal([])
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion

