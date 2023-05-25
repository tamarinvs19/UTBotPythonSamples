import sys
sys.path.append(r'..\..\..')
import data_structures.queue.double_ended_queue
import builtins
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.queue.double_ended_queue.pop
    
    # region FUZZER
    
    def test_pop_with_exception(self):
        """
        self = data_structures.queue.double_ended_queue.Deque
        """
        deque = data_structures.queue.double_ended_queue.Deque()
        # This test fails because function [data_structures.queue.double_ended_queue.pop] produces [AssertionError]
        deque.pop()
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.double_ended_queue.popleft
    
    # region FUZZER
    
    def test_popleft_with_exception(self):
        """
        self = data_structures.queue.double_ended_queue.Deque
        """
        deque = data_structures.queue.double_ended_queue.Deque()
        # This test fails because function [data_structures.queue.double_ended_queue.popleft] produces [AssertionError]
        deque.popleft()
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.double_ended_queue.is_empty
    
    # region FUZZER
    
    def test_is_empty(self):
        """
        self = data_structures.queue.double_ended_queue.Deque
        """
        deque = data_structures.queue.double_ended_queue.Deque()
        
        actual = deque.is_empty()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion

