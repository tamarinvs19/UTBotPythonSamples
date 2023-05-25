import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.lower


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.lower.lower
    
    # region FUZZER
    
    def test_lower(self):
        """
        word = 'py5tön'
        """
        actual = strings.lower.lower("py5tön")
        
        self.assertEqual('py5tön', actual)
    # endregion
    
    # endregion

