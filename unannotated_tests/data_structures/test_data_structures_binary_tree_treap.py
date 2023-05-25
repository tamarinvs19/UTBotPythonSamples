import sys
sys.path.append(r'..\..\..')
import data_structures.binary_tree.treap
import types
import builtins
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.treap.split
    
    # region FUZZER
    
    def test_split(self):
        """
        root = data_structures.binary_tree.treap.Node
        value = -170141183460469231731687303715884105727 (mutated from positive)
        """
        root = data_structures.binary_tree.treap.Node()
        root1 = root
        
        actual = data_structures.binary_tree.treap.split(root1, -170141183460469231731687303715884105727)
        
        self.assertEqual((None, None), actual)
        
        self.assertEqual(root, root1)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.treap.merge
    
    # region FUZZER
    
    def test_merge(self):
        """
        left = data_structures.binary_tree.treap.Node
        right = data_structures.binary_tree.treap.Node
        """
        left = data_structures.binary_tree.treap.Node()
        left1 = left
        right = data_structures.binary_tree.treap.Node()
        right1 = right
        
        actual = data_structures.binary_tree.treap.merge(left1, right1)
        
        self.assertEqual(left, actual)
        
        self.assertEqual(left, left1)
        
        self.assertEqual(right, right1)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.treap.insert
    
    # region FUZZER
    
    def test_insert(self):
        """
        root = data_structures.binary_tree.treap.Node
        value = -170141183460469231731687303715884105727 (mutated from positive)
        """
        root = data_structures.binary_tree.treap.Node()
        root1 = root
        
        actual = data_structures.binary_tree.treap.insert(root1, -170141183460469231731687303715884105727)
        
        expected = object.__new__(data_structures.binary_tree.treap.Node)
        expected.value = -170141183460469231731687303715884105727
        expected.prior = 0.6279668851791987
        expected.left = None
        expected.right = None
        actual_value = actual.value
        expected_value = expected.value
        
        self.assertEqual(expected_value, actual_value)
        actual_prior = actual.prior
        expected_prior = expected.prior
        
        self.assertEqual(expected_prior, actual_prior)
        actual_left = actual.left
        expected_left = expected.left
        
        self.assertEqual(expected_left, actual_left)
        actual_right = actual.right
        expected_right = expected.right
        
        self.assertEqual(expected_right, actual_right)
        
        self.assertEqual(root, root1)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.treap.erase
    
    # region FUZZER
    
    def test_erase(self):
        """
        root = data_structures.binary_tree.treap.Node
        value = max (mutated from -1)
        """
        root = data_structures.binary_tree.treap.Node()
        root1 = root
        
        actual = data_structures.binary_tree.treap.erase(root1, 170141183460469231731687303715884105727)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(root, root1)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.treap.inorder
    
    # region FUZZER
    
    def test_inorder(self):
        """
        root = data_structures.binary_tree.treap.Node
        """
        root = data_structures.binary_tree.treap.Node()
        root1 = root
        
        actual = data_structures.binary_tree.treap.inorder(root1)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(root, root1)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.treap.main
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_main_with_exception(self):
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        data_structures.binary_tree.treap.main()
    # endregion
    
    # endregion

