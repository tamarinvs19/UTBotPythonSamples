import sys
sys.path.append(r'../..')
import builtins
import data_structures.queue.circular_queue_linked_list
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.queue.circular_queue_linked_list.create_linked_list
    
    # region FUZZER
    
    def test_create_linked_list(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        initial_capacity = -170141183460469231731687303715884105664 (mutated from min)
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        
        actual = circular_queue_linked_list.create_linked_list(-170141183460469231731687303715884105664)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(circular_queue_linked_list, circular_queue_linked_list)
    
    def test_create_linked_list1(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        initial_capacity = 64 (mutated from -170141183460469231731687303715884105664)
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        
        actual = circular_queue_linked_list.create_linked_list(64)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(circular_queue_linked_list, circular_queue_linked_list)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_create_linked_list_with_exception(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        initial_capacity = 5316911983139663491615228241121378368 (mutated from 64)
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        circular_queue_linked_list.create_linked_list(5316911983139663491615228241121378368)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue_linked_list.is_empty
    
    # region FUZZER
    
    def test_is_empty(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        
        actual = circular_queue_linked_list.is_empty()
        
        self.assertEqual(True, actual)
        
        self.assertEqual(circular_queue_linked_list, circular_queue_linked_list)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue_linked_list.first
    
    # region FUZZER
    
    def test_first_with_exception(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        # This test fails because function [data_structures.queue.circular_queue_linked_list.first] produces [Exception]
        circular_queue_linked_list.first()
        
        self.assertEqual(circular_queue_linked_list, circular_queue_linked_list)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue_linked_list.enqueue
    
    # region FUZZER
    
    def test_enqueue(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        data = object()
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        data = object()
        
        actual = circular_queue_linked_list.enqueue(data)
        
        self.assertEqual(None, actual)
        
        data_modified = object.__new__(object)
        
        self.assertTrue(isinstance(data, builtins.object))
        
        self.assertEqual(circular_queue_linked_list, circular_queue_linked_list)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue_linked_list.dequeue
    
    # region FUZZER
    
    def test_dequeue_with_exception(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        # This test fails because function [data_structures.queue.circular_queue_linked_list.dequeue] produces [Exception]
        circular_queue_linked_list.dequeue()
        
        self.assertEqual(circular_queue_linked_list, circular_queue_linked_list)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue_linked_list.check_can_perform_operation
    
    # region FUZZER
    
    def test_check_can_perform_operation_with_exception(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        # This test fails because function [data_structures.queue.circular_queue_linked_list.check_can_perform_operation] produces [Exception]
        circular_queue_linked_list.check_can_perform_operation()
        
        self.assertEqual(circular_queue_linked_list, circular_queue_linked_list)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue_linked_list.check_is_full
    
    # region FUZZER
    
    def test_check_is_full(self):
        """
        self = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList
        """
        circular_queue_linked_list = data_structures.queue.circular_queue_linked_list.CircularQueueLinkedList()
        
        actual = circular_queue_linked_list.check_is_full()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(circular_queue_linked_list, circular_queue_linked_list)
    # endregion
    
    # endregion

