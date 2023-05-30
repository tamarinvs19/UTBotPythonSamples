import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.knuth_morris_pratt


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.knuth_morris_pratt.kmp
    
    # region FUZZER
    
    def test_kmp(self):
        """
        pattern = '€'
        text = '-foo'
        """
        actual = strings.knuth_morris_pratt.kmp("€", "-foo")
        
        self.assertEqual(False, actual)
    
    def test_kmp1(self):
        """
        pattern = 'foo'
        text = 'foo'
        """
        actual = strings.knuth_morris_pratt.kmp("foo", "foo")
        
        self.assertEqual(True, actual)
    
    def test_kmp2(self):
        """
        pattern = 'pythönW'
        text = 'abcdefghijklmnopqrst'
        """
        actual = strings.knuth_morris_pratt.kmp("pythönW", "abcdefghijklmnopqrst")
        
        self.assertEqual(False, actual)
    
    def test_kmp3(self):
        """
        pattern = 'o'
        text = 'fo'
        """
        actual = strings.knuth_morris_pratt.kmp("o", "fo")
        
        self.assertEqual(True, actual)
    
    def test_kmp4(self):
        """
        pattern = 'pythön'
        text = ''
        """
        actual = strings.knuth_morris_pratt.kmp("pythön", "")
        
        self.assertEqual(False, actual)
    
    def test_kmp_with_exception(self):
        """
        pattern = ''
        text = 'ro'
        """
        # This test fails because function [strings.knuth_morris_pratt.kmp] produces [IndexError]
        strings.knuth_morris_pratt.kmp("", "ro")
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.knuth_morris_pratt.get_failure_array
    
    # region FUZZER
    
    def test_get_failure_array(self):
        """
        pattern = '€'
        """
        actual = strings.knuth_morris_pratt.get_failure_array("€")
        
        self.assertEqual([0], actual)
    
    def test_get_failure_array1(self):
        """
        pattern = 'abcdefBhijklmnopqrst'
        """
        actual = strings.knuth_morris_pratt.get_failure_array("abcdefBhijklmnopqrst")
        
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], actual)
    
    def test_get_failure_array2(self):
        """
        pattern = 'oo'
        """
        actual = strings.knuth_morris_pratt.get_failure_array("oo")
        
        self.assertEqual([0, 1], actual)
    
    def test_get_failure_array3(self):
        """
        pattern = 'o«ow'
        """
        actual = strings.knuth_morris_pratt.get_failure_array("o«ow")
        
        self.assertEqual([0, 0, 1, 0], actual)
    # endregion
    
    # endregion

