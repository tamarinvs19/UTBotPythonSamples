import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import geodesy
import unittest
import geodesy.haversine_distance


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable geodesy.haversine_distance.haversine_distance
    
    # region FUZZER
    
    def test_haversine_distance(self):
        """
        lat1 = 512.0 (mutated from 2.0)
        lon1 = positive
        lat2 = 2.0
        lon2 = 2.0
        """
        actual = geodesy.haversine_distance.haversine_distance(512.0, 1.0, 2.0, 2.0)
        
        self.assertEqual(3331687.704345533, actual)
    
    def test_haversine_distance_with_exception(self):
        """
        lat1 = 2.000000238418579 (mutated from 2.0)
        lon1 = 2.0
        lat2 = float('inf')
        lon2 = float('-inf')
        """
        # This test fails because function [geodesy.haversine_distance.haversine_distance] produces [ValueError]
        geodesy.haversine_distance.haversine_distance(2.000000238418579, 2.0, float('inf'), float('-inf'))
    
    def test_haversine_distance_with_exception1(self):
        """
        lat1 = positive
        lon1 = 2.0
        lat2 = 1.0000000018626451 (mutated from positive)
        lon2 = float('-inf')
        """
        # This test fails because function [geodesy.haversine_distance.haversine_distance] produces [ValueError]
        geodesy.haversine_distance.haversine_distance(1.0, 2.0, 1.0000000018626451, float('-inf'))
    
    def test_haversine_distance_with_exception2(self):
        """
        lat1 = float('-inf')
        lon1 = float('inf')
        lat2 = 2.000030517578125 (mutated from 2.0)
        lon2 = float('nan')
        """
        lon2 = float('nan')
        # This test fails because function [geodesy.haversine_distance.haversine_distance] produces [ValueError]
        geodesy.haversine_distance.haversine_distance(float('-inf'), float('inf'), 2.000030517578125, lon2)
    # endregion
    
    # endregion

