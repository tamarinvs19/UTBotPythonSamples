import sys
sys.path.append(r'..\..\..')
import builtins
import types
import strings
import unittest
import strings.rabin_karp


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.rabin_karp.rabin_karp
    
    # region FUZZER
    
    def test_rabin_karp(self):
        """
        pattern = '€'
        text = '-foo'
        """
        actual = strings.rabin_karp.rabin_karp("€", "-foo")
        
        self.assertEqual(False, actual)
    
    def test_rabin_karp1(self):
        """
        pattern = 'foo'
        text = '€⃖'
        """
        actual = strings.rabin_karp.rabin_karp("foo", "€⃖")
        
        self.assertEqual(False, actual)
    
    def test_rabin_karp2(self):
        """
        pattern = 'abcdefghijklmnopqrst'
        text = 'abcdefghijklmnopqrst'
        """
        actual = strings.rabin_karp.rabin_karp("abcdefghijklmnopqrst", "abcdefghijklmnopqrst")
        
        self.assertEqual(True, actual)
    
    def test_rabin_karp3(self):
        """
        pattern = ''
        text = builtins.list[typing.Any]
        """
        actual = strings.rabin_karp.rabin_karp("", [])
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.rabin_karp.test_rabin_karp
    
    # region FUZZER
    
    def test_test_rabin_karp(self):
        actual = strings.rabin_karp.test_rabin_karp()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

