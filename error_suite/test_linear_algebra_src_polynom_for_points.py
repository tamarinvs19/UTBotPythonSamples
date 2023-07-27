import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import linear_algebra
import unittest
import linear_algebra.src.polynom_for_points


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable linear_algebra.src.polynom_for_points.points_to_polynomial
    
    # region FUZZER
    
    def test_points_to_polynomial(self):
        """
        coordinates = builtins.list[builtins.list[builtins.int]]
        """
        actual = linear_algebra.src.polynom_for_points.points_to_polynomial([[3, 170141183460469231731687303715884105727], [0, 0]])
        
        self.assertEqual('f(x)=x^1*5.671372782015641e+37+x^0*0.0', actual)
    
    def test_points_to_polynomial1(self):
        """
        coordinates = builtins.list[builtins.list[builtins.int]]
        """
        actual = linear_algebra.src.polynom_for_points.points_to_polynomial([[1, 0], [1, 1]])
        
        self.assertEqual('x=1', actual)
    
    def test_points_to_polynomial_with_exception(self):
        """
        coordinates = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [linear_algebra.src.polynom_for_points.points_to_polynomial] produces [ValueError]
        linear_algebra.src.polynom_for_points.points_to_polynomial([[170141183460469231731687303715884105727, 2, 3, 1], [-1, 170141183460469231731687303715884105727, -1, 1], [3, -170141183460469231731687303715884105728, 0, 170141183460469231731687303715884105727], [3, 170141183460469231731687303715884105727, 2, -1]])
    
    def test_points_to_polynomial_with_exception1(self):
        """
        coordinates = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [linear_algebra.src.polynom_for_points.points_to_polynomial] produces [ZeroDivisionError]
        linear_algebra.src.polynom_for_points.points_to_polynomial([[0, 0], [3, 170141183460469231731687303715884105727]])
    
    def test_points_to_polynomial_with_exception2(self):
        """
        coordinates = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [linear_algebra.src.polynom_for_points.points_to_polynomial] produces [ValueError]
        linear_algebra.src.polynom_for_points.points_to_polynomial([[-170141183460469231731687303715884105728, 0], [-170141183460469231731687303715884105728, 0]])
    
    def test_points_to_polynomial_with_exception3(self):
        """
        coordinates = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [linear_algebra.src.polynom_for_points.points_to_polynomial] produces [ZeroDivisionError]
        linear_algebra.src.polynom_for_points.points_to_polynomial([[-170141183460469231731687303715884105728, 77371252455336267181211648], [-170141183460469231731687302616372477950, -170141183460469231731687303715884105728]])
    # endregion
    
    # endregion

