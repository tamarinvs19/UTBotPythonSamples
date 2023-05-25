import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.detecting_english_programmatically


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.detecting_english_programmatically.load_dictionary
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_load_dictionary_with_exception(self):
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.detecting_english_programmatically.load_dictionary()
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.detecting_english_programmatically.get_english_count
    
    # region FUZZER
    
    def test_get_english_count(self):
        """
        message = 'oo6'
        """
        actual = strings.detecting_english_programmatically.get_english_count("oo6")
        
        self.assertEqual(0.0, actual)
    
    def test_get_english_count_with_exception(self):
        """
        message = '€₩'
        """
        # This test fails because function [strings.detecting_english_programmatically.get_english_count] produces [ZeroDivisionError]
        strings.detecting_english_programmatically.get_english_count("€₩")
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.detecting_english_programmatically.remove_non_letters
    
    # region FUZZER
    
    def test_remove_non_letters(self):
        """
        message = '€'
        """
        actual = strings.detecting_english_programmatically.remove_non_letters("€")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.detecting_english_programmatically.is_english
    
    # region FUZZER
    
    def test_is_english(self):
        """
        message = 'abcdefBhijklmnopqrst'
        """
        actual = strings.detecting_english_programmatically.is_english("abcdefBhijklmnopqrst")
        
        self.assertEqual(False, actual)
    
    def test_is_english_with_exception(self):
        """
        message = '€'
        """
        # This test fails because function [strings.detecting_english_programmatically.is_english] produces [ZeroDivisionError]
        strings.detecting_english_programmatically.is_english("€")
    # endregion
    
    # endregion

