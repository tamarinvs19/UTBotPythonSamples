import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.reverse_long_words


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.reverse_long_words.reverse_long_words
    
    # region FUZZER
    
    def test_reverse_long_words(self):
        """
        sentence = ''
        """
        actual = strings.reverse_long_words.reverse_long_words("")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion

