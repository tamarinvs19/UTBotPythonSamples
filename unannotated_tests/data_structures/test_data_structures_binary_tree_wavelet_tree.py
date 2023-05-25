import sys
sys.path.append(r'..\..\..')
import builtins
import data_structures.binary_tree.wavelet_tree
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.wavelet_tree.build_tree
    
    # region FUZZER
    
    def test_build_tree_with_exception(self):
        """
        arr = builtins.list[typing.Any]
        """
        # This test fails because function [data_structures.binary_tree.wavelet_tree.build_tree] produces [ValueError]
        data_structures.binary_tree.wavelet_tree.build_tree([])
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.wavelet_tree.rank_till_index
    
    # region FUZZER
    
    def test_rank_till_index(self):
        """
        node = data_structures.binary_tree.wavelet_tree.Node
        num = min
        index = -170141183460469231731687303715884104704 (mutated from min)
        """
        node = data_structures.binary_tree.wavelet_tree.Node(3)
        node1 = node
        
        actual = data_structures.binary_tree.wavelet_tree.rank_till_index(node1, -170141183460469231731687303715884105728, -170141183460469231731687303715884104704)
        
        self.assertEqual(0, actual)
        
        self.assertEqual(node, node1)
    
    def test_rank_till_index1(self):
        """
        node = data_structures.binary_tree.wavelet_tree.Node
        num = min
        index = 4398046512384 (mutated from -170141183460469231731687299317837593344)
        """
        node = data_structures.binary_tree.wavelet_tree.Node(3)
        node1 = node
        
        actual = data_structures.binary_tree.wavelet_tree.rank_till_index(node1, -170141183460469231731687303715884105728, 4398046512384)
        
        self.assertEqual(0, actual)
        
        self.assertEqual(node, node1)
    # endregion
    
    # endregion

