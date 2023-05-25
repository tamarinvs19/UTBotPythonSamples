import sys
sys.path.append(r'..\..\..')
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
        separated = builtins.list[typing.Any]
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
    
    def test_join_with_exception(self):
        """
        separator = 'pythön'
        separated = builtins.list[builtins.object]
        """
        object1 = builtins.object()
        separated = [object(), object1]
        # This test fails because function [strings.join.join] produces [Exception]
        strings.join.join("pythön", separated)
        
        self.assertEqual([object(), object1], separated)
    # endregion
    
    # endregion

