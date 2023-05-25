import sys
sys.path.append(r'../..')
import builtins
import samples
import unittest
import samples.test_coverage


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.test_coverage.hard_function
    
    # region FUZZER
    
    def test_hard_function(self):
        """
        x = 2097551 (mutated from 399)
        """
        actual = samples.test_coverage.hard_function(2097551)
        
        self.assertEqual(3, actual)
    
    def test_hard_function1(self):
        """
        x = -170141183460469231731687303715882008177 (mutated from 2097551)
        """
        actual = samples.test_coverage.hard_function(-170141183460469231731687303715882008177)
        
        self.assertEqual(2, actual)
    
    def test_hard_function2(self):
        """
        x = -170139885386254598024780171091801800700 (mutated from -170141183460469231731687303715884105724)
        """
        actual = samples.test_coverage.hard_function(-170139885386254598024780171091801800700)
        
        self.assertEqual(1, actual)
    # endregion
    
    # endregion

