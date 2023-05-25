import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.is_contains_unique_chars


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.is_contains_unique_chars.is_contains_unique_chars
    
    # region FUZZER
    
    def test_is_contains_unique_chars(self):
        """
        input_str = '€'
        """
        actual = strings.is_contains_unique_chars.is_contains_unique_chars("€")
        
        self.assertEqual(True, actual)
    
    def test_is_contains_unique_chars1(self):
        """
        input_str = 'f>oo'
        """
        actual = strings.is_contains_unique_chars.is_contains_unique_chars("f>oo")
        
        self.assertEqual(False, actual)
    
    def test_is_contains_unique_chars2(self):
        """
        input_str = builtins.list[typing.Any]
        """
        actual = strings.is_contains_unique_chars.is_contains_unique_chars([])
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion

