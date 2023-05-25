import sys
sys.path.append(r'..\..\..')
import builtins
import strings.boyer_moore_search
import strings
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.boyer_moore_search.match_in_pattern
    
    # region FUZZER
    
    def test_match_in_pattern(self):
        """
        self = strings.boyer_moore_search.BoyerMooreSearch
        char = object()
        """
        boyer_moore_search = strings.boyer_moore_search.BoyerMooreSearch("abcdefghijklmnopqrst", "foo")
        char = object()
        
        actual = boyer_moore_search.match_in_pattern(char)
        
        self.assertEqual(-1, actual)
        
        char_modified = object.__new__(object)
        
        self.assertTrue(isinstance(char, builtins.object))
        
        self.assertEqual(boyer_moore_search, boyer_moore_search)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.boyer_moore_search.mismatch_in_text
    
    # region FUZZER
    
    def test_mismatch_in_text_with_exception(self):
        """
        self = strings.boyer_moore_search.BoyerMooreSearch
        current_pos = -5316911983139663491615228241121378306 (mutated from -2)
        """
        boyer_moore_search = strings.boyer_moore_search.BoyerMooreSearch("pythön", "foo")
        # This test fails because function [strings.boyer_moore_search.mismatch_in_text] produces [IndexError]
        boyer_moore_search.mismatch_in_text(-5316911983139663491615228241121378306)
        
        self.assertEqual(boyer_moore_search, boyer_moore_search)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.boyer_moore_search.bad_character_heuristic
    
    # region FUZZER
    
    def test_bad_character_heuristic(self):
        """
        self = strings.boyer_moore_search.BoyerMooreSearch
        """
        boyer_moore_search = strings.boyer_moore_search.BoyerMooreSearch("€", "€")
        
        actual = boyer_moore_search.bad_character_heuristic()
        
        self.assertEqual([0], actual)
        
        self.assertEqual(boyer_moore_search, boyer_moore_search)
    
    def test_bad_character_heuristic1(self):
        """
        self = strings.boyer_moore_search.BoyerMooreSearch
        """
        boyer_moore_search = strings.boyer_moore_search.BoyerMooreSearch("€", "")
        
        actual = boyer_moore_search.bad_character_heuristic()
        
        self.assertEqual([], actual)
        
        self.assertEqual(boyer_moore_search, boyer_moore_search)
    
    def test_bad_character_heuristic2(self):
        """
        self = strings.boyer_moore_search.BoyerMooreSearch
        """
        boyer_moore_search = strings.boyer_moore_search.BoyerMooreSearch("€", "9")
        
        actual = boyer_moore_search.bad_character_heuristic()
        
        self.assertEqual([], actual)
        
        self.assertEqual(boyer_moore_search, boyer_moore_search)
    
    def test_bad_character_heuristic3(self):
        """
        self = strings.boyer_moore_search.BoyerMooreSearch
        """
        boyer_moore_search = strings.boyer_moore_search.BoyerMooreSearch("€⃥", "€")
        
        actual = boyer_moore_search.bad_character_heuristic()
        
        self.assertEqual([0], actual)
        
        self.assertEqual(boyer_moore_search, boyer_moore_search)
    # endregion
    
    # endregion

