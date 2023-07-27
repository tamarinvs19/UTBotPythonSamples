import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import electronics
import unittest
import electronics.resistor_equivalence


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable electronics.resistor_equivalence.resistor_parallel
    
    # region FUZZER
    
    def test_resistor_parallel(self):
        """
        resistors = builtins.list[builtins.float]
        """
        actual = electronics.resistor_equivalence.resistor_parallel([1.0])
        
        self.assertEqual(1.0, actual)
    
    def test_resistor_parallel_with_exception(self):
        """
        resistors = builtins.list[builtins.float]
        """
        # This test fails because function [electronics.resistor_equivalence.resistor_parallel] produces [ValueError]
        electronics.resistor_equivalence.resistor_parallel([float('-inf'), float('-inf'), 0.0, 1.0])
    
    def test_resistor_parallel_with_exception1(self):
        """
        resistors = builtins.list[builtins.float]
        """
        # This test fails because function [electronics.resistor_equivalence.resistor_parallel] produces [ValueError]
        electronics.resistor_equivalence.resistor_parallel([4.450147717014403E-308, 1.0, 1.0, float('-inf')])
    
    def test_resistor_parallel_with_exception2(self):
        """
        resistors = builtins.list[builtins.float]
        """
        # This test fails because function [electronics.resistor_equivalence.resistor_parallel] produces [ZeroDivisionError]
        electronics.resistor_equivalence.resistor_parallel([float('inf'), float('inf'), float('inf')])
    
    def test_resistor_parallel_with_exception3(self):
        """
        resistors = builtins.list[builtins.float]
        """
        # This test fails because function [electronics.resistor_equivalence.resistor_parallel] produces [ZeroDivisionError]
        electronics.resistor_equivalence.resistor_parallel([])
    # endregion
    
    # endregion
    
    # region Test suites for executable electronics.resistor_equivalence.resistor_series
    
    # region FUZZER
    
    def test_resistor_series(self):
        """
        resistors = builtins.list[builtins.float]
        """
        actual = electronics.resistor_equivalence.resistor_series([float('nan')])
        
        self.assertTrue(isinstance(actual, float))
    
    def test_resistor_series1(self):
        """
        resistors = builtins.list[builtins.float]
        """
        actual = electronics.resistor_equivalence.resistor_series([])
        
        self.assertEqual(0.0, actual)
    
    def test_resistor_series_with_exception(self):
        """
        resistors = builtins.list[builtins.float]
        """
        # This test fails because function [electronics.resistor_equivalence.resistor_series] produces [ValueError]
        electronics.resistor_equivalence.resistor_series([1.0, float('nan'), 0.0, float('-inf')])
    
    def test_resistor_series_with_exception1(self):
        """
        resistors = builtins.list[builtins.float]
        """
        # This test fails because function [electronics.resistor_equivalence.resistor_series] produces [ValueError]
        electronics.resistor_equivalence.resistor_series([float('-inf'), float('nan'), 0.0, 1.0])
    # endregion
    
    # endregion

