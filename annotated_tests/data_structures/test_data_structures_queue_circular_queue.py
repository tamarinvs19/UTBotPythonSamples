import sys
sys.path.append(r'../..')
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

