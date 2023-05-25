import sys
sys.path.append(r'..\..\..')
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

