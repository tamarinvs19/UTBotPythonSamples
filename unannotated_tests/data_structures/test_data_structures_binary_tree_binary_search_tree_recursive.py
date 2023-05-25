import sys
sys.path.append(r'..\..\..')
import types
import data_structures
import unittest
import data_structures.binary_tree.binary_search_tree_recursive


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.binary_search_tree_recursive.binary_search_tree_example
    
    # region FUZZER
    
    def test_binary_search_tree_example(self):
        actual = data_structures.binary_tree.binary_search_tree_recursive.binary_search_tree_example()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

