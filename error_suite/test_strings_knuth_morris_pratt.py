import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import strings
import unittest
import strings.knuth_morris_pratt


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.knuth_morris_pratt.kmp
    
    # region FUZZER
    
    def test_kmp(self):
        """
        pattern = 'foo'
        text = 'npöyth'
        """
        actual = strings.knuth_morris_pratt.kmp("foo", "npöyth")
        
        self.assertEqual(False, actual)
    
    def test_kmp1(self):
        """
        pattern = 'foo'
        text = ''
        """
        actual = strings.knuth_morris_pratt.kmp("foo", "")
        
        self.assertEqual(False, actual)
    
    def test_kmp2(self):
        """
        pattern = 'pythön'
        text = 'pyhön'
        """
        actual = strings.knuth_morris_pratt.kmp("pythön", "pyhön")
        
        self.assertEqual(False, actual)
    
    def test_kmp3(self):
        """
        pattern = 'pythön'
        text = 'pythön'
        """
        actual = strings.knuth_morris_pratt.kmp("pythön", "pythön")
        
        self.assertEqual(True, actual)
    
    def test_kmp_with_exception(self):
        """
        pattern = ''
        text = 'foo'
        """
        # This test fails because function [strings.knuth_morris_pratt.kmp] produces [IndexError]
        strings.knuth_morris_pratt.kmp("", "foo")
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.knuth_morris_pratt.get_failure_array
    
    # region FUZZER
    
    def test_get_failure_array(self):
        """
        pattern = 'pfoo' (mutated from 'foo')
        """
        actual = strings.knuth_morris_pratt.get_failure_array("pfoo")
        
        self.assertEqual([0, 0, 0, 0], actual)
    
    def test_get_failure_array1(self):
        """
        pattern = 'oopf'
        """
        actual = strings.knuth_morris_pratt.get_failure_array("oopf")
        
        self.assertEqual([0, 1, 0, 0], actual)
    
    def test_get_failure_array2(self):
        """
        pattern = ''
        """
        actual = strings.knuth_morris_pratt.get_failure_array("")
        
        self.assertEqual([0], actual)
    
    def test_get_failure_array3(self):
        """
        pattern = 'oo'
        """
        actual = strings.knuth_morris_pratt.get_failure_array("oo")
        
        self.assertEqual([0, 1], actual)
    # endregion
    
    # endregion

