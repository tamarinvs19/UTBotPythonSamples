import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import linear_algebra
import unittest
import linear_algebra.src.transformations_2d


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable linear_algebra.src.transformations_2d.scaling
    
    # region FUZZER
    
    def test_scaling(self):
        """
        scaling_factor = float('nan')
        """
        scaling_factor = float('nan')
        
        actual = linear_algebra.src.transformations_2d.scaling(scaling_factor)
        
        expected_list = [[float('nan'), float('nan')], [float('nan'), float('nan')]]
        expected_length = len(expected_list)
        actual_length = len(actual)
        
        self.assertEqual(expected_length, actual_length)
        
        self.assertTrue(isinstance(actual, list))
    # endregion
    
    # endregion
    
    # region Test suites for executable linear_algebra.src.transformations_2d.rotation
    
    # region FUZZER
    
    def test_rotation(self):
        """
        angle = float('nan')
        """
        angle = float('nan')
        
        actual = linear_algebra.src.transformations_2d.rotation(angle)
        
        expected_list = [[float('nan'), float('nan')], [float('nan'), float('nan')]]
        expected_length = len(expected_list)
        actual_length = len(actual)
        
        self.assertEqual(expected_length, actual_length)
        
        self.assertTrue(isinstance(actual, list))
    
    def test_rotation_with_exception(self):
        """
        angle = float('-inf')
        """
        # This test fails because function [linear_algebra.src.transformations_2d.rotation] produces [ValueError]
        linear_algebra.src.transformations_2d.rotation(float('-inf'))
    # endregion
    
    # endregion
    
    # region Test suites for executable linear_algebra.src.transformations_2d.projection
    
    # region FUZZER
    
    def test_projection(self):
        """
        angle = float('nan')
        """
        angle = float('nan')
        
        actual = linear_algebra.src.transformations_2d.projection(angle)
        
        expected_list = [[float('nan'), float('nan')], [float('nan'), float('nan')]]
        expected_length = len(expected_list)
        actual_length = len(actual)
        
        self.assertEqual(expected_length, actual_length)
        
        self.assertTrue(isinstance(actual, list))
    
    def test_projection_with_exception(self):
        """
        angle = float('-inf')
        """
        # This test fails because function [linear_algebra.src.transformations_2d.projection] produces [ValueError]
        linear_algebra.src.transformations_2d.projection(float('-inf'))
    # endregion
    
    # endregion
    
    # region Test suites for executable linear_algebra.src.transformations_2d.reflection
    
    # region FUZZER
    
    def test_reflection(self):
        """
        angle = -2.0 (mutated from 2.0)
        """
        actual = linear_algebra.src.transformations_2d.reflection(-2.0)
        
        self.assertEqual([[-1.8322936730942847, 0.7568024953079283], [0.7568024953079283, -2.8185948536513634]], actual)
    
    def test_reflection_with_exception(self):
        """
        angle = float('-inf')
        """
        # This test fails because function [linear_algebra.src.transformations_2d.reflection] produces [ValueError]
        linear_algebra.src.transformations_2d.reflection(float('-inf'))
    # endregion
    
    # endregion

