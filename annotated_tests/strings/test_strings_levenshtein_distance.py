import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.levenshtein_distance


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.levenshtein_distance.levenshtein_distance
    
    # region FUZZER
    
    def test_levenshtein_distance(self):
        """
        first_word = '€'
        second_word = '-foo'
        """
        actual = strings.levenshtein_distance.levenshtein_distance("€", "-foo")
        
        self.assertEqual(4, actual)
    
    def test_levenshtein_distance1(self):
        """
        first_word = '€'
        second_word = ''
        """
        actual = strings.levenshtein_distance.levenshtein_distance("€", "")
        
        self.assertEqual(1, actual)
    # endregion
    
    # endregion

