import sys
sys.path.append(r'..\..\..')
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
        matrix = builtins.list[typing.Any]
        """
        actual = matrix.spiral_print.check_matrix([])
        
        self.assertEqual(False, actual)
    
    def test_check_matrix1(self):
        """
        matrix = builtins.list[builtins.list[typing.Any]]
        """
        actual = matrix.spiral_print.check_matrix([[]])
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.spiral_print.spiral_print_clockwise
    
    # region FUZZER
    
    def test_spiral_print_clockwise(self):
        """
        a = builtins.list[typing.Any]
        """
        actual = matrix.spiral_print.spiral_print_clockwise([])
        
        self.assertEqual(None, actual)
    
    def test_spiral_print_clockwise1(self):
        """
        a = builtins.list[builtins.list[typing.Any]]
        """
        actual = matrix.spiral_print.spiral_print_clockwise([[]])
        
        self.assertEqual(None, actual)
    
    def test_spiral_print_clockwise_with_exception(self):
        """
        a = builtins.list[builtins.list[typing.Any]]
        """
        # This test fails because function [matrix.spiral_print.spiral_print_clockwise] produces [IndexError]
        matrix.spiral_print.spiral_print_clockwise([[], [], []])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.spiral_print.spiral_traversal
    
    # region FUZZER
    
    def test_spiral_traversal(self):
        """
        matrix = builtins.list[typing.Any]
        """
        actual = matrix.spiral_print.spiral_traversal([])
        
        self.assertEqual([], actual)
    
    def test_spiral_traversal1(self):
        """
        matrix = builtins.list[builtins.list[typing.Any]]
        """
        matrix1 = [[]]
        
        actual = matrix.spiral_print.spiral_traversal(matrix1)
        
        self.assertEqual([], actual)
        
        self.assertEqual([], matrix1)
    # endregion
    
    # endregion

