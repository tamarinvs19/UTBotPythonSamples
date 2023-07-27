import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import scheduling.multi_level_feedback_queue
import collections
import scheduling
import unittest


class TestMLFQ(unittest.TestCase):
    # region Test suites for executable scheduling.multi_level_feedback_queue.calculate_sequence_of_finish_queue
    
    # region FUZZER
    
    def test_calculate_sequence_of_finish_queue(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        """
        deque = collections.deque()
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(4194304, [-1, -1, 0], deque, 1)
        deque1 = collections.deque()
        deque2 = collections.deque([])
        m_l_f_q.current_time = -170141183460469231731687303715884105728
        m_l_f_q.time_slices = [0, 0, 0, 0]
        m_l_f_q.number_of_queues = 0
        m_l_f_q.finish_queue = deque1
        m_l_f_q.ready_queue = deque2
        
        actual = m_l_f_q.calculate_sequence_of_finish_queue()
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.multi_level_feedback_queue.calculate_waiting_time
    
    # region FUZZER
    
    def test_calculate_waiting_time(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        queue = builtins.list[scheduling.multi_level_feedback_queue.Process]
        """
        deque = collections.deque(tuple())
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(-170141183460469231731687303715884105728, [-1, -1, -1], deque, -1)
        deque1 = collections.deque()
        deque2 = collections.deque()
        m_l_f_q.current_time = 0
        m_l_f_q.time_slices = [1, 170141183460469231731687303715884105727, 0, -1, -170141183460469231731687303715884105728]
        m_l_f_q.ready_queue = deque1
        m_l_f_q.finish_queue = deque2
        m_l_f_q.number_of_queues = -1
        process = scheduling.multi_level_feedback_queue.Process("foo", -1, -1)
        process.waiting_time = -1
        process.process_name = "foo"
        process.stop_time = 0
        process.burst_time = -170141183460469231731687303715884105728
        process.turnaround_time = -170141183460469231731687303715884105728
        process.arrival_time = 0
        process1 = scheduling.multi_level_feedback_queue.Process("pythön", 1, 170141183460469231731110842963580682239)
        process1.stop_time = -170141183460469231731687303715884105728
        process1.turnaround_time = -170141183460469231731687303715884105728
        process1.arrival_time = -1
        process1.process_name = "foo"
        process1.waiting_time = -170141183460469231731687303715884105728
        process1.burst_time = 170141183460469231731687303715884105727
        process2 = scheduling.multi_level_feedback_queue.Process("", 0, -1)
        process2.arrival_time = 1
        process2.turnaround_time = -1
        process2.process_name = "pythön"
        process2.burst_time = -1
        process2.waiting_time = -170141183460469231731687303715884105728
        process2.stop_time = -1
        queue = [process, process1, process2]
        
        actual = m_l_f_q.calculate_waiting_time(queue)
        
        self.assertEqual([-1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.multi_level_feedback_queue.calculate_turnaround_time
    
    # region FUZZER
    
    def test_calculate_turnaround_time(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        queue = builtins.list[scheduling.multi_level_feedback_queue.Process]
        """
        deque = collections.deque(tuple())
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(-170141183460469231731687303715884105728, [-1, -1, -1], deque, -1)
        deque1 = collections.deque()
        deque2 = collections.deque()
        m_l_f_q.current_time = 0
        m_l_f_q.time_slices = [1, 170141183460469231731687303715884105727, 0, -1, -170141183460469231731687303715884105728]
        m_l_f_q.ready_queue = deque1
        m_l_f_q.finish_queue = deque2
        m_l_f_q.number_of_queues = -1
        process = scheduling.multi_level_feedback_queue.Process("foo", -1, -1)
        process.waiting_time = -1
        process.process_name = "foo"
        process.stop_time = 0
        process.burst_time = -170141183460469231731687303715884105728
        process.turnaround_time = -170141183460469231731687303715884105728
        process.arrival_time = 0
        process1 = scheduling.multi_level_feedback_queue.Process("pythön", 1, 170141183460469231731110842963580682239)
        process1.stop_time = -170141183460469231731687303715884105728
        process1.turnaround_time = -170141183460469231731687303715884105728
        process1.arrival_time = -1
        process1.process_name = "foo"
        process1.waiting_time = -170141183460469231731687303715884105728
        process1.burst_time = 170141183460469231731687303715884105727
        process2 = scheduling.multi_level_feedback_queue.Process("", 0, -1)
        process2.arrival_time = 1
        process2.turnaround_time = -1
        process2.process_name = "pythön"
        process2.burst_time = -1
        process2.waiting_time = -170141183460469231731687303715884105728
        process2.stop_time = -1
        queue = [process, process1, process2]
        
        actual = m_l_f_q.calculate_turnaround_time(queue)
        
        self.assertEqual([-170141183460469231731687303715884105728, -170141183460469231731687303715884105728, -1], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.multi_level_feedback_queue.calculate_completion_time
    
    # region FUZZER
    
    def test_calculate_completion_time(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        queue = builtins.list[scheduling.multi_level_feedback_queue.Process]
        """
        deque = collections.deque(tuple())
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(-170141183460469231731687303715884105728, [-1, -1, -1], deque, -1)
        deque1 = collections.deque()
        deque2 = collections.deque()
        m_l_f_q.current_time = 0
        m_l_f_q.time_slices = [1, 170141183460469231731687303715884105727, 0, -1, -170141183460469231731687303715884105728]
        m_l_f_q.ready_queue = deque1
        m_l_f_q.finish_queue = deque2
        m_l_f_q.number_of_queues = -1
        process = scheduling.multi_level_feedback_queue.Process("foo", -1, -1)
        process.waiting_time = -1
        process.process_name = "foo"
        process.stop_time = 0
        process.burst_time = -170141183460469231731687303715884105728
        process.turnaround_time = -170141183460469231731687303715884105728
        process.arrival_time = 0
        process1 = scheduling.multi_level_feedback_queue.Process("pythön", 1, 170141183460469231731110842963580682239)
        process1.stop_time = -170141183460469231731687303715884105728
        process1.turnaround_time = -170141183460469231731687303715884105728
        process1.arrival_time = -1
        process1.process_name = "foo"
        process1.waiting_time = -170141183460469231731687303715884105728
        process1.burst_time = 170141183460469231731687303715884105727
        process2 = scheduling.multi_level_feedback_queue.Process("", 0, -1)
        process2.arrival_time = 1
        process2.turnaround_time = -1
        process2.process_name = "pythön"
        process2.burst_time = -1
        process2.waiting_time = -170141183460469231731687303715884105728
        process2.stop_time = -1
        queue = [process, process1, process2]
        
        actual = m_l_f_q.calculate_completion_time(queue)
        
        self.assertEqual([0, -170141183460469231731687303715884105728, -1], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.multi_level_feedback_queue.calculate_remaining_burst_time_of_processes
    
    # region FUZZER
    
    def test_calculate_remaining_burst_time_of_processes(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        queue = collections.deque[scheduling.multi_level_feedback_queue.Process]
        """
        deque = collections.deque()
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(-170141183460469231731687303715884105728, [0, -170141183460469231731687303715884105728, 0, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728], deque, 1)
        chain_map = collections.ChainMap()
        chain_map.maps = []
        deque1 = collections.deque(chain_map)
        deque2 = collections.deque()
        m_l_f_q.current_time = 0
        m_l_f_q.finish_queue = deque1
        m_l_f_q.time_slices = [1, -170141183460469231731687303715884105728]
        m_l_f_q.number_of_queues = -268435457
        m_l_f_q.ready_queue = deque2
        queue = collections.deque()
        
        actual = m_l_f_q.calculate_remaining_burst_time_of_processes(queue)
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.multi_level_feedback_queue.update_waiting_time
    
    # region FUZZER
    
    def test_update_waiting_time(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        process = scheduling.multi_level_feedback_queue.Process
        """
        deque = collections.deque()
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(-170141183460469231731687303715884105728, [-1, -170141183460469231731687303715884105728, 0, 0, 1], deque, 1)
        deque1 = collections.deque()
        deque2 = collections.deque()
        m_l_f_q.ready_queue = deque1
        m_l_f_q.finish_queue = deque2
        m_l_f_q.time_slices = [-1, 170141183460469231731687303715884105727, 1, -170141183460469231731687303715884105728]
        m_l_f_q.number_of_queues = 170141183460469231731687303715884105727
        m_l_f_q.current_time = -1
        process = scheduling.multi_level_feedback_queue.Process("foo", -1, 170141183460469231731687303715884105727)
        process.burst_time = 0
        process.arrival_time = -170141183460469231731687303715884105728
        process.process_name = ""
        process.turnaround_time = 0
        process.stop_time = 170141183460469231731687303715884105727
        process.waiting_time = 1
        process1 = process
        
        actual = m_l_f_q.update_waiting_time(process1)
        
        self.assertEqual(-170141183460469231731687303715884105727, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.multi_level_feedback_queue.first_come_first_served
    
    # region FUZZER
    
    def test_first_come_first_served(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        ready_queue = collections.deque[scheduling.multi_level_feedback_queue.Process]
        """
        deque = collections.deque()
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(1, [0, 1, 0, 170141183460469231731687303715884105727, 1], deque, -170141183460469231731687303715884105728)
        chain_map = collections.ChainMap()
        chain_map.maps = []
        deque1 = collections.deque(chain_map)
        deque2 = collections.deque()
        m_l_f_q.current_time = 0
        m_l_f_q.finish_queue = deque1
        m_l_f_q.time_slices = [-170141183460469231731687303715884105728, 1]
        m_l_f_q.number_of_queues = -268435457
        m_l_f_q.ready_queue = deque2
        ready_queue = collections.deque()
        
        actual = m_l_f_q.first_come_first_served(ready_queue)
        
        expected = collections.deque()
        self.assertEqual(expected, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.multi_level_feedback_queue.round_robin
    
    # region FUZZER
    
    def test_round_robin(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        ready_queue = collections.deque[scheduling.multi_level_feedback_queue.Process]
        time_slice = 170141183459850261712044613578434543615 (mutated from max)
        """
        deque = collections.deque()
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(-170141183460469231731687303715884105728, [1], deque, 1)
        deque1 = collections.deque()
        deque2 = collections.deque()
        m_l_f_q.ready_queue = deque1
        m_l_f_q.finish_queue = deque2
        m_l_f_q.number_of_queues = -1
        m_l_f_q.time_slices = [-170141183460469231731687303715884105728]
        m_l_f_q.current_time = -1
        ready_queue = collections.deque()
        
        actual = m_l_f_q.round_robin(ready_queue, 170141183459850261712044613578434543615)
        
        deque3 = collections.deque()
        self.assertEqual((deque3, ready_queue), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.multi_level_feedback_queue.multi_level_feedback_queue
    
    # region FUZZER
    
    def test_multi_level_feedback_queue(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        """
        deque = collections.deque(set())
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(170141102330830817125005607926878961663, [2, 0], deque, 1)
        deque1 = collections.deque()
        chain_map = collections.ChainMap()
        chain_map.maps = []
        deque2 = collections.deque(chain_map)
        m_l_f_q.finish_queue = deque1
        m_l_f_q.current_time = 0
        m_l_f_q.number_of_queues = 0
        m_l_f_q.ready_queue = deque2
        m_l_f_q.time_slices = [-1]
        
        actual = m_l_f_q.multi_level_feedback_queue()
        
        self.assertEqual(deque1, actual)
    
    def test_multi_level_feedback_queue1(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        """
        deque = collections.deque({})
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(2, [1], deque, -170141183460469231731687303715884105728)
        deque1 = collections.deque()
        m_l_f_q.ready_queue = deque1
        
        actual = m_l_f_q.multi_level_feedback_queue()
        
        expected = collections.deque()
        self.assertEqual(expected, actual)
    
    def test_multi_level_feedback_queue_with_exception(self):
        """
        self = scheduling.multi_level_feedback_queue.MLFQ
        """
        deque = collections.deque()
        m_l_f_q = scheduling.multi_level_feedback_queue.MLFQ(-4194305, [0, 2, 170141183460469231731687303715884105727], deque, 1)
        deque1 = collections.deque()
        deque2 = collections.deque([])
        m_l_f_q.current_time = 170141183460469231731687303715884105727
        m_l_f_q.time_slices = [1, 1, 1, 1]
        m_l_f_q.number_of_queues = 170141183460469231731687303715884105727
        m_l_f_q.finish_queue = deque1
        m_l_f_q.ready_queue = deque2
        # This test fails because function [scheduling.multi_level_feedback_queue.multi_level_feedback_queue] produces [IndexError]
        m_l_f_q.multi_level_feedback_queue()
    # endregion
    
    # endregion

