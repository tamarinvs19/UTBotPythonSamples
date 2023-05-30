import sys
sys.path.append(r'../../..')
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
    
    def test_naive_pattern_search4(self):
        """
        s = 'pythön'
        pattern = 'pythön'
        """
        actual = strings.naive_string_search.naive_pattern_search("pythön", "pythön")
        
        self.assertEqual([0], actual)
    # endregion
    
    # endregion

