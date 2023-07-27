import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import divide_and_conquer
import unittest
import divide_and_conquer.closest_pair_of_points


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable divide_and_conquer.closest_pair_of_points.euclidean_distance_sqr
    
    # region FUZZER
    
    def test_euclidean_distance_sqr_with_exception(self):
        """
        point1 = 'oof'
        point2 = ''
        """
        # This test fails because function [divide_and_conquer.closest_pair_of_points.euclidean_distance_sqr] produces [IndexError]
        divide_and_conquer.closest_pair_of_points.euclidean_distance_sqr("oof", "")
    # endregion
    
    # endregion
    
    # region Test suites for executable divide_and_conquer.closest_pair_of_points.closest_pair_of_points_sqr
    
    # region FUZZER
    
    def test_closest_pair_of_points_sqr(self):
        """
        points_sorted_on_x = builtins.list[typing.Any]
        points_sorted_on_y = builtins.list[typing.Any]
        points_counts = -170141183460468929500232400058590429182 (mutated from 302231454903657293676546)
        """
        actual = divide_and_conquer.closest_pair_of_points.closest_pair_of_points_sqr([], [], -170141183460468929500232400058590429182)
        
        self.assertEqual(float('inf'), actual)
    
    def test_closest_pair_of_points_sqr_with_exception(self):
        """
        points_sorted_on_x = builtins.list[typing.Any]
        points_sorted_on_y = builtins.list[typing.Any]
        points_counts = 302231454903657293676546 (mutated from 2)
        """
        # This test fails because function [divide_and_conquer.closest_pair_of_points.closest_pair_of_points_sqr] produces [IndexError]
        divide_and_conquer.closest_pair_of_points.closest_pair_of_points_sqr([], [], 302231454903657293676546)
    
    def test_closest_pair_of_points_sqr_with_exception1(self):
        """
        points_sorted_on_x = builtins.list[typing.Any]
        points_sorted_on_y = builtins.list[typing.Any]
        points_counts = 2 (mutated from -170141183460469231731687303715884105726)
        """
        # This test fails because function [divide_and_conquer.closest_pair_of_points.closest_pair_of_points_sqr] produces [IndexError]
        divide_and_conquer.closest_pair_of_points.closest_pair_of_points_sqr([], [], 2)
    # endregion
    
    # endregion

