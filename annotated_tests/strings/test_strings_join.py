import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.join


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.join.join
    
    # region FUZZER
    
    def test_join(self):
        """
        separator = 'join() accepts onlystrings to be joined'
        separated = builtins.list[builtins.str]
        """
        actual = strings.join.join("join() accepts onlystrings to be joined", [])
        
        self.assertEqual('', actual)
    
    def test_join1(self):
        """
        separator = 'pythön'
        separated = builtins.list[builtins.str]
        """
        actual = strings.join.join("pythön", ["", "join() accepts only strings to be joined"])
        
        self.assertEqual('join() accepts only strings to be joined', actual)
    # endregion
    
    # endregion

