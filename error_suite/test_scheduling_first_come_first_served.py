import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import scheduling
import unittest
import scheduling.first_come_first_served


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable scheduling.first_come_first_served.calculate_waiting_times
    
    # region FUZZER
    
    def test_calculate_waiting_times(self):
        """
        duration_times = builtins.list[builtins.int]
        """
        actual = scheduling.first_come_first_served.calculate_waiting_times([2, 2, 0, 170141183460469231731687303715884105727])
        
        self.assertEqual([0, 2, 4, 4], actual)
    
    def test_calculate_waiting_times1(self):
        """
        duration_times = builtins.list[builtins.int]
        """
        actual = scheduling.first_come_first_served.calculate_waiting_times([170141183460469231731687303715884105727])
        
        self.assertEqual([0], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.first_come_first_served.calculate_turnaround_times
    
    # region FUZZER
    
    def test_calculate_turnaround_times(self):
        """
        duration_times = builtins.list[builtins.int]
        waiting_times = builtins.list[builtins.int]
        """
        actual = scheduling.first_come_first_served.calculate_turnaround_times([-1, -1, -170141183460469231731687303715884105728, -1], [170141183460469231731687303715884105727, 1, -1, 1, 1])
        
        self.assertEqual([170141183460469231731687303715884105726, 0, -170141183460469231731687303715884105729, 0], actual)
    
    def test_calculate_turnaround_times1(self):
        """
        duration_times = builtins.list[builtins.int]
        waiting_times = builtins.list[builtins.int]
        """
        actual = scheduling.first_come_first_served.calculate_turnaround_times([], [])
        
        self.assertEqual([], actual)
    
    def test_calculate_turnaround_times_with_exception(self):
        """
        duration_times = builtins.list[builtins.int]
        waiting_times = builtins.list[builtins.int]
        """
        # This test fails because function [scheduling.first_come_first_served.calculate_turnaround_times] produces [IndexError]
        scheduling.first_come_first_served.calculate_turnaround_times([0, 0, 1], [170141183460469231731687303715884105727])
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.first_come_first_served.calculate_average_turnaround_time
    
    # region FUZZER
    
    def test_calculate_average_turnaround_time(self):
        """
        turnaround_times = builtins.list[builtins.int]
        """
        actual = scheduling.first_come_first_served.calculate_average_turnaround_time([-1, -170141183460469231731687303715884105728, -1, -1])
        
        self.assertEqual(-4.253529586511731e+37, actual)
    
    def test_calculate_average_turnaround_time_with_exception(self):
        """
        turnaround_times = builtins.list[builtins.int]
        """
        # This test fails because function [scheduling.first_come_first_served.calculate_average_turnaround_time] produces [ZeroDivisionError]
        scheduling.first_come_first_served.calculate_average_turnaround_time([])
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.first_come_first_served.calculate_average_waiting_time
    
    # region FUZZER
    
    def test_calculate_average_waiting_time(self):
        """
        waiting_times = builtins.list[builtins.int]
        """
        actual = scheduling.first_come_first_served.calculate_average_waiting_time([-1, -170141183460469231731687303715884105728, -1, -1])
        
        self.assertEqual(-4.253529586511731e+37, actual)
    
    def test_calculate_average_waiting_time_with_exception(self):
        """
        waiting_times = builtins.list[builtins.int]
        """
        # This test fails because function [scheduling.first_come_first_served.calculate_average_waiting_time] produces [ZeroDivisionError]
        scheduling.first_come_first_served.calculate_average_waiting_time([])
    # endregion
    
    # endregion

