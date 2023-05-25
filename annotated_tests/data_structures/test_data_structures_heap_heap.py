import sys
sys.path.append(r'../..')
import data_structures.heap.heap
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.heap.heap.__repr__
    
    # region FUZZER
    
    def test___repr__(self):
        """
        self = data_structures.heap.heap.Heap
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.__repr__()
        
        self.assertEqual('[]', actual)
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.heap.parent_index
    
    # region FUZZER
    
    def test_parent_index(self):
        """
        self = data_structures.heap.heap.Heap
        child_idx = 66 (mutated from 2)
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.parent_index(66)
        
        self.assertEqual(32, actual)
        
        self.assertEqual(heap, heap)
    
    def test_parent_index1(self):
        """
        self = data_structures.heap.heap.Heap
        child_idx = -170141183460469231731687303715884105662 (mutated from 66)
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.parent_index(-170141183460469231731687303715884105662)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.heap.left_child_idx
    
    # region FUZZER
    
    def test_left_child_idx(self):
        """
        self = data_structures.heap.heap.Heap
        parent_idx = 64 (mutated from zero)
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.left_child_idx(64)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(heap, heap)
    
    def test_left_child_idx1(self):
        """
        self = data_structures.heap.heap.Heap
        parent_idx = -170141183460469231731687303715884105664 (mutated from 64)
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.left_child_idx(-170141183460469231731687303715884105664)
        
        self.assertEqual(-340282366920938463463374607431768211327, actual)
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.heap.right_child_idx
    
    # region FUZZER
    
    def test_right_child_idx(self):
        """
        self = data_structures.heap.heap.Heap
        parent_idx = 64 (mutated from zero)
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.right_child_idx(64)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(heap, heap)
    
    def test_right_child_idx1(self):
        """
        self = data_structures.heap.heap.Heap
        parent_idx = -170141183460469231731687303715884105664 (mutated from 64)
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.right_child_idx(-170141183460469231731687303715884105664)
        
        self.assertEqual(-340282366920938463463374607431768211326, actual)
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.heap.max_heapify
    
    # region FUZZER
    
    def test_max_heapify(self):
        """
        self = data_structures.heap.heap.Heap
        index = 170141183460469231731687303715884105663 (mutated from -65)
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.max_heapify(170141183460469231731687303715884105663)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(heap, heap)
    
    def test_max_heapify_with_exception(self):
        """
        self = data_structures.heap.heap.Heap
        index = -65 (mutated from -1)
        """
        heap = data_structures.heap.heap.Heap()
        # This test fails because function [data_structures.heap.heap.max_heapify] produces [IndexError]
        heap.max_heapify(-65)
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.heap.build_max_heap
    
    # region FUZZER
    
    def test_build_max_heap(self):
        """
        self = data_structures.heap.heap.Heap
        collection = builtins.tuple[typing.Any, ...]
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.build_max_heap(())
        
        self.assertEqual(None, actual)
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.heap.extract_max
    
    # region FUZZER
    
    def test_extract_max_with_exception(self):
        """
        self = data_structures.heap.heap.Heap
        """
        heap = data_structures.heap.heap.Heap()
        # This test fails because function [data_structures.heap.heap.extract_max] produces [Exception]
        heap.extract_max()
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.heap.insert
    
    # region FUZZER
    
    def test_insert(self):
        """
        self = data_structures.heap.heap.Heap
        value = float('-inf')
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.insert(float('-inf'))
        
        self.assertEqual(None, actual)
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.heap.heap_sort
    
    # region FUZZER
    
    def test_heap_sort(self):
        """
        self = data_structures.heap.heap.Heap
        """
        heap = data_structures.heap.heap.Heap()
        
        actual = heap.heap_sort()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(heap, heap)
    # endregion
    
    # endregion

