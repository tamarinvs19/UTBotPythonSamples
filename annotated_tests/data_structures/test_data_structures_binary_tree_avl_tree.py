import sys
sys.path.append(r'../..')
import data_structures.binary_tree.avl_tree
import types
import builtins
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.avl_tree.get_height
    
    # region FUZZER
    
    def test_get_height(self):
        """
        self = data_structures.binary_tree.avl_tree.AVLtree
        """
        a_v_ltree = data_structures.binary_tree.avl_tree.AVLtree()
        
        actual = a_v_ltree.get_height()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(a_v_ltree, a_v_ltree)
    # endregion
    
    # endregion

