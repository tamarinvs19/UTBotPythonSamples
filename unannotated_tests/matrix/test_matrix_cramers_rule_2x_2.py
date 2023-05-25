import sys
sys.path.append(r'..\..\..')
import builtins
import matrix
import unittest
import matrix.cramers_rule_2x2


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.cramers_rule_2x2.cramers_rule_2x2
    
    # region FUZZER
    
    def test_cramers_rule_2x_2(self):
        """
        equation1 = builtins.list[builtins.int]
        equation2 = builtins.list[builtins.int]
        """
        actual = matrix.cramers_rule_2x2.cramers_rule_2x2([2, 170141183460469231731687303715884105727, 3], [4, 3, -1])
        
        self.assertEqual((-0.25, 2.0571151139390031e-38), actual)
    
    def test_cramers_rule_2x_2_with_exception(self):
        """
        equation1 = builtins.list[typing.Any]
        equation2 = builtins.list[typing.Any]
        """
        # This test fails because function [matrix.cramers_rule_2x2.cramers_rule_2x2] produces [ValueError]
        matrix.cramers_rule_2x2.cramers_rule_2x2([], [])
    # endregion
    
    # endregion

