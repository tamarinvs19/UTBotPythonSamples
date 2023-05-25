import sys
sys.path.append(r'..\..\..')
import data_structures.binary_tree.binary_tree_node_sum
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.binary_tree_node_sum.depth_first_search
    
    # region FUZZER
    
    def test_depth_first_search(self):
        """
        self = data_structures.binary_tree.binary_tree_node_sum.BinaryTreeNodeSum
        node = data_structures.binary_tree.binary_tree_node_sum.Node
        """
        node = data_structures.binary_tree.binary_tree_node_sum.Node(-170141183460469231731687303715884105728)
        binary_tree_node_sum = data_structures.binary_tree.binary_tree_node_sum.BinaryTreeNodeSum(node)
        node1 = data_structures.binary_tree.binary_tree_node_sum.Node(0)
        node2 = node1
        
        actual = binary_tree_node_sum.depth_first_search(node2)
        
        self.assertEqual(0, actual)
        
        self.assertEqual(node1, node2)
        
        self.assertEqual(binary_tree_node_sum, binary_tree_node_sum)
    # endregion
    
    # endregion

