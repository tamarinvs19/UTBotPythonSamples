import sys
sys.path.append(r'../../..')
import builtins
import types
import matrix
import unittest
import matrix.pascal_triangle


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.pascal_triangle.print_pascal_triangle
    
    # region FUZZER
    
    def test_print_pascal_triangle(self):
        """
        num_rows = 8 (mutated from -170141183460469231731687303715884105720)
        """
        actual = matrix.pascal_triangle.print_pascal_triangle(8)
        
        self.assertEqual(None, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_print_pascal_triangle_with_exception(self):
        """
        num_rows = 2097153 (mutated from positive)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.pascal_triangle.print_pascal_triangle(2097153)
    
    def test_print_pascal_triangle_with_exception1(self):
        """
        num_rows = -19342813113834066795298817 (mutated from -1)
        """
        # This test fails because function [matrix.pascal_triangle.print_pascal_triangle] produces [ValueError]
        matrix.pascal_triangle.print_pascal_triangle(-19342813113834066795298817)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.pascal_triangle.generate_pascal_triangle
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_generate_pascal_triangle_with_exception(self):
        """
        num_rows = 170141183460469231731687303715882008575 (mutated from max)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.pascal_triangle.generate_pascal_triangle(170141183460469231731687303715882008575)
    
    def test_generate_pascal_triangle_with_exception1(self):
        """
        num_rows = -134217729 (mutated from -1)
        """
        # This test fails because function [matrix.pascal_triangle.generate_pascal_triangle] produces [ValueError]
        matrix.pascal_triangle.generate_pascal_triangle(-134217729)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.pascal_triangle.populate_current_row
    
    # region FUZZER
    
    def test_populate_current_row(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row_idx = positive
        """
        actual = matrix.pascal_triangle.populate_current_row([[1], [-170141183460469231731687303715884105727], [1], [-170141183460469231731687303715884105727], [1]], 1)
        
        self.assertEqual([1, 1], actual)
    
    def test_populate_current_row_with_exception(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row_idx = -1 (mutated from max)
        """
        # This test fails because function [matrix.pascal_triangle.populate_current_row] produces [IndexError]
        matrix.pascal_triangle.populate_current_row([[]], -1)
    
    def test_populate_current_row_with_exception1(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row_idx = max (mutated from -1)
        """
        # This test fails because function [matrix.pascal_triangle.populate_current_row] produces [OverflowError]
        matrix.pascal_triangle.populate_current_row([[]], 170141183460469231731687303715884105727)
    
    def test_populate_current_row_with_exception2(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row_idx = 1048577 (mutated from positive)
        """
        # This test fails because function [matrix.pascal_triangle.populate_current_row] produces [IndexError]
        matrix.pascal_triangle.populate_current_row([[-170141183460469231731687303715884105727], [1], [1], [1], [-170141183460469231731687303715884105727]], 1048577)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_populate_current_row_with_exception3(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row_idx = 536870913 (mutated from positive)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.pascal_triangle.populate_current_row([[170141183460469231731687303715884105727, -2, -2, 0], [-1, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728, 0], [2, 170141183460469231731687303715884105727, -2, -170141183460469231731687303715884105728], [2, -170141183460469231731687303715884105726, 576460752303423490, 268435458]], 536870913)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_populate_current_row_with_exception4(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row_idx = 135528448 (mutated from 135528449)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.pascal_triangle.populate_current_row([[-170141183460469231731687303715884105727], [1], [1], [1], [-170141183460469231731687303715884105727]], 135528448)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.pascal_triangle.calculate_current_element
    
    # region FUZZER
    
    def test_calculate_current_element(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row = builtins.list[builtins.int]
        current_row_idx = -1
        current_col_idx = -1
        """
        current_row = [2]
        
        actual = matrix.pascal_triangle.calculate_current_element([[2, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 2], [2, 2, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-170141183460469231731687303715884105728, 2, -170141183460469231731687303715884105728, 2], [2, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 2]], current_row, -1, -1)
        
        self.assertEqual(None, actual)
        
        self.assertEqual([-170141183460469231731687303715884105726], current_row)
    
    def test_calculate_current_element_with_exception(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row = builtins.list[builtins.int]
        current_row_idx = 2 (mutated from positive)
        current_col_idx = max (mutated from -1)
        """
        # This test fails because function [matrix.pascal_triangle.calculate_current_element] produces [IndexError]
        matrix.pascal_triangle.calculate_current_element([[]], [1, -170141183460469231731687303715884105727, 20769187434139310514121985316880385], 2, 170141183460469231731687303715884105727)
    
    def test_calculate_current_element_with_exception1(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row = builtins.list[builtins.int]
        current_row_idx = zero (mutated from positive)
        current_col_idx = positive
        """
        # This test fails because function [matrix.pascal_triangle.calculate_current_element] produces [IndexError]
        matrix.pascal_triangle.calculate_current_element([[70368744177665, 1, 8796093022209], [1, 8796093022209, 70368744177665], [8796093022209, 70368744177665, 1]], [], 0, 1)
    
    def test_calculate_current_element_with_exception2(self):
        """
        triangle = builtins.list[builtins.list[builtins.int]]
        current_row = builtins.list[builtins.int]
        current_row_idx = zero (mutated from positive)
        current_col_idx = positive
        """
        # This test fails because function [matrix.pascal_triangle.calculate_current_element] produces [IndexError]
        matrix.pascal_triangle.calculate_current_element([[-170141183460469231731687303715884105727]], [1, 1, 0, 1], 0, 1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.pascal_triangle.generate_pascal_triangle_optimized
    
    # region FUZZER
    
    def test_generate_pascal_triangle_optimized(self):
        """
        num_rows = 9 (mutated from positive)
        """
        actual = matrix.pascal_triangle.generate_pascal_triangle_optimized(9)
        
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]], actual)
    
    def test_generate_pascal_triangle_optimized_with_exception(self):
        """
        num_rows = -2097154 (mutated from -2)
        """
        # This test fails because function [matrix.pascal_triangle.generate_pascal_triangle_optimized] produces [ValueError]
        matrix.pascal_triangle.generate_pascal_triangle_optimized(-2097154)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_generate_pascal_triangle_optimized_with_exception1(self):
        """
        num_rows = 170141183460469231731687303715882008574 (mutated from -2097154)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.pascal_triangle.generate_pascal_triangle_optimized(170141183460469231731687303715882008574)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_generate_pascal_triangle_optimized_with_exception2(self):
        """
        num_rows = 514 (mutated from 2)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.pascal_triangle.generate_pascal_triangle_optimized(514)
    # endregion
    
    # endregion

