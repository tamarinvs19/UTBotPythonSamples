import sys
sys.path.append(r'..\..\..')
import data_structures.queue.linked_queue
import types
import builtins
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.queue.linked_queue.__len__
    
    # region FUZZER
    
    def test___len__(self):
        """
        self = data_structures.queue.linked_queue.LinkedQueue
        """
        linked_queue = data_structures.queue.linked_queue.LinkedQueue()
        
        actual = linked_queue.__len__()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(linked_queue, linked_queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.linked_queue.__str__
    
    # region FUZZER
    
    def test___str__(self):
        """
        self = 'oo6'
        """
        actual = "oo6".__str__()
        
        self.assertEqual('o <- o <- 6', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.linked_queue.is_empty
    
    # region FUZZER
    
    def test_is_empty(self):
        """
        self = data_structures.queue.linked_queue.LinkedQueue
        """
        linked_queue = data_structures.queue.linked_queue.LinkedQueue()
        
        actual = linked_queue.is_empty()
        
        self.assertEqual(True, actual)
        
        self.assertEqual(linked_queue, linked_queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.linked_queue.get
    
    # region FUZZER
    
    def test_get_with_exception(self):
        """
        self = data_structures.queue.linked_queue.LinkedQueue
        """
        linked_queue = data_structures.queue.linked_queue.LinkedQueue()
        # This test fails because function [data_structures.queue.linked_queue.get] produces [IndexError]
        linked_queue.get()
        
        self.assertEqual(linked_queue, linked_queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.linked_queue.clear
    
    # region FUZZER
    
    def test_clear(self):
        """
        self = data_structures.queue.linked_queue.LinkedQueue
        """
        linked_queue = data_structures.queue.linked_queue.LinkedQueue()
        
        actual = linked_queue.clear()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(linked_queue, linked_queue)
    # endregion
    
    # endregion

