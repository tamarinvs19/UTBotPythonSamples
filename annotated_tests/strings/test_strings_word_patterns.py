import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.word_patterns


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.word_patterns.get_word_pattern
    
    # region FUZZER
    
    def test_get_word_pattern(self):
        """
        word = ''
        """
        actual = strings.word_patterns.get_word_pattern("")
        
        self.assertEqual('', actual)
    
    def test_get_word_pattern1(self):
        """
        word = '€'
        """
        actual = strings.word_patterns.get_word_pattern("€")
        
        self.assertEqual('0', actual)
    # endregion
    
    # endregion

