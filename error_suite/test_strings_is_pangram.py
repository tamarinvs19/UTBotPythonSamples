import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import strings
import unittest
import strings.is_pangram


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.is_pangram.is_pangram
    
    # region FUZZER
    
    def test_is_pangram(self):
        actual = strings.is_pangram.is_pangram()
        
        self.assertEqual(True, actual)
    
    def test_is_pangram1(self):
        """
        input_str = ' '
        """
        actual = strings.is_pangram.is_pangram(" ")
        
        self.assertEqual(False, actual)
    
    def test_is_pangram2(self):
        """
        input_str = '' (mutated from '')
        """
        actual = strings.is_pangram.is_pangram("")
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.is_pangram.is_pangram_faster
    
    # region FUZZER
    
    def test_is_pangram_faster(self):
        actual = strings.is_pangram.is_pangram_faster()
        
        self.assertEqual(True, actual)
    
    def test_is_pangram_faster1(self):
        """
        input_str = 'pfoo' (mutated from 'foo')
        """
        actual = strings.is_pangram.is_pangram_faster("pfoo")
        
        self.assertEqual(False, actual)
    
    def test_is_pangram_faster2(self):
        """
        input_str = ''
        """
        actual = strings.is_pangram.is_pangram_faster("")
        
        self.assertEqual(False, actual)
    
    def test_is_pangram_faster3(self):
        """
        input_str = '4' (mutated from '')
        """
        actual = strings.is_pangram.is_pangram_faster("4")
        
        self.assertEqual(False, actual)
    
    def test_is_pangram_faster_with_exception(self):
        """
        input_str = 'ythön'
        """
        # This test fails because function [strings.is_pangram.is_pangram_faster] produces [IndexError]
        strings.is_pangram.is_pangram_faster("ythön")
    
    def test_is_pangram_faster_with_exception1(self):
        """
        input_str = 'pnt´öyh' (mutated from 'pntöyh')
        """
        # This test fails because function [strings.is_pangram.is_pangram_faster] produces [IndexError]
        strings.is_pangram.is_pangram_faster("pnt´öyh")
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.is_pangram.is_pangram_fastest
    
    # region FUZZER
    
    def test_is_pangram_fastest(self):
        actual = strings.is_pangram.is_pangram_fastest()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.is_pangram.benchmark
    
    # region FUZZER
    
    def test_benchmark_with_exception(self):
        # This test fails because function [strings.is_pangram.benchmark] produces [ImportError]
        strings.is_pangram.benchmark()
    # endregion
    
    # endregion

