import sys
sys.path.append(r'..\..\..')
import data_structures.binary_tree.binary_tree_path_sum
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.binary_tree_path_sum.path_sum
    
    # region FUZZER
    
    def test_path_sum(self):
        """
        self = data_structures.binary_tree.binary_tree_path_sum.BinaryTreePathSum
        node = data_structures.binary_tree.binary_tree_path_sum.Node
        target = -1 (mutated from max)
        """
        binary_tree_path_sum = data_structures.binary_tree.binary_tree_path_sum.BinaryTreePathSum()
        node = data_structures.binary_tree.binary_tree_path_sum.Node(-1)
        node1 = node
        
        actual = binary_tree_path_sum.path_sum(node1, -1)
        
        self.assertEqual(1, actual)
        
        self.assertEqual(node, node1)
        
        self.assertEqual(binary_tree_path_sum, binary_tree_path_sum)
    # endregion
    
    # endregion

