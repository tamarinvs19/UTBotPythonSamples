import sys
sys.path.append(r'../../..')
import builtins
import types
import samples
import unittest
import samples.type_inference_2


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.type_inference_2.g
    
    # region FUZZER
    
    def test_g(self):
        """
        x = min (mutated from zero)
        """
        actual = samples.type_inference_2.g(False)
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

