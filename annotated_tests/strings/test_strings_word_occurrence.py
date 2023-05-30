import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.word_occurrence


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.word_occurrence.word_occurrence
    
    # region FUZZER
    
    def test_word_occurrence(self):
        """
        sentence = '€'
        """
        actual = strings.word_occurrence.word_occurrence("€")
        
        self.assertEqual({'€': 1, }, actual)
    
    def test_word_occurrence1(self):
        """
        sentence = ''
        """
        actual = strings.word_occurrence.word_occurrence("")
        
        self.assertEqual({}, actual)
    # endregion
    
    # endregion

