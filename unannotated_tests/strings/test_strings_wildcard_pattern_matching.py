import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.wildcard_pattern_matching


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.wildcard_pattern_matching.match_pattern
    
    # region FUZZER
    
    def test_match_pattern(self):
        """
        input_string = 'pythön'
        pattern = 'fo'
        """
        actual = strings.wildcard_pattern_matching.match_pattern("pythön", "fo")
        
        self.assertEqual(False, actual)
    
    def test_match_pattern1(self):
        """
        input_string = 'foo'
        pattern = '*'
        """
        actual = strings.wildcard_pattern_matching.match_pattern("foo", "*")
        
        self.assertEqual(False, actual)
    
    def test_match_pattern2(self):
        """
        input_string = '*'
        pattern = '.'
        """
        actual = strings.wildcard_pattern_matching.match_pattern("*", ".")
        
        self.assertEqual(True, actual)
    
    def test_match_pattern3(self):
        """
        input_string = 'foo'
        pattern = ''
        """
        actual = strings.wildcard_pattern_matching.match_pattern("foo", "")
        
        self.assertEqual(False, actual)
    
    def test_match_pattern4(self):
        """
        input_string = '*Z'
        pattern = '*'
        """
        actual = strings.wildcard_pattern_matching.match_pattern("*Z", "*")
        
        self.assertEqual(False, actual)
    
    def test_match_pattern5(self):
        """
        input_string = builtins.list[typing.Any]
        pattern = ''
        """
        actual = strings.wildcard_pattern_matching.match_pattern([], "")
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion

