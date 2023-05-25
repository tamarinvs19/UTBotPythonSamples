import sys
sys.path.append(r'../..')
import data_structures.queue.queue_on_list
import builtins
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

