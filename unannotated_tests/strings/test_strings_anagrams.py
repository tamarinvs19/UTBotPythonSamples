import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.anagrams


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.anagrams.signature
    
    # region FUZZER
    
    def test_signature(self):
        """
        word = ''
        """
        actual = strings.anagrams.signature("")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.anagrams.anagram
    
    # region FUZZER
    
    def test_anagram(self):
        """
        my_word = '€'
        """
        actual = strings.anagrams.anagram("€")
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion

