import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.hamming_distance


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.hamming_distance.hamming_distance
    
    # region FUZZER
    
    def test_hamming_distance(self):
        """
        string1 = 'abcdefghijklmnopqrst'
        string2 = 'abcdefghijklmnopqrst'
        """
        actual = strings.hamming_distance.hamming_distance("abcdefghijklmnopqrst", "abcdefghijklmnopqrst")
        
        self.assertEqual(0, actual)
    
    def test_hamming_distance1(self):
        """
        string1 = 'abcdefghijklmnopqrst'
        string2 = 'abcde¦fghijkmnopqrst'
        """
        actual = strings.hamming_distance.hamming_distance("abcdefghijklmnopqrst", "abcde¦fghijkmnopqrst")
        
        self.assertEqual(7, actual)
    
    def test_hamming_distance_with_exception(self):
        """
        string1 = '€'
        string2 = 'fo'
        """
        # This test fails because function [strings.hamming_distance.hamming_distance] produces [ValueError]
        strings.hamming_distance.hamming_distance("€", "fo")
    # endregion
    
    # endregion

