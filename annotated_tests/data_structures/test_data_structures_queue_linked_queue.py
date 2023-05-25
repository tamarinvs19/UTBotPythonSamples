import sys
sys.path.append(r'../..')
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
        self = data_structures.queue.linked_queue.LinkedQueue
        """
        linked_queue = data_structures.queue.linked_queue.LinkedQueue()
        
        actual = linked_queue.__str__()
        
        self.assertEqual('', actual)
        
        self.assertEqual(linked_queue, linked_queue)
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

