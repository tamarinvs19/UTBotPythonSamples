import sys
sys.path.append(r'..\..\..')
import builtins
import matrix
import unittest
import matrix.largest_square_area_in_matrix


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch
    
    # region FUZZER
    
    def test_largest_square_area_in_matrix_top_down_approch(self):
        """
        rows = 77371252455336267181195264 (mutated from zero)
        cols = zero
        mat = builtins.list[typing.Any]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(77371252455336267181195264, 0, [])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_top_down_approch_with_exception(self):
        """
        rows = max
        cols = 170141183460469231731687303715884105663 (mutated from max)
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch] produces [RecursionError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(170141183460469231731687303715884105727, 170141183460469231731687303715884105663, [])
    
    def test_largest_square_area_in_matrix_top_down_approch_with_exception1(self):
        """
        rows = 170141183460469231731687303715883843583 (mutated from max)
        cols = positive (mutated from zero)
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch] produces [RecursionError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(170141183460469231731687303715883843583, 1, [])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp
    
    # region FUZZER
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp(self):
        """
        rows = -77371252455336267181195265 (mutated from -1)
        cols = positive (mutated from zero)
        mat = builtins.list[typing.Any]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(-77371252455336267181195265, 1, [])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp_with_exception(self):
        """
        rows = max
        cols = 170141183460469231731687268531512016895 (mutated from max)
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp] produces [OverflowError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(170141183460469231731687303715884105727, 170141183460469231731687268531512016895, [])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_top_down_approch_with_dp_with_exception1(self):
        """
        rows = 39614081257132168796771975170 (mutated from 2)
        cols = 2 (mutated from positive)
        mat = builtins.list[typing.Any]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(39614081257132168796771975170, 2, [])
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp_with_exception2(self):
        """
        rows = positive (mutated from zero)
        cols = 2 (mutated from positive)
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp] produces [IndexError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(1, 2, [])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up
    
    # region FUZZER
    
    def test_largest_square_area_in_matrix_bottom_up(self):
        """
        rows = -77371252455336267181195265 (mutated from -1)
        cols = positive (mutated from zero)
        mat = builtins.list[typing.Any]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(-77371252455336267181195265, 1, [])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_bottom_up_with_exception(self):
        """
        rows = zero
        cols = max
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up] produces [OverflowError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(0, 170141183460469231731687303715884105727, [])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_bottom_up_with_exception1(self):
        """
        rows = 262145 (mutated from positive)
        cols = zero
        mat = builtins.list[typing.Any]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(262145, 0, [])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_bottom_up_with_exception2(self):
        """
        rows = 39614081257132168796771975170 (mutated from 2)
        cols = 2 (mutated from positive)
        mat = builtins.list[typing.Any]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(39614081257132168796771975170, 2, [])
    
    def test_largest_square_area_in_matrix_bottom_up_with_exception3(self):
        """
        rows = positive (mutated from zero)
        cols = 2 (mutated from positive)
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up] produces [IndexError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(1, 2, [])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization
    
    # region FUZZER
    
    def test_largest_square_area_in_matrix_bottom_up_space_optimization(self):
        """
        rows = -77371252455336267181195265 (mutated from -1)
        cols = positive (mutated from zero)
        mat = builtins.list[typing.Any]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(-77371252455336267181195265, 1, [])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_bottom_up_space_optimization1(self):
        """
        rows = positive (mutated from zero)
        cols = -2097153 (mutated from -1)
        mat = builtins.list[typing.Any]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(1, -2097153, [])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_bottom_up_space_optimization_with_exception(self):
        """
        rows = min
        cols = min (mutated from zero)
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization] produces [OverflowError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(-170141183460469231731687303715884105728, -170141183460469231731687303715884105728, [])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_bottom_up_space_optimization_with_exception1(self):
        """
        rows = 262145 (mutated from positive)
        cols = zero
        mat = builtins.list[typing.Any]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(262145, 0, [])
    
    def test_largest_square_area_in_matrix_bottom_up_space_optimization_with_exception2(self):
        """
        rows = 39614081257132168796771975170 (mutated from 2)
        cols = 2 (mutated from positive)
        mat = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization] produces [IndexError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(39614081257132168796771975170, 2, [])
    # endregion
    
    # endregion

