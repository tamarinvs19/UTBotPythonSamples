import sys
sys.path.append(r'../../..')
import builtins
import types
import matrix
import unittest
import matrix.rotate_matrix


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.rotate_matrix.make_matrix
    
    # region FUZZER
    
    def test_make_matrix(self):
        actual = matrix.rotate_matrix.make_matrix()
        
        self.assertEqual([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_make_matrix_with_exception(self):
        """
        row_size = 2097153 (mutated from positive)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.rotate_matrix.make_matrix(2097153)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.rotate_matrix.rotate_90
    
    # region FUZZER
    
    def test_rotate_90(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        matrix1 = [[]]
        
        actual = matrix.rotate_matrix.rotate_90(matrix1)
        
        self.assertEqual([], actual)
        
        self.assertEqual([], matrix1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.rotate_matrix.rotate_180
    
    # region FUZZER
    
    def test_rotate_180(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.rotate_matrix.rotate_180([[]])
        
        self.assertEqual([[]], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.rotate_matrix.rotate_270
    
    # region FUZZER
    
    def test_rotate_270(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        matrix1 = [[]]
        
        actual = matrix.rotate_matrix.rotate_270(matrix1)
        
        self.assertEqual([], actual)
        
        self.assertEqual([], matrix1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.rotate_matrix.transpose
    
    # region FUZZER
    
    def test_transpose(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        matrix1 = [[]]
        
        actual = matrix.rotate_matrix.transpose(matrix1)
        
        self.assertEqual([], actual)
        
        self.assertEqual([], matrix1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.rotate_matrix.reverse_row
    
    # region FUZZER
    
    def test_reverse_row(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.rotate_matrix.reverse_row([[]])
        
        self.assertEqual([[]], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.rotate_matrix.reverse_column
    
    # region FUZZER
    
    def test_reverse_column(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.rotate_matrix.reverse_column([[]])
        
        self.assertEqual([[]], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.rotate_matrix.print_matrix
    
    # region FUZZER
    
    def test_print_matrix(self):
        """
        matrix = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.rotate_matrix.print_matrix([[]])
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

