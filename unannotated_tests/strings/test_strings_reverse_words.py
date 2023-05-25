import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.reverse_words


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.reverse_words.reverse_words
    
    # region FUZZER
    
    def test_reverse_words(self):
        """
        input_str = ''
        """
        actual = strings.reverse_words.reverse_words("")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion

