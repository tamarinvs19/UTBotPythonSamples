import sys
sys.path.append(r'../../..')
import samples.dummy_without_eq
import builtins
import samples
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.dummy_without_eq.propagate
    
    # region FUZZER
    
    def test_propagate(self):
        """
        self = samples.dummy_without_eq.Dummy
        """
        dummy = samples.dummy_without_eq.Dummy()
        
        actual = dummy.propagate()
        
        expected_list = [dummy, dummy]
        expected_length = len(expected_list)
        actual_length = len(actual)
        
        self.assertEqual(expected_length, actual_length)
        
        index = None
        for index in range(0, expected_length, 1):
            expected_element = expected_list[index]
            actual_element = actual[index]
            
            self.assertTrue(isinstance(actual_element, samples.dummy_without_eq.Dummy))
        
        self.assertEqual(dummy, dummy)
    # endregion
    
    # endregion

