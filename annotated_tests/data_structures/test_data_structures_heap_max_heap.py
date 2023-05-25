import sys
sys.path.append(r'../..')
import builtins
import data_structures.heap.max_heap
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.heap.max_heap.insert
    
    # region FUZZER
    
    def test_insert(self):
        """
        self = data_structures.heap.max_heap.BinaryHeap
        value = -170141183460469231731687303715884105664 (mutated from min)
        """
        binary_heap = data_structures.heap.max_heap.BinaryHeap()
        
        actual = binary_heap.insert(-170141183460469231731687303715884105664)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(binary_heap, binary_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.max_heap.pop
    
    # region FUZZER
    
    def test_pop_with_exception(self):
        """
        self = data_structures.heap.max_heap.BinaryHeap
        """
        binary_heap = data_structures.heap.max_heap.BinaryHeap()
        # This test fails because function [data_structures.heap.max_heap.pop] produces [IndexError]
        binary_heap.pop()
        
        self.assertEqual(binary_heap, binary_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.max_heap.__len__
    
    # region FUZZER
    
    def test___len__(self):
        """
        self = data_structures.heap.max_heap.BinaryHeap
        """
        binary_heap = data_structures.heap.max_heap.BinaryHeap()
        
        actual = binary_heap.__len__()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(binary_heap, binary_heap)
    # endregion
    
    # endregion

