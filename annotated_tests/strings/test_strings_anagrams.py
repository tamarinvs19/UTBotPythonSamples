import sys
sys.path.append(r'../../..')
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
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_anagram_with_exception(self):
        """
        my_word = 'f-oo'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.anagrams.anagram("f-oo")
    # endregion
    
    # endregion

