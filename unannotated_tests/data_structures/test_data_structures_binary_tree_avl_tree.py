import sys
sys.path.append(r'..\..\..')
import data_structures.binary_tree.avl_tree
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.avl_tree.is_empty
    
    # region FUZZER
    
    def test_is_empty(self):
        """
        self = data_structures.binary_tree.avl_tree.MyQueue
        """
        my_queue = data_structures.binary_tree.avl_tree.MyQueue()
        
        actual = my_queue.is_empty()
        
        self.assertEqual(True, actual)
        
        self.assertEqual(my_queue, my_queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.avl_tree.pop
    
    # region FUZZER
    
    def test_pop_with_exception(self):
        """
        self = data_structures.binary_tree.avl_tree.MyQueue
        """
        my_queue = data_structures.binary_tree.avl_tree.MyQueue()
        # This test fails because function [data_structures.binary_tree.avl_tree.pop] produces [IndexError]
        my_queue.pop()
        
        self.assertEqual(my_queue, my_queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.avl_tree.count
    
    # region FUZZER
    
    def test_count(self):
        """
        self = data_structures.binary_tree.avl_tree.MyQueue
        """
        my_queue = data_structures.binary_tree.avl_tree.MyQueue()
        
        actual = my_queue.count()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(my_queue, my_queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.avl_tree.print_queue
    
    # region FUZZER
    
    def test_print_queue(self):
        """
        self = data_structures.binary_tree.avl_tree.MyQueue
        """
        my_queue = data_structures.binary_tree.avl_tree.MyQueue()
        
        actual = my_queue.print_queue()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(my_queue, my_queue)
    # endregion
    
    # endregion

