import sys
sys.path.append(r'..\..\..')
import builtins
import matrix
import unittest
import matrix.matrix_operation


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.matrix_operation.add
    
    # region FUZZER
    
    def test_add(self):
        actual = matrix.matrix_operation.add()
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion

