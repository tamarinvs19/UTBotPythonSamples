import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.text_justification


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.text_justification.text_justification
    
    # region FUZZER
    
    def test_text_justification(self):
        """
        word = ' '
        max_width = 34 (mutated from 2)
        """
        actual = strings.text_justification.text_justification(" ", 34)
        
        self.assertEqual(['                                   '], actual)
    
    def test_text_justification1(self):
        """
        word = 'pythön'
        max_width = 1025 (mutated from positive)
        """
        actual = strings.text_justification.text_justification("pythön", 1025)
        
        self.assertEqual(['pythön                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           '], actual)
    
    def test_text_justification_with_exception(self):
        """
        word = '￿'
        max_width = zero (mutated from min)
        """
        # This test fails because function [strings.text_justification.text_justification] produces [IndexError]
        strings.text_justification.text_justification("￿", 0)
    
    def test_text_justification_with_exception1(self):
        """
        word = 'pythön'
        max_width = 170141183460469231731687303715884097535 (mutated from max)
        """
        # This test fails because function [strings.text_justification.text_justification] produces [OverflowError]
        strings.text_justification.text_justification("pythön", 170141183460469231731687303715884097535)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_text_justification_with_exception2(self):
        """
        word = ' '
        max_width = 134217729 (mutated from positive)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.text_justification.text_justification(" ", 134217729)
    # endregion
    
    # endregion

