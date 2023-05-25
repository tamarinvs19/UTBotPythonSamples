import sys
sys.path.append(r'../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.huffman.parse_file
    
    # region FUZZER
    
    def test_parse_file_with_exception(self):
        """
        file_path = '€'
        """
        # This test fails because function [compression.huffman.parse_file] produces [FileNotFoundError]
        compression.huffman.parse_file("../€")
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
    
    def test_build_tree1(self):
        """
        letters = builtins.list[compression.huffman.Letter]
        """
        letter = compression.huffman.Letter("abcdefghij>klmnopqst", 0)
        letter1 = compression.huffman.Letter("abcdefghijklmnopqrst", 131072)
        letter2 = compression.huffman.Letter("abcdefghijklmnopqrst", -170141183460469231731687303715884105728)
        letter3 = compression.huffman.Letter("abcdefghijlmnopqrst", 0)
        letters = [letter, letter1, letter2, letter3]
        
        actual = compression.huffman.build_tree(letters)
        
        expected = object.__new__(compression.huffman.TreeNode)
        tree_node = object.__new__(compression.huffman.TreeNode)
        tree_node.freq = -170141183460469231731687303715884105728
        tree_node.left = letter2
        tree_node.right = letter3
        tree_node1 = object.__new__(compression.huffman.TreeNode)
        tree_node1.freq = 131072
        tree_node1.left = letter
        tree_node1.right = letter1
        expected.freq = -170141183460469231731687303715883974656
        expected.left = tree_node
        expected.right = tree_node1
        actual_freq = actual.freq
        expected_freq = expected.freq
        
        self.assertEqual(expected_freq, actual_freq)
        actual_left = actual.left
        expected_left = expected.left
        actual_freq1 = actual_left.freq
        expected_freq1 = expected_left.freq
        
        self.assertEqual(expected_freq1, actual_freq1)
        actual_left1 = actual_left.left
        expected_left1 = expected_left.left
        actual_letter = actual_left1.letter
        expected_letter = expected_left1.letter
        
        self.assertEqual(expected_letter, actual_letter)
        actual_freq2 = actual_left1.freq
        expected_freq2 = expected_left1.freq
        
        self.assertEqual(expected_freq2, actual_freq2)
        actual_bitstring = actual_left1.bitstring
        expected_bitstring = expected_left1.bitstring
        
        self.assertEqual(expected_bitstring, actual_bitstring)
        actual_right = actual_left.right
        expected_right = expected_left.right
        actual_letter1 = actual_right.letter
        expected_letter1 = expected_right.letter
        
        self.assertEqual(expected_letter1, actual_letter1)
        actual_freq3 = actual_right.freq
        expected_freq3 = expected_right.freq
        
        self.assertEqual(expected_freq3, actual_freq3)
        actual_bitstring1 = actual_right.bitstring
        expected_bitstring1 = expected_right.bitstring
        
        self.assertEqual(expected_bitstring1, actual_bitstring1)
        actual_right1 = actual.right
        expected_right1 = expected.right
        actual_freq4 = actual_right1.freq
        expected_freq4 = expected_right1.freq
        
        self.assertEqual(expected_freq4, actual_freq4)
        actual_left2 = actual_right1.left
        expected_left2 = expected_right1.left
        actual_letter2 = actual_left2.letter
        expected_letter2 = expected_left2.letter
        
        self.assertEqual(expected_letter2, actual_letter2)
        actual_freq5 = actual_left2.freq
        expected_freq5 = expected_left2.freq
        
        self.assertEqual(expected_freq5, actual_freq5)
        actual_bitstring2 = actual_left2.bitstring
        expected_bitstring2 = expected_left2.bitstring
        
        self.assertEqual(expected_bitstring2, actual_bitstring2)
        actual_right2 = actual_right1.right
        expected_right2 = expected_right1.right
        actual_letter3 = actual_right2.letter
        expected_letter3 = expected_right2.letter
        
        self.assertEqual(expected_letter3, actual_letter3)
        actual_freq6 = actual_right2.freq
        expected_freq6 = expected_right2.freq
        
        self.assertEqual(expected_freq6, actual_freq6)
        actual_bitstring3 = actual_right2.bitstring
        expected_bitstring3 = expected_right2.bitstring
        
        self.assertEqual(expected_bitstring3, actual_bitstring3)
        
        self.assertEqual([letter, letter1, letter2, letter3], letters)
    
    def test_build_tree_with_exception(self):
        """
        letters = builtins.list[compression.huffman.Letter]
        """
        # This test fails because function [compression.huffman.build_tree] produces [IndexError]
        compression.huffman.build_tree([])
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.huffman.traverse_tree
    
    # region FUZZER
    
    def test_traverse_tree(self):
        """
        root = compression.huffman.Letter
        bitstring = 'pythön'
        """
        root = compression.huffman.Letter("abcdefghijklmnopqrst", -1)
        root1 = root
        
        actual = compression.huffman.traverse_tree(root1, "pythön")
        
        expected_list = [root]
        expected_length = len(expected_list)
        actual_length = len(actual)
        
        self.assertEqual(expected_length, actual_length)
        
        index = None
        for index in range(0, expected_length, 1):
            expected_element = expected_list[index]
            actual_element = actual[index]
            actual_letter = actual_element.letter
            expected_letter = expected_element.letter
            
            self.assertEqual(expected_letter, actual_letter)
            actual_freq = actual_element.freq
            expected_freq = expected_element.freq
            
            self.assertEqual(expected_freq, actual_freq)
            actual_bitstring = actual_element.bitstring
            expected_bitstring = expected_element.bitstring
            
            self.assertEqual(expected_bitstring, actual_bitstring)
        
        self.assertEqual(root, root1)
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
    # endregion
    
    # endregion

