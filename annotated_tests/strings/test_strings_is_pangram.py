import sys
sys.path.append(r'../../..')
import builtins
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
        input_str = '+'
        """
        actual = strings.is_pangram.is_pangram("+")
        
        self.assertEqual(False, actual)
    
    def test_is_pangram2(self):
        """
        input_str = ''
        """
        actual = strings.is_pangram.is_pangram("")
        
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
        input_str = '€'
        """
        actual = strings.is_pangram.is_pangram_faster("€")
        
        self.assertEqual(False, actual)
    
    def test_is_pangram_faster2(self):
        """
        input_str = 'abcdefghijklmnopqrst'
        """
        actual = strings.is_pangram.is_pangram_faster("abcdefghijklmnopqrst")
        
        self.assertEqual(False, actual)
    
    def test_is_pangram_faster3(self):
        """
        input_str = ''
        """
        actual = strings.is_pangram.is_pangram_faster("")
        
        self.assertEqual(False, actual)
    
    def test_is_pangram_faster_with_exception(self):
        """
        input_str = 'pythön'
        """
        # This test fails because function [strings.is_pangram.is_pangram_faster] produces [IndexError]
        strings.is_pangram.is_pangram_faster("pythön")
    
    def test_is_pangram_faster_with_exception1(self):
        """
        input_str = 'Jpytøn'
        """
        # This test fails because function [strings.is_pangram.is_pangram_faster] produces [IndexError]
        strings.is_pangram.is_pangram_faster("Jpytøn")
    
    def test_is_pangram_faster_with_exception2(self):
        """
        input_str = 'Ępytøö'
        """
        # This test fails because function [strings.is_pangram.is_pangram_faster] produces [IndexError]
        strings.is_pangram.is_pangram_faster("Ępytøö")
    
    def test_is_pangram_faster_with_exception3(self):
        """
        input_str = 'pythön'
        """
        # This test fails because function [strings.is_pangram.is_pangram_faster] produces [IndexError]
        strings.is_pangram.is_pangram_faster("pythön")
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

