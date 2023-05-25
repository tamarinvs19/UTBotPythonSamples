import sys
sys.path.append(r'..\..\..')
import builtins
import matrix
import unittest
import matrix.pascal_triangle


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.pascal_triangle.print_pascal_triangle
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_print_pascal_triangle_with_exception(self):
        """
        num_rows = 2097153 (mutated from positive)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.pascal_triangle.print_pascal_triangle(2097153)
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
        triangle = builtins.list[typing.Any]
        current_row_idx = zero (mutated from min)
        """
        actual = matrix.pascal_triangle.populate_current_row([], 0)
        
        self.assertEqual([1], actual)
    
    def test_populate_current_row_with_exception(self):
        """
        triangle = builtins.list[typing.Any]
        current_row_idx = -65 (mutated from -1)
        """
        # This test fails because function [matrix.pascal_triangle.populate_current_row] produces [IndexError]
        matrix.pascal_triangle.populate_current_row([], -65)
    
    def test_populate_current_row_with_exception1(self):
        """
        triangle = builtins.list[typing.Any]
        current_row_idx = 170141183460469231731687303715884105663 (mutated from -65)
        """
        # This test fails because function [matrix.pascal_triangle.populate_current_row] produces [OverflowError]
        matrix.pascal_triangle.populate_current_row([], 170141183460469231731687303715884105663)
    
    def test_populate_current_row_with_exception2(self):
        """
        triangle = builtins.list[typing.Any]
        current_row_idx = 2 (mutated from positive)
        """
        # This test fails because function [matrix.pascal_triangle.populate_current_row] produces [IndexError]
        matrix.pascal_triangle.populate_current_row([], 2)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_populate_current_row_with_exception3(self):
        """
        triangle = builtins.list[typing.Any]
        current_row_idx = 536870912 (mutated from zero)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.pascal_triangle.populate_current_row([], 536870912)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.pascal_triangle.calculate_current_element
    
    # region FUZZER
    
    def test_calculate_current_element_with_exception(self):
        """
        triangle = builtins.list[typing.Any]
        current_row = builtins.list[typing.Any]
        current_row_idx = min
        current_col_idx = 2 (mutated from positive)
        """
        # This test fails because function [matrix.pascal_triangle.calculate_current_element] produces [IndexError]
        matrix.pascal_triangle.calculate_current_element([], [], -170141183460469231731687303715884105728, 2)
    # endregion
    
    # endregion

