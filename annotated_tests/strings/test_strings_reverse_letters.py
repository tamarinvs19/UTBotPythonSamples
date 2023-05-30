import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.reverse_letters


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.reverse_letters.reverse_letters
    
    # region FUZZER
    
    def test_reverse_letters(self):
        """
        input_str = ''
        """
        actual = strings.reverse_letters.reverse_letters("")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion

