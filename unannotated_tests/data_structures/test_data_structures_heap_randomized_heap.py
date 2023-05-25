import sys
sys.path.append(r'..\..\..')
import builtins
import data_structures.heap.randomized_heap
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.heap.randomized_heap.insert
    
    # region FUZZER
    
    def test_insert(self):
        """
        self = data_structures.heap.randomized_heap.RandomizedHeap[T]
        value = 'pyhön'
        """
        randomized_heap = data_structures.heap.randomized_heap.RandomizedHeap()
        
        actual = randomized_heap.insert("pyhön")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(randomized_heap, randomized_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.randomized_heap.pop
    
    # region FUZZER
    
    def test_pop_with_exception(self):
        """
        self = data_structures.heap.randomized_heap.RandomizedHeap[builtins.bool]
        """
        randomized_heap = data_structures.heap.randomized_heap.RandomizedHeap()
        # This test fails because function [data_structures.heap.randomized_heap.pop] produces [IndexError]
        randomized_heap.pop()
        
        self.assertEqual(randomized_heap, randomized_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.randomized_heap.top
    
    # region FUZZER
    
    def test_top_with_exception(self):
        """
        self = data_structures.heap.randomized_heap.RandomizedHeap[builtins.bool]
        """
        randomized_heap = data_structures.heap.randomized_heap.RandomizedHeap()
        # This test fails because function [data_structures.heap.randomized_heap.top] produces [IndexError]
        randomized_heap.top()
        
        self.assertEqual(randomized_heap, randomized_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.randomized_heap.clear
    
    # region FUZZER
    
    def test_clear(self):
        """
        self = data_structures.heap.randomized_heap.RandomizedHeap[builtins.bool]
        """
        randomized_heap = data_structures.heap.randomized_heap.RandomizedHeap()
        
        actual = randomized_heap.clear()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(randomized_heap, randomized_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.randomized_heap.to_sorted_list
    
    # region FUZZER
    
    def test_to_sorted_list(self):
        """
        self = data_structures.heap.randomized_heap.RandomizedHeap[builtins.bool]
        """
        randomized_heap = data_structures.heap.randomized_heap.RandomizedHeap()
        
        actual = randomized_heap.to_sorted_list()
        
        self.assertEqual([], actual)
        
        self.assertEqual(randomized_heap, randomized_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.randomized_heap.__bool__
    
    # region FUZZER
    
    def test___bool__(self):
        """
        self = data_structures.heap.randomized_heap.RandomizedHeap[builtins.bool]
        """
        randomized_heap = data_structures.heap.randomized_heap.RandomizedHeap()
        
        actual = randomized_heap.__bool__()
        
        self.assertEqual(False, actual)
        
        self.assertEqual(randomized_heap, randomized_heap)
    # endregion
    
    # endregion

