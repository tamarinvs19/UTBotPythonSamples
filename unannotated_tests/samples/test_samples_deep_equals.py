import sys
sys.path.append(r'../..')
import samples.deep_equals
import builtins
import samples
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.deep_equals.__eq__
    
    # region FUZZER
    
    def test___eq__(self):
        """
        self = samples.deep_equals.ComparableClass
        other = samples.deep_equals.ComparableClass
        """
        comparable_class = samples.deep_equals.ComparableClass(-170141183457993351653116543166085857280)
        other = samples.deep_equals.ComparableClass(0)
        
        actual = comparable_class.__eq__(other)
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion

