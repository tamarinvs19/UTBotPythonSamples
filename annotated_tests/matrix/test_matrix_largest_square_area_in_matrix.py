import sys
sys.path.append(r'../../..')
import builtins
import matrix
import unittest
import matrix.largest_square_area_in_matrix


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch
    
    # region FUZZER
    
    def test_largest_square_area_in_matrix_top_down_approch(self):
        """
        rows = min (mutated from zero)
        cols = zero
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(-170141183460469231731687303715884105728, 0, [[1, 0, 170141183460469231731687303715884105727, -1, -1], [-170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 170141183460469231731687303715884105727], [1, -170141183460469231731687303715884105727, 1025]])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_top_down_approch1(self):
        """
        rows = 2 (mutated from positive)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(2, 1, [[0, 0, 0, -170141183460469231731687303715884105728, -1], [1, 8589934593, 8388609, 8796093022209, -170141183460469231731687303715884105727], [0, 2, 170141183460469231731687303715884105727, -1, 170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 170141183460469231731687303715884105471, -1, 170141183460449888918573469649088806911, 170141183460469156173823577801560686591], [-170141183460469231731687303715884105728, -170141183460469231731686740765930684416, 0, -170141183460469231731687303715884105726, -170141183455517471574545782616287608832]])
        
        self.assertEqual(1, actual)
    
    def test_largest_square_area_in_matrix_top_down_approch2(self):
        """
        rows = 2 (mutated from positive)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(2, 1, [[1, 8589934593, 8388609, 8796093022209, -170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 170141183460469231731687303715884105471, -1, 170141183460449888918573469649088806911, 170141183460469156173823577801560686591], [-170141183460469231731687303715884105728, -170141183460469231731686740765930684416, 0, -170141183460469231731687303715884105726, -170141183455517471574545782616287608832], [0, 0, 0, -170141183460469231731687303715884105728, -1], [0, 2, 170141183460469231731687303715884105727, -1, 170141183460469231731687303715884105727]])
        
        self.assertEqual(1, actual)
    
    def test_largest_square_area_in_matrix_top_down_approch3(self):
        """
        rows = 2 (mutated from positive)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(2, 1, [[0, 2, 170141183460469231731687303715884105727, -1, 170141183460469231731687303715884105727], [0, 0, 0, -170141183460469231731687303715884105728, -1], [1, 8589934593, 8388609, 8796093022209, -170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 170141183460469231731687303715884105471, -1, 170141183460449888918573469649088806911, 170141183460469156173823577801560686591], [-170141183460469231731687303715884105728, -170141183460469231731686740765930684416, 0, -170141183460469231731687303715884105726, -170141183455517471574545782616287608832]])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_top_down_approch_with_exception(self):
        """
        rows = 2 (mutated from positive)
        cols = max
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch] produces [RecursionError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(2, 170141183460469231731687303715884105727, [[1, -170141183460469231731687303715884105728, 2, 1, 0], [2, 2535301200456458802993406410754, 65538, -170141183460469231731687303715884105726, 324518553658426726783156020576258], [1, 158456325028528675187087900673, 4722366482869645213697, 1152921504606846977, 65537], [1, 562949953421313, -170141183460469231731687303715884105727, -170141183460469231731687303715884105727, -170141183460469231731687303715884105727], [-170141183460469231731687303715884105728, -170141178389866830818769697729071284224, -170141178389866830818769697729071284224, 0, 0]])
    
    def test_largest_square_area_in_matrix_top_down_approch_with_exception1(self):
        """
        rows = 536870914 (mutated from 2)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch] produces [RecursionError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(536870914, 1, [[0, 0, 0, -170141183460469231731687303715884105728, -1], [1, 8589934593, 8388609, 8796093022209, -170141183460469231731687303715884105727], [0, 2, 170141183460469231731687303715884105727, -1, 170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 170141183460469231731687303715884105471, -1, 170141183460449888918573469649088806911, 170141183460469156173823577801560686591], [-170141183460469231731687303715884105728, -170141183460469231731686740765930684416, 0, -170141183460469231731687303715884105726, -170141183455517471574545782616287608832]])
    
    def test_largest_square_area_in_matrix_top_down_approch_with_exception2(self):
        """
        rows = 2 (mutated from positive)
        cols = 257 (mutated from positive)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch] produces [IndexError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch(2, 257, [[0, 0, 0, -170141183460469231731687303715884105728, -1], [1, 8589934593, 8388609, 8796093022209, -170141183460469231731687303715884105727], [0, 2, 170141183460469231731687303715884105727, -1, 170141183460469231731687303715884105727], [170141183460469231731687303715884105727, 170141183460469231731687303715884105471, -1, 170141183460449888918573469649088806911, 170141183460469156173823577801560686591], [-170141183460469231731687303715884105728, -170141183460469231731686740765930684416, 0, -170141183460469231731687303715884105726, -170141183455517471574545782616287608832]])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp
    
    # region FUZZER
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp(self):
        """
        rows = -2 (mutated from -1)
        cols = -2 (mutated from -1)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(-2, -2, [[1, 170141183460469231731687303715884105727, 2], [0, 0, -170141183460469231731687303715884105728], [2, 4398046511106, 130, 37778931862957161709570, 158456325028528675187087900674]])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp1(self):
        """
        rows = positive (mutated from zero)
        cols = 2 (mutated from positive)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(1, 2, [[-1, 0, -1, -170141183460469231731687303715884105728, -1], [-1, -170141183460469231731687303715884105728, -1, 0, -1], [-1, -1, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-1, -1, -1, 0, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728, 0, -1]])
        
        self.assertEqual(1, actual)
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp2(self):
        """
        rows = positive (mutated from zero)
        cols = 2 (mutated from positive)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(1, 2, [[-1, -1, -1, 0, -170141183460469231731687303715884105728], [-1, -1, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728, 0, -1], [-1, 0, -1, -170141183460469231731687303715884105728, -1], [-1, -170141183460469231731687303715884105728, -1, 0, -1]])
        
        self.assertEqual(1, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_top_down_approch_with_dp_with_exception(self):
        """
        rows = max (mutated from -1)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(170141183460469231731687303715884105727, 1, [[2, -1, -170141183460469231731687303715884105728, 0, -170141183460469231731687303715884105728], [170141183460469231731687303715884105727, -1, 1], [-2, 170141183460469231731687303715884105726, -1026]])
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp_with_exception1(self):
        """
        rows = positive (mutated from zero)
        cols = 170141183460469231731687303715867328511 (mutated from -16777217)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp] produces [OverflowError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(1, 170141183460469231731687303715867328511, [[170141183460469231731687303715884105727, 170141180925168031275228500722477694975], [170141180925168031275228500722477694975, 170141183460469231731687303715884105727]])
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp_with_exception2(self):
        """
        rows = 34 (mutated from 2)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp] produces [IndexError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(34, 1, [[-2, 170141183460469231731687303715884105726, 170141183460469231731687303715884105726, -2097154, 170141183460469231731687303715884105726], [170141183460469231731687303715884105726, 170141183460469231731687303715884105726, -2097154, 170141183460469231731687303715884105726, -2], [170141183460469231731687303715884105726, -2, 170141183460469231731687303715884105726, -2097154, 170141183460469231731687303715884105726], [170141183460469231731687303715884105726, 170141183460469231731687303715884105726, -2, 170141183460469231731687303715884105726, -2097154], [-2, 170141183460469231731687303715884105726, 170141183460469231731687303715884105726, -2097154, 170141183460469231731687303715884105726]])
    
    def test_largest_square_area_in_matrix_top_down_approch_with_dp_with_exception3(self):
        """
        rows = 32769 (mutated from positive)
        cols = 3 (mutated from 2)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp] produces [RecursionError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(32769, 3, [[-1, -1, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-1, -1, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728, 0, -1], [-1, 0, -1, -170141183460469231731687303715884105728, -1], [-1, -170141183460469231731687303715884105728, -1, 0, -1]])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_top_down_approch_with_dp_with_exception4(self):
        """
        rows = 134250497 (mutated from 32769)
        cols = 3 (mutated from 2)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_top_down_approch_with_dp(134250497, 3, [[-1, -1, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-1, -1, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728, 0, -1], [-1, 0, -1, -170141183460469231731687303715884105728, -1], [-1, -170141183460469231731687303715884105728, -1, 0, -1]])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up
    
    # region FUZZER
    
    def test_largest_square_area_in_matrix_bottom_up(self):
        """
        rows = -2 (mutated from -1)
        cols = -2 (mutated from -1)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(-2, -2, [[1, 170141183460469231731687303715884105727, 2], [0, 0, -170141183460469231731687303715884105728], [2, 4398046511106, 130, 37778931862957161709570, 158456325028528675187087900674]])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_bottom_up1(self):
        """
        rows = positive (mutated from zero)
        cols = -16777217 (mutated from -1)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(1, -16777217, [[170141183460469231731687303715884105727, 170141180925168031275228500722477694975], [170141180925168031275228500722477694975, 170141183460469231731687303715884105727]])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_bottom_up2(self):
        """
        rows = positive (mutated from zero)
        cols = 2 (mutated from positive)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(1, 2, [[-1, 0, -1, -170141183460469231731687303715884105728, -1], [-1, -170141183460469231731687303715884105728, -1, 0, -1], [-1, -1, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [-1, -1, -1, 0, -170141183460469231731687303715884105728], [-1, -1, -170141183460469231731687303715884105728, 0, -1]])
        
        self.assertEqual(0, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_bottom_up_with_exception(self):
        """
        rows = max (mutated from -1)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(170141183460469231731687303715884105727, 1, [[2, -1, -170141183460469231731687303715884105728, 0, -170141183460469231731687303715884105728], [170141183460469231731687303715884105727, -1, 1], [-2, 170141183460469231731687303715884105726, -1026]])
    
    def test_largest_square_area_in_matrix_bottom_up_with_exception1(self):
        """
        rows = positive (mutated from zero)
        cols = 170141183460469231731687303715867328511 (mutated from -16777217)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up] produces [OverflowError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(1, 170141183460469231731687303715867328511, [[170141183460469231731687303715884105727, 170141180925168031275228500722477694975], [170141180925168031275228500722477694975, 170141183460469231731687303715884105727]])
    
    def test_largest_square_area_in_matrix_bottom_up_with_exception2(self):
        """
        rows = 34 (mutated from 2)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up] produces [IndexError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up(34, 1, [[-2, 170141183460469231731687303715884105726, 170141183460469231731687303715884105726, -2097154, 170141183460469231731687303715884105726], [170141183460469231731687303715884105726, 170141183460469231731687303715884105726, -2097154, 170141183460469231731687303715884105726, -2], [170141183460469231731687303715884105726, -2, 170141183460469231731687303715884105726, -2097154, 170141183460469231731687303715884105726], [170141183460469231731687303715884105726, 170141183460469231731687303715884105726, -2, 170141183460469231731687303715884105726, -2097154], [-2, 170141183460469231731687303715884105726, 170141183460469231731687303715884105726, -2097154, 170141183460469231731687303715884105726]])
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization
    
    # region FUZZER
    
    def test_largest_square_area_in_matrix_bottom_up_space_optimization(self):
        """
        rows = 2 (mutated from positive)
        cols = zero
        mat = builtins.list[builtins.list[builtins.int]]
        """
        actual = matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(2, 0, [])
        
        self.assertEqual(0, actual)
    
    def test_largest_square_area_in_matrix_bottom_up_space_optimization_with_exception(self):
        """
        rows = max (mutated from -1)
        cols = positive (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization] produces [IndexError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(170141183460469231731687303715884105727, 1, [[2, -1, -170141183460469231731687303715884105728, 0, -170141183460469231731687303715884105728], [170141183460469231731687303715884105727, -1, 1], [-2, 170141183460469231731687303715884105726, -1026]])
    
    def test_largest_square_area_in_matrix_bottom_up_space_optimization_with_exception1(self):
        """
        rows = max
        cols = min
        mat = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization] produces [OverflowError]
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(170141183460469231731687303715884105727, -170141183460469231731687303715884105728, [[-2, -1, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728], [170141183460469231731687303715884105727, 170141180925168031275228500722477694975, 170141183460469231731687303715884040191, -1, 170140858941915573304960520559863529471], [2, 158456325028528675187087900674, 4722366482869645213698, 1152921504606846978, 65538], [2, 562949953421314, -170141183460469231731687303715884105726, -170141183460469231731687303715884105726, -170141183460469231731687303715884105726], [2, 5070602400912917605986812821506, 5070602400912917605986812821506, -170141183460469231731687303715884105726, -170141183460469231731687303715884105726]])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_bottom_up_space_optimization_with_exception2(self):
        """
        rows = 4194306 (mutated from 2)
        cols = -1 (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(4194306, -1, [[0, 562949953421312], [0, 324518553658426726783156020576256]])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_bottom_up_space_optimization_with_exception3(self):
        """
        rows = 65538 (mutated from 2)
        cols = min (mutated from zero)
        mat = builtins.list[builtins.list[builtins.int]]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(65538, -170141183460469231731687303715884105728, [])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_largest_square_area_in_matrix_bottom_up_space_optimization_with_exception4(self):
        """
        rows = -170141183460469231731687303715884040190 (mutated from 65538)
        cols = zero
        mat = builtins.list[builtins.list[builtins.int]]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix.largest_square_area_in_matrix.largest_square_area_in_matrix_bottom_up_space_optimization(-170141183460469231731687303715884040190, 0, [])
    # endregion
    
    # endregion

