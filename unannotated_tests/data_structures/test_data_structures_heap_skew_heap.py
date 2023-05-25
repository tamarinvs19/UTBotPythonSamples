import sys
sys.path.append(r'..\..\..')
import data_structures.heap.skew_heap
import types
import builtins
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.heap.skew_heap.__bool__
    
    # region FUZZER
    
    def test___bool__(self):
        """
        self = data_structures.heap.skew_heap.SkewHeap[builtins.bool]
        """
        skew_heap = data_structures.heap.skew_heap.SkewHeap()
        
        actual = skew_heap.__bool__()
        
        self.assertEqual(False, actual)
        
        self.assertEqual(skew_heap, skew_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.skew_heap.insert
    
    # region FUZZER
    
    def test_insert(self):
        """
        self = data_structures.heap.skew_heap.SkewHeap[T]
        value = 'pyhön'
        """
        skew_heap = data_structures.heap.skew_heap.SkewHeap()
        
        actual = skew_heap.insert("pyhön")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(skew_heap, skew_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.skew_heap.pop
    
    # region FUZZER
    
    def test_pop_with_exception(self):
        """
        self = data_structures.heap.skew_heap.SkewHeap[builtins.bool]
        """
        skew_heap = data_structures.heap.skew_heap.SkewHeap()
        # This test fails because function [data_structures.heap.skew_heap.pop] produces [IndexError]
        skew_heap.pop()
        
        self.assertEqual(skew_heap, skew_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.skew_heap.top
    
    # region FUZZER
    
    def test_top_with_exception(self):
        """
        self = data_structures.heap.skew_heap.SkewHeap[builtins.bool]
        """
        skew_heap = data_structures.heap.skew_heap.SkewHeap()
        # This test fails because function [data_structures.heap.skew_heap.top] produces [IndexError]
        skew_heap.top()
        
        self.assertEqual(skew_heap, skew_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.skew_heap.clear
    
    # region FUZZER
    
    def test_clear(self):
        """
        self = data_structures.heap.skew_heap.SkewHeap[builtins.bool]
        """
        skew_heap = data_structures.heap.skew_heap.SkewHeap()
        
        actual = skew_heap.clear()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(skew_heap, skew_heap)
    # endregion
    
    # endregion

