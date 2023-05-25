import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.check_anagrams


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.check_anagrams.check_anagrams
    
    # region FUZZER
    
    def test_check_anagrams(self):
        """
        first_str = 'pythön'
        second_str = 'fo'
        """
        actual = strings.check_anagrams.check_anagrams("pythön", "fo")
        
        self.assertEqual(False, actual)
    
    def test_check_anagrams1(self):
        """
        first_str = 'abcdefghijklmnopqrst'
        second_str = 'abcdefghijklmnopqrst'
        """
        actual = strings.check_anagrams.check_anagrams("abcdefghijklmnopqrst", "abcdefghijklmnopqrst")
        
        self.assertEqual(True, actual)
    
    def test_check_anagrams2(self):
        """
        first_str = ''
        second_str = ' '
        """
        actual = strings.check_anagrams.check_anagrams("", " ")
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion

