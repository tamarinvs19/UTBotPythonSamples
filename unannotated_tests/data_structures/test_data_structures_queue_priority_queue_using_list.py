import sys
sys.path.append(r'..\..\..')
import data_structures
import unittest
import data_structures.queue.priority_queue_using_list


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.queue.priority_queue_using_list.fixed_priority_queue
    
    # region FUZZER
    
    def test_fixed_priority_queue_with_exception(self):
        # This test fails because function [data_structures.queue.priority_queue_using_list.fixed_priority_queue] produces [data_structures.queue.priority_queue_using_list.UnderFlowError]
        data_structures.queue.priority_queue_using_list.fixed_priority_queue()
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.queue.priority_queue_using_list.element_priority_queue
    
    # region FUZZER
    
    def test_element_priority_queue_with_exception(self):
        # This test fails because function [data_structures.queue.priority_queue_using_list.element_priority_queue] produces [data_structures.queue.priority_queue_using_list.UnderFlowError]
        data_structures.queue.priority_queue_using_list.element_priority_queue()
    # endregion
    
    # endregion

