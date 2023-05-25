import sys
sys.path.append(r'../../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.huffman.parse_file
    
    # region FUZZER
    
    def test_parse_file(self):
        """
        file_path = '€'
        """
        actual = compression.huffman.parse_file("../../€")
        
        self.assertEqual([], actual)
    
    def test_parse_file_with_exception(self):
        """
        file_path = 'abcdefBhijklmnopqrst'
        """
        # This test fails because function [compression.huffman.parse_file] produces [FileNotFoundError]
        compression.huffman.parse_file("abcdefBhijklmnopqrst")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.huffman.build_tree
    
    # region FUZZER
    
    def test_build_tree(self):
        """
        letters = builtins.list[compression.huffman.Letter]
        """
        letter = compression.huffman.Letter("abcdefghijklmnopqrst", -1)
        letters = [letter]
        
        actual = compression.huffman.build_tree(letters)
        
        actual_letter = actual.letter
        expected_letter = letter.letter
        
        self.assertEqual(expected_letter, actual_letter)
        actual_freq = actual.freq
        expected_freq = letter.freq
        
        self.assertEqual(expected_freq, actual_freq)
        actual_bitstring = actual.bitstring
        expected_bitstring = letter.bitstring
        
        self.assertEqual(expected_bitstring, actual_bitstring)
        
        self.assertEqual([letter], letters)
    
    def test_build_tree_with_exception(self):
        """
        letters = builtins.list[typing.Any]
        """
        # This test fails because function [compression.huffman.build_tree] produces [IndexError]
        compression.huffman.build_tree([])
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.huffman.huffman
    
    # region FUZZER
    
    def test_huffman_with_exception(self):
        """
        file_path = ' '
        """
        # This test fails because function [compression.huffman.huffman] produces [FileNotFoundError]
        compression.huffman.huffman(" ")
    
    def test_huffman_with_exception1(self):
        """
        file_path = '€'
        """
        # This test fails because function [compression.huffman.huffman] produces [IndexError]
        compression.huffman.huffman("../../€")
    # endregion
    
    # endregion

