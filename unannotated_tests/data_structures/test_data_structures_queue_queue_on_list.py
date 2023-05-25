import sys
sys.path.append(r'..\..\..')
import data_structures.queue.queue_on_list
import builtins
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.queue.queue_on_list.__str__
    
    # region FUZZER
    
    def test___str__(self):
        """
        self = data_structures.queue.queue_on_list.Queue
        """
        queue = data_structures.queue.queue_on_list.Queue()
        
        actual = queue.__str__()
        
        self.assertEqual('<>', actual)
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_list.put
    
    # region FUZZER
    
    def test_put(self):
        """
        self = data_structures.queue.queue_on_list.Queue
        item = -1 (mutated from max)
        """
        queue = data_structures.queue.queue_on_list.Queue()
        
        actual = queue.put(-1)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_list.get
    
    # region FUZZER
    
    def test_get_with_exception(self):
        """
        self = data_structures.queue.queue_on_list.Queue
        """
        queue = data_structures.queue.queue_on_list.Queue()
        # This test fails because function [data_structures.queue.queue_on_list.get] produces [IndexError]
        queue.get()
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_list.rotate
    
    # region FUZZER
    
    def test_rotate(self):
        """
        self = data_structures.queue.queue_on_list.Queue
        rotation = min (mutated from zero)
        """
        queue = data_structures.queue.queue_on_list.Queue()
        
        actual = queue.rotate(-170141183460469231731687303715884105728)
        
        self.assertEqual(None, actual)
        
        self.assertEqual(queue, queue)
    
    def test_rotate_with_exception(self):
        """
        self = data_structures.queue.queue_on_list.Queue
        rotation = 170141183460469231731687303715884040191 (mutated from max)
        """
        queue = data_structures.queue.queue_on_list.Queue()
        # This test fails because function [data_structures.queue.queue_on_list.rotate] produces [IndexError]
        queue.rotate(170141183460469231731687303715884040191)
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_list.get_front
    
    # region FUZZER
    
    def test_get_front_with_exception(self):
        """
        self = data_structures.queue.queue_on_list.Queue
        """
        queue = data_structures.queue.queue_on_list.Queue()
        # This test fails because function [data_structures.queue.queue_on_list.get_front] produces [IndexError]
        queue.get_front()
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.queue_on_list.size
    
    # region FUZZER
    
    def test_size(self):
        """
        self = data_structures.queue.queue_on_list.Queue
        """
        queue = data_structures.queue.queue_on_list.Queue()
        
        actual = queue.size()
        
        self.assertEqual(0, actual)
        
        self.assertEqual(queue, queue)
    # endregion
    
    # endregion

