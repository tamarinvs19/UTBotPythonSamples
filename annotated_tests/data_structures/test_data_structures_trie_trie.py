import sys
sys.path.append(r'../..')
import data_structures.trie.trie
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.trie.trie.print_words
    
    # region FUZZER
    
    def test_print_words(self):
        """
        node = data_structures.trie.trie.TrieNode
        word = 'abcdefghijklmnopqrs'
        """
        node = data_structures.trie.trie.TrieNode()
        node1 = node
        
        actual = data_structures.trie.trie.print_words(node1, "abcdefghijklmnopqrs")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(node, node1)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.trie.trie.test_trie
    
    # region FUZZER
    
    def test_test_trie(self):
        actual = data_structures.trie.trie.test_trie()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.trie.trie.print_results
    
    # region FUZZER
    
    def test_print_results(self):
        """
        msg = 'works!'
        passes = zero (mutated from min)
        """
        actual = data_structures.trie.trie.print_results("works!", True)
        
        self.assertEqual(None, actual)
    
    def test_print_results_with_exception(self):
        """
        msg = 'fo'
        passes = zero (mutated from min)
        """
        # This test fails because function [data_structures.trie.trie.print_results] produces [UnicodeEncodeError]
        data_structures.trie.trie.print_results("fo", True)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.trie.trie.pytests
    
    # region FUZZER
    
    def test_pytests(self):
        actual = data_structures.trie.trie.pytests()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.trie.trie.main
    
    # region FUZZER
    
    def test_main(self):
        actual = data_structures.trie.trie.main()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

