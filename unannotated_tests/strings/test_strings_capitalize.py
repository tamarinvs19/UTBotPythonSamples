import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.capitalize


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.capitalize.capitalize
    
    # region FUZZER
    
    def test_capitalize(self):
        """
        sentence = ''
        """
        actual = strings.capitalize.capitalize("")
        
        self.assertEqual('', actual)
    
    def test_capitalize1(self):
        """
        sentence = '-'
        """
        actual = strings.capitalize.capitalize("-")
        
        self.assertEqual('-', actual)
    # endregion
    
    # endregion

