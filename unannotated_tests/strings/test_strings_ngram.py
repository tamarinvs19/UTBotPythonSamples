import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.ngram


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.ngram.create_ngram
    
    # region FUZZER
    
    def test_create_ngram(self):
        """
        sentence = '€'
        ngram_size = 33 (mutated from positive)
        """
        actual = strings.ngram.create_ngram("€", 33)
        
        self.assertEqual([], actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_create_ngram_with_exception(self):
        """
        sentence = 'abcdefghijklmnopqrst'
        ngram_size = -170141183460469231731687303715884105727 (mutated from positive)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.ngram.create_ngram("abcdefghijklmnopqrst", -170141183460469231731687303715884105727)
    # endregion
    
    # endregion

