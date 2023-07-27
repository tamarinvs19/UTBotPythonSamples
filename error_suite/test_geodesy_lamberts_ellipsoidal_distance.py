import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import geodesy
import unittest
import geodesy.lamberts_ellipsoidal_distance


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance
    
    # region FUZZER
    
    def test_lamberts_ellipsoidal_distance(self):
        """
        lat1 = positive
        lon1 = 2.0
        lat2 = 2.0
        lon2 = 2.0000000037252903 (mutated from 2.0)
        """
        actual = geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance(1.0, 2.0, 2.0, 2.0000000037252903)
        
        self.assertEqual(110575.06437305336, actual)
    
    def test_lamberts_ellipsoidal_distance_with_exception(self):
        """
        lat1 = 2.000000238418579 (mutated from 2.0)
        lon1 = 2.0
        lat2 = float('-inf')
        lon2 = 2.0
        """
        # This test fails because function [geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance] produces [ValueError]
        geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance(2.000000238418579, 2.0, float('-inf'), 2.0)
    
    def test_lamberts_ellipsoidal_distance_with_exception1(self):
        """
        lat1 = 2.0
        lon1 = 2.0
        lat2 = -2.0 (mutated from 2.0)
        lon2 = float('inf')
        """
        # This test fails because function [geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance] produces [ValueError]
        geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance(2.0, 2.0, -2.0, float('inf'))
    
    def test_lamberts_ellipsoidal_distance_with_exception2(self):
        """
        lat1 = float('-inf')
        lon1 = 2.0
        lat2 = negative (mutated from positive)
        lon2 = 2.0
        """
        # This test fails because function [geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance] produces [ValueError]
        geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance(float('-inf'), 2.0, -1.0, 2.0)
    
    def test_lamberts_ellipsoidal_distance_with_exception3(self):
        """
        lat1 = 2.0
        lon1 = 2.0
        lat2 = 2.0
        lon2 = 2.0 (mutated from -2.0)
        """
        # This test fails because function [geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance] produces [ZeroDivisionError]
        geodesy.lamberts_ellipsoidal_distance.lamberts_ellipsoidal_distance(2.0, 2.0, 2.0, 2.0)
    # endregion
    
    # endregion

