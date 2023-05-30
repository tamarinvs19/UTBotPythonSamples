import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.split


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.split.split
    
    # region FUZZER
    
    def test_split(self):
        """
        string = '€'
        """
        actual = strings.split.split("€")
        
        self.assertEqual(['€'], actual)
    
    def test_split1(self):
        """
        string = ''
        """
        actual = strings.split.split("")
        
        self.assertEqual([], actual)
    
    def test_split2(self):
        """
        string = ' '
        """
        actual = strings.split.split(" ")
        
        self.assertEqual([''], actual)
    
    def test_split3(self):
        """
        string = ' 	'
        """
        actual = strings.split.split(" 	")
        
        self.assertEqual(['', '\t'], actual)
    
    def test_split4(self):
        """
        string = ' '
        """
        actual = strings.split.split(" ")
        
        self.assertEqual(['\x04'], actual)
    # endregion
    
    # endregion

