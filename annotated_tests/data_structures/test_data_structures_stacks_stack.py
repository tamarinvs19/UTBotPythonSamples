import sys
sys.path.append(r'../..')
import types
import data_structures
import unittest
import data_structures.stacks.stack


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.stacks.stack.test_stack
    
    # region FUZZER
    
    def test_test_stack(self):
        actual = data_structures.stacks.stack.test_stack()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

