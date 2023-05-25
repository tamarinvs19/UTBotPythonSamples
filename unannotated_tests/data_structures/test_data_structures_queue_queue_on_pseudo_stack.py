import sys
sys.path.append(r'..\..\..')
import data_structures.queue.queue_on_pseudo_stack
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.queue.queue_on_pseudo_stack.__str__
    
    # region FUZZER
    
    def test___str__(self):
        """
        self = data_structures.queue.queue_on_pseudo_stack.Queue
        """
        queue = data_structures.queue.queue_on_pseudo_stack.Queue()
        
        actual = queue.__str__()
        
        self.assertEqual('<>', actual)
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_pseudo_stack.put
    
    # region FUZZER
    
    def test_put(self):
        """
        self = data_structures.queue.queue_on_pseudo_stack.Queue
        item = -170141183460469231731687303715884105664 (mutated from min)
        """
        queue = data_structures.queue.queue_on_pseudo_stack.Queue()
        
        actual = queue.put(-170141183460469231731687303715884105664)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_pseudo_stack.get
    
    # region FUZZER
    
    def test_get_with_exception(self):
        """
        self = data_structures.queue.queue_on_pseudo_stack.Queue
        """
        queue = data_structures.queue.queue_on_pseudo_stack.Queue()
        # This test fails because function [data_structures.queue.queue_on_pseudo_stack.get] produces [IndexError]
        queue.get()
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_pseudo_stack.rotate
    
    # region FUZZER
    
    def test_rotate(self):
        """
        self = data_structures.queue.queue_on_pseudo_stack.Queue
        rotation = -170141183460469231731687303715884105662 (mutated from 66)
        """
        queue = data_structures.queue.queue_on_pseudo_stack.Queue()
        
        actual = queue.rotate(-170141183460469231731687303715884105662)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(queue, queue)
    
    def test_rotate_with_exception(self):
        """
        self = data_structures.queue.queue_on_pseudo_stack.Queue
        rotation = 66 (mutated from 2)
        """
        queue = data_structures.queue.queue_on_pseudo_stack.Queue()
        # This test fails because function [data_structures.queue.queue_on_pseudo_stack.rotate] produces [IndexError]
        queue.rotate(66)
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_pseudo_stack.front
    
    # region FUZZER
    
    def test_front_with_exception(self):
        """
        self = data_structures.queue.queue_on_pseudo_stack.Queue
        """
        queue = data_structures.queue.queue_on_pseudo_stack.Queue()
        # This test fails because function [data_structures.queue.queue_on_pseudo_stack.front] produces [IndexError]
        queue.front()
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_pseudo_stack.size
    
    # region FUZZER
    
    def test_size(self):
        """
        self = data_structures.queue.queue_on_pseudo_stack.Queue
        """
        queue = data_structures.queue.queue_on_pseudo_stack.Queue()
        
        actual = queue.size()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion

