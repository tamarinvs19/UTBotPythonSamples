import sys
sys.path.append(r'../../..')
import samples.dummy_with_eq
import builtins
import samples
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.dummy_with_eq.__eq__
    
    # region FUZZER
    
    def test___eq__(self):
        """
        self = samples.dummy_with_eq.Dummy
        other = samples.dummy_with_eq.Dummy
        """
        dummy = samples.dummy_with_eq.Dummy(-170141183457993351653116543166085857280)
        other = samples.dummy_with_eq.Dummy(0)
        
        actual = dummy.__eq__(other)
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.dummy_with_eq.propagate
    
    # region FUZZER
    
    def test_propagate(self):
        """
        self = samples.dummy_with_eq.Dummy
        """
        dummy = samples.dummy_with_eq.Dummy(170141183460391860479231967448702910463)
        
        actual = dummy.propagate()
        
        dummy1 = object.__new__(samples.dummy_with_eq.Dummy)
        dummy1.field = 170141183460391860479231967448702910463
        
        self.assertEqual([dummy1, dummy1], actual)
    # endregion
    
    # endregion

