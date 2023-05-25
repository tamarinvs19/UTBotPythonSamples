import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.naive_string_search


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.naive_string_search.naive_pattern_search
    
    # region FUZZER
    
    def test_naive_pattern_search(self):
        """
        s = '€'
        pattern = '-foo'
        """
        actual = strings.naive_string_search.naive_pattern_search("€", "-foo")
        
        self.assertEqual([], actual)
    
    def test_naive_pattern_search1(self):
        """
        s = '₻€₤'
        pattern = '-fo'
        """
        actual = strings.naive_string_search.naive_pattern_search("₻€₤", "-fo")
        
        self.assertEqual([], actual)
    
    def test_naive_pattern_search2(self):
        """
        s = 'foo'
        pattern = 'fo'
        """
        actual = strings.naive_string_search.naive_pattern_search("foo", "fo")
        
        self.assertEqual([0], actual)
    
    def test_naive_pattern_search3(self):
        """
        s = 'foo'
        pattern = ''
        """
        actual = strings.naive_string_search.naive_pattern_search("foo", "")
        
        self.assertEqual([0, 1, 2, 3], actual)
    
    def test_naive_pattern_search_with_exception(self):
        """
        s = '€'
        pattern = builtins.dict[builtins.int, builtins.int]
        """
        # This test fails because function [strings.naive_string_search.naive_pattern_search] produces [KeyError]
        strings.naive_string_search.naive_pattern_search("€", {1: -170141183460469231731687303715884105728, })
    # endregion
    
    # endregion

