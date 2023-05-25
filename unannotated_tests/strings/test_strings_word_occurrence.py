import sys
sys.path.append(r'..\..\..')
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
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_word_occurrence_with_exception(self):
        """
        sentence = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.word_occurrence.word_occurrence(bytes(67125313))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_word_occurrence_with_exception1(self):
        """
        sentence = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.word_occurrence.word_occurrence(bytes(16793665))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_word_occurrence_with_exception2(self):
        """
        sentence = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.word_occurrence.word_occurrence(bytearray(268435458))
    # endregion
    
    # endregion

