import sys
sys.path.append(r'..\..\..')
import builtins
import types
import data_structures
import unittest
import data_structures.trie.radix_tree


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.trie.radix_tree.test_trie
    
    # region FUZZER
    
    def test_test_trie(self):
        actual = data_structures.trie.radix_tree.test_trie()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.trie.radix_tree.pytests
    
    # region FUZZER
    
    def test_pytests(self):
        actual = data_structures.trie.radix_tree.pytests()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.trie.radix_tree.main
    
    # region FUZZER
    
    def test_main(self):
        actual = data_structures.trie.radix_tree.main()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

