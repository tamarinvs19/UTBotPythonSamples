import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.jaro_winkler


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.jaro_winkler.jaro_winkler
    
    # region FUZZER
    
    def test_jaro_winkler(self):
        """
        str1 = '€'
        str2 = 'fo'
        """
        actual = strings.jaro_winkler.jaro_winkler("€", "fo")
        
        self.assertEqual(0.0, actual)
    
    def test_jaro_winkler1(self):
        """
        str1 = ''
        str2 = ''
        """
        actual = strings.jaro_winkler.jaro_winkler("", "")
        
        self.assertEqual(0.0, actual)
    
    def test_jaro_winkler2(self):
        """
        str1 = 'foou'
        str2 = 'foo'
        """
        actual = strings.jaro_winkler.jaro_winkler("foou", "foo")
        
        self.assertEqual(0.9416666666666667, actual)
    
    def test_jaro_winkler3(self):
        """
        str1 = 'foou'
        str2 = 'foR'
        """
        actual = strings.jaro_winkler.jaro_winkler("foou", "foR")
        
        self.assertEqual(0.7777777777777777, actual)
    # endregion
    
    # endregion

