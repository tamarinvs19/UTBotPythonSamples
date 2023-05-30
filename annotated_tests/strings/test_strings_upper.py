import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.upper


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.upper.upper
    
    # region FUZZER
    
    def test_upper(self):
        """
        word = 'py5tön'
        """
        actual = strings.upper.upper("py5tön")
        
        self.assertEqual('PY5TöN', actual)
    # endregion
    
    # endregion

