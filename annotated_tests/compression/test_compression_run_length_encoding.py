import sys
sys.path.append(r'../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.run_length_encoding.run_length_encode
    
    # region FUZZER
    
    def test_run_length_encode(self):
        """
        text = '€'
        """
        actual = compression.run_length_encoding.run_length_encode("€")
        
        self.assertEqual([('€', 1)], actual)
    
    def test_run_length_encode1(self):
        """
        text = 'f>oo'
        """
        actual = compression.run_length_encoding.run_length_encode("f>oo")
        
        self.assertEqual([('f', 1), ('>', 1), ('o', 2)], actual)
    
    def test_run_length_encode2(self):
        """
        text = ''
        """
        actual = compression.run_length_encoding.run_length_encode("")
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.run_length_encoding.run_length_decode
    
    # region FUZZER
    
    def test_run_length_decode(self):
        """
        encoded = builtins.list[typing.Any]
        """
        actual = compression.run_length_encoding.run_length_decode([])
        
        self.assertEqual('', actual)
    
    def test_run_length_decode_with_exception(self):
        """
        encoded = builtins.list[builtins.str]
        """
        # This test fails because function [compression.run_length_encoding.run_length_decode] produces [ValueError]
        compression.run_length_encoding.run_length_decode(["abcdefghijklmnopqrst"])
    # endregion
    
    # endregion

