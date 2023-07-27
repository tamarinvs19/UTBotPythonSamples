import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import divide_and_conquer
import unittest
import divide_and_conquer.peak


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable divide_and_conquer.peak.peak
    
    # region FUZZER
    
    def test_peak(self):
        """
        lst = builtins.list[builtins.int]
        """
        actual = divide_and_conquer.peak.peak([0, 170141183460469231731687303715884105727, 1, -1])
        
        self.assertEqual(170141183460469231731687303715884105727, actual)
    
    def test_peak1(self):
        """
        lst = builtins.list[builtins.int]
        """
        actual = divide_and_conquer.peak.peak([3, -1, 0, 1, -170141183460469231731687303715884105728])
        
        self.assertEqual(1, actual)
    
    def test_peak2(self):
        """
        lst = builtins.list[builtins.int]
        """
        actual = divide_and_conquer.peak.peak([1, -1, 3, 0, -170141183460469231731687303715884105728])
        
        self.assertEqual(3, actual)
    
    def test_peak_with_exception(self):
        """
        lst = builtins.list[builtins.int]
        """
        # This test fails because function [divide_and_conquer.peak.peak] produces [IndexError]
        divide_and_conquer.peak.peak([170141183460469231731687303715884105727])
    
    def test_peak_with_exception1(self):
        """
        lst = builtins.list[builtins.int]
        """
        # This test fails because function [divide_and_conquer.peak.peak] produces [IndexError]
        divide_and_conquer.peak.peak([170141183460469231731687303715884105727, 0])
    
    def test_peak_with_exception2(self):
        """
        lst = builtins.list[builtins.int]
        """
        # This test fails because function [divide_and_conquer.peak.peak] produces [IndexError]
        divide_and_conquer.peak.peak([3, 0, -170141183460469231731687303715884105728])
    
    def test_peak_with_exception3(self):
        """
        lst = builtins.list[builtins.int]
        """
        # This test fails because function [divide_and_conquer.peak.peak] produces [IndexError]
        divide_and_conquer.peak.peak([-170141183460469231731687303715884105728, 0, 3])
    
    def test_peak_with_exception4(self):
        """
        lst = builtins.list[builtins.int]
        """
        # This test fails because function [divide_and_conquer.peak.peak] produces [IndexError]
        divide_and_conquer.peak.peak([170141183460469231731687303715884105727, -131073, -1, -1, -1])
    # endregion
    
    # endregion

