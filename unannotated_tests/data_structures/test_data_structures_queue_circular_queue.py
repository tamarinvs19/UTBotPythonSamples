import sys
sys.path.append(r'..\..\..')
import data_structures.queue.circular_queue
import builtins
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.queue.circular_queue.__len__
    
    # region FUZZER
    
    def test___len__(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(-1)
        
        actual = circular_queue.__len__()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(circular_queue, circular_queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue.is_empty
    
    # region FUZZER
    
    def test_is_empty(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(0)
        
        actual = circular_queue.is_empty()
        
        self.assertEqual(True, actual)
        
        self.assertEqual(circular_queue, circular_queue)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_empty_with_exception(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(81920)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        circular_queue.is_empty()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_empty_with_exception1(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(327680)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        circular_queue.is_empty()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_empty_with_exception2(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(1073807360)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        circular_queue.is_empty()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_empty_with_exception3(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(4259840)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        circular_queue.is_empty()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_empty_with_exception4(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(1114112)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        circular_queue.is_empty()
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue.first
    
    # region FUZZER
    
    def test_first(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(-1)
        
        actual = circular_queue.first()
        
        self.assertEqual(False, actual)
        
        self.assertEqual(circular_queue, circular_queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.circular_queue.dequeue
    
    # region FUZZER
    
    def test_dequeue_with_exception(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(-1)
        # This test fails because function [data_structures.queue.circular_queue.dequeue] produces [Exception]
        circular_queue.dequeue()
        
        self.assertEqual(circular_queue, circular_queue)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_dequeue_with_exception1(self):
        """
        self = data_structures.queue.circular_queue.CircularQueue
        """
        circular_queue = data_structures.queue.circular_queue.CircularQueue(536870913)
        circular_queue.rear = -170141183460469231731687303715884105728
        circular_queue.size = 0
        circular_queue.front = 2
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        circular_queue.dequeue()
    # endregion
    
    # endregion

