import sys
sys.path.append(r'../../..')
import builtins
import samples
import unittest
import samples.deep_equals


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.deep_equals.comparable_list
    
    # region FUZZER
    
    def test_comparable_list(self):
        """
        length = -170141183460469231731687303715882008576 (mutated from min)
        """
        actual = samples.deep_equals.comparable_list(-170141183460469231731687303715882008576)
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.deep_equals.incomparable_list
    
    # region FUZZER
    
    def test_incomparable_list(self):
        """
        length = -170141183460469231731687303715882008576 (mutated from min)
        """
        actual = samples.deep_equals.incomparable_list(-170141183460469231731687303715882008576)
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion

