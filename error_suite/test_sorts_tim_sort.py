import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import sorts
import unittest
import sorts.tim_sort


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable sorts.tim_sort.tim_sort
    
    # region FUZZER
    
    def test_tim_sort(self):
        """
        lst = builtins.list[builtins.list[typing.Any]]
        """
        actual = sorts.tim_sort.tim_sort([[], [], [], []])
        
        self.assertEqual([[], [], [], []], actual)
    
    def test_tim_sort1(self):
        """
        lst = builtins.list[builtins.list[typing.Any]]
        """
        actual = sorts.tim_sort.tim_sort([[]])
        
        self.assertEqual([[]], actual)
    
    def test_tim_sort2(self):
        """
        lst = builtins.list[builtins.list[builtins.list[typing.Any]]]
        """
        actual = sorts.tim_sort.tim_sort([[[], [], [], []], [[]], [[], [], [], [], []], [[], [], [], []]])
        
        self.assertEqual([[[]], [[], [], [], []], [[], [], [], []], [[], [], [], [], []]], actual)
    
    def test_tim_sort3(self):
        """
        lst = builtins.list[builtins.list[builtins.list[typing.Any]]]
        """
        actual = sorts.tim_sort.tim_sort([[[], [], [], []], [[], []]])
        
        self.assertEqual([[[], []], [[], [], [], []]], actual)
    
    def test_tim_sort_with_exception(self):
        """
        lst = builtins.list[typing.Any]
        """
        # This test fails because function [sorts.tim_sort.tim_sort] produces [IndexError]
        sorts.tim_sort.tim_sort([])
    # endregion
    
    # endregion

