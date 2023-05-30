import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.frequency_finder


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.frequency_finder.get_letter_count
    
    # region FUZZER
    
    def test_get_letter_count(self):
        """
        message = 'oo6'
        """
        actual = strings.frequency_finder.get_letter_count("oo6")
        
        self.assertEqual({'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 2, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, }, actual)
    
    def test_get_letter_count1(self):
        """
        message = '€₩'
        """
        actual = strings.frequency_finder.get_letter_count("€₩")
        
        self.assertEqual({'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, }, actual)
    
    def test_get_letter_count2(self):
        """
        message = ''
        """
        actual = strings.frequency_finder.get_letter_count("")
        
        self.assertEqual({'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, }, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.frequency_finder.get_item_at_index_zero
    
    # region FUZZER
    
    def test_get_item_at_index_zero(self):
        """
        x = builtins.tuple[builtins.int, ...]
        """
        actual = strings.frequency_finder.get_item_at_index_zero((-1,))
        
        self.assertEqual(-1, actual)
    
    def test_get_item_at_index_zero_with_exception(self):
        """
        x = builtins.tuple[typing.Any, ...]
        """
        # This test fails because function [strings.frequency_finder.get_item_at_index_zero] produces [IndexError]
        strings.frequency_finder.get_item_at_index_zero(())
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.frequency_finder.get_frequency_order
    
    # region FUZZER
    
    def test_get_frequency_order(self):
        """
        message = ''
        """
        actual = strings.frequency_finder.get_frequency_order("")
        
        self.assertEqual('ZQXJKVBPYGFWMUCLDRHSNIOATE', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.frequency_finder.english_freq_match_score
    
    # region FUZZER
    
    def test_english_freq_match_score(self):
        """
        message = '€'
        """
        actual = strings.frequency_finder.english_freq_match_score("€")
        
        self.assertEqual(0, actual)
    
    def test_english_freq_match_score1(self):
        """
        message = 'abcdfghi6klmnRnp2qrst'
        """
        actual = strings.frequency_finder.english_freq_match_score("abcdfghi6klmnRnp2qrst")
        
        self.assertEqual(2, actual)
    # endregion
    
    # endregion

