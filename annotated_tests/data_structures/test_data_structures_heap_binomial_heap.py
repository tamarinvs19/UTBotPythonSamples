import sys
sys.path.append(r'../..')
import data_structures.heap.binomial_heap
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.heap.binomial_heap.is_empty
    
    # region FUZZER
    
    def test_is_empty(self):
        """
        self = data_structures.heap.binomial_heap.BinomialHeap
        """
        binomial_heap = data_structures.heap.binomial_heap.BinomialHeap()
        
        actual = binomial_heap.is_empty()
        
        self.assertEqual(True, actual)
        
        self.assertEqual(binomial_heap, binomial_heap)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.heap.binomial_heap.__str__
    
    # region FUZZER
    
    def test___str__(self):
        """
        self = data_structures.heap.binomial_heap.BinomialHeap
        """
        binomial_heap = data_structures.heap.binomial_heap.BinomialHeap()
        
        actual = binomial_heap.__str__()
        
        self.assertEqual('', actual)
        
        self.assertEqual(binomial_heap, binomial_heap)
    # endregion
    
    # endregion

