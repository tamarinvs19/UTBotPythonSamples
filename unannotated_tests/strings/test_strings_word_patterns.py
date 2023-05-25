import sys
sys.path.append(r'..\..\..')
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
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_word_pattern_with_exception(self):
        """
        word = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.word_patterns.get_word_pattern(bytearray(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_word_pattern_with_exception1(self):
        """
        word = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.word_patterns.get_word_pattern(bytearray(33554433))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_word_pattern_with_exception2(self):
        """
        word = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.word_patterns.get_word_pattern(bytes(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_word_pattern_with_exception3(self):
        """
        word = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.word_patterns.get_word_pattern(bytes(33554433))
    # endregion
    
    # endregion

