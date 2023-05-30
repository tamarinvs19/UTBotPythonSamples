import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.remove_duplicate


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.remove_duplicate.remove_duplicates
    
    # region FUZZER
    
    def test_remove_duplicates(self):
        """
        sentence = ''
        """
        actual = strings.remove_duplicate.remove_duplicates("")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion

