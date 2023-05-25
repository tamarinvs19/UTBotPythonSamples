import sys
sys.path.append(r'..\..\..')
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
        string = builtins.list[typing.Any]
        """
        actual = strings.split.split([])
        
        self.assertEqual([], actual)
    
    def test_split2(self):
        """
        string = 'foo'
        separator = 'f'
        """
        actual = strings.split.split("foo", "f")
        
        self.assertEqual(['', 'oo'], actual)
    # endregion
    
    # endregion

