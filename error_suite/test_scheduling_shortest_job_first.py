import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import scheduling
import unittest
import scheduling.shortest_job_first


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable scheduling.shortest_job_first.calculate_waitingtime
    
    # region FUZZER
    
    def test_calculate_waitingtime(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = zero
        """
        actual = scheduling.shortest_job_first.calculate_waitingtime([170141183460469231731687303715884105727, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728, 999999998], [-1, 1000000000], 0)
        
        self.assertEqual([], actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_waitingtime_with_exception(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = -1 (mutated from zero)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_waitingtime([-170141183460469231731687303715884105728, -1, -268435457, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [170141183460469231731687303715884105727, 1000000000], -1)
    
    def test_calculate_waitingtime_with_exception1(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = 16385 (mutated from positive)
        """
        # This test fails because function [scheduling.shortest_job_first.calculate_waitingtime] produces [IndexError]
        scheduling.shortest_job_first.calculate_waitingtime([999999999, -170141183460469231731687303715884105728], [1000000000, 2, 1000000000], 16385)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_waitingtime_with_exception2(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = 2 (mutated from positive)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_waitingtime([-1, -1, 1, 2], [999999998, 999999999, 999999999, 0, 1], 2)
    
    def test_calculate_waitingtime_with_exception3(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = max
        """
        # This test fails because function [scheduling.shortest_job_first.calculate_waitingtime] produces [OverflowError]
        scheduling.shortest_job_first.calculate_waitingtime([2, -1, 1000000000, 999999999, 170141183460469231731687303715884105727], [1, 1, 65], 170141183460469231731687303715884105727)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_waitingtime_with_exception4(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = 999999967 (mutated from 999999999)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_waitingtime([1000000000, -1], [-170141183460469231731687303715884105728], 999999967)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_waitingtime_with_exception5(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = -19807040628566084398385987585 (mutated from -1)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_waitingtime([2, 0, 999999998, 2], [-1, 1000000000, 1000000000, 999999998, -170141183460469231731687303715884105728], -19807040628566084398385987585)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_waitingtime_with_exception6(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = zero
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_waitingtime([170141183460469231731687303715884105727, 0], [-170141183460469231731687303715884105728, 999999998, 170141183460469231731687303715884105727, -1, -1], 0)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_waitingtime_with_exception7(self):
        """
        arrival_time = builtins.list[builtins.int]
        burst_time = builtins.list[builtins.int]
        no_of_processes = 65536 (mutated from zero)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_waitingtime([170141183460469231731686740765930684415, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728, 999999998], [1000000000, -1], 65536)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.shortest_job_first.calculate_turnaroundtime
    
    # region FUZZER
    
    def test_calculate_turnaroundtime(self):
        """
        burst_time = builtins.list[builtins.int]
        no_of_processes = zero
        waiting_time = builtins.list[builtins.int]
        """
        actual = scheduling.shortest_job_first.calculate_turnaroundtime([-1], 0, [1, 1])
        
        self.assertEqual([], actual)
    
    def test_calculate_turnaroundtime1(self):
        """
        burst_time = builtins.list[builtins.int]
        no_of_processes = positive (mutated from zero)
        waiting_time = builtins.list[builtins.int]
        """
        actual = scheduling.shortest_job_first.calculate_turnaroundtime([-1, -170141183460469231731687303715884105728, 1], 1, [-1, -170141183460469231731687303715884105728])
        
        self.assertEqual([-2], actual)
    
    def test_calculate_turnaroundtime_with_exception(self):
        """
        burst_time = builtins.list[builtins.int]
        no_of_processes = max
        waiting_time = builtins.list[builtins.int]
        """
        # This test fails because function [scheduling.shortest_job_first.calculate_turnaroundtime] produces [OverflowError]
        scheduling.shortest_job_first.calculate_turnaroundtime([-1, -1, 1, -1], 170141183460469231731687303715884105727, [-170141183460469231731687303715884105728, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728])
    
    def test_calculate_turnaroundtime_with_exception1(self):
        """
        burst_time = builtins.list[builtins.int]
        no_of_processes = 2097153 (mutated from positive)
        waiting_time = builtins.list[builtins.int]
        """
        # This test fails because function [scheduling.shortest_job_first.calculate_turnaroundtime] produces [IndexError]
        scheduling.shortest_job_first.calculate_turnaroundtime([1], 2097153, [1, -170141183460469231731687303715884105728, 170141183460469231731687303715884105727, -1, 1])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_turnaroundtime_with_exception2(self):
        """
        burst_time = builtins.list[builtins.int]
        no_of_processes = -170141183460469231731687303715884105727 (mutated from positive)
        waiting_time = builtins.list[builtins.int]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_turnaroundtime([-170141183460449888918573469649088806911], -170141183460469231731687303715884105727, [170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_turnaroundtime_with_exception3(self):
        """
        burst_time = builtins.list[builtins.int]
        no_of_processes = -1 (mutated from zero)
        waiting_time = builtins.list[builtins.int]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_turnaroundtime([-1, 1], -1, [0, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_turnaroundtime_with_exception4(self):
        """
        burst_time = builtins.list[builtins.int]
        no_of_processes = positive (mutated from zero)
        waiting_time = builtins.list[builtins.int]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_turnaroundtime([-170141183460449888918573469649088806911], 1, [170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727])
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_turnaroundtime_with_exception5(self):
        """
        burst_time = builtins.list[builtins.int]
        no_of_processes = max
        waiting_time = builtins.list[builtins.int]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.shortest_job_first.calculate_turnaroundtime([-170141183460469231731687303715884105728, -1, -170141183460469231731687303715884105728], 170141183460469231731687303715884105727, [170141183460469231731687303715884105727, -1208925819614629174706177])
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.shortest_job_first.calculate_average_times
    
    # region FUZZER
    
    def test_calculate_average_times(self):
        """
        waiting_time = builtins.list[builtins.int]
        turn_around_time = builtins.list[builtins.int]
        no_of_processes = -170141183440662191103121219317498118144 (mutated from min)
        """
        actual = scheduling.shortest_job_first.calculate_average_times([-1, -1, -1, 1], [170141183460469231731687303715884105727, -170141183460469231731687303715884105728, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], -170141183440662191103121219317498118144)
        
        self.assertEqual(None, actual)
    
    def test_calculate_average_times1(self):
        """
        waiting_time = builtins.list[builtins.int]
        turn_around_time = builtins.list[builtins.int]
        no_of_processes = positive (mutated from zero)
        """
        actual = scheduling.shortest_job_first.calculate_average_times([-1], [1, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 170141183460469231731687303715884105727], 1)
        
        self.assertEqual(None, actual)
    
    def test_calculate_average_times_with_exception(self):
        """
        waiting_time = builtins.list[builtins.int]
        turn_around_time = builtins.list[builtins.int]
        no_of_processes = 19807040628566084398385987584 (mutated from -170141183440662191103121219317498118144)
        """
        # This test fails because function [scheduling.shortest_job_first.calculate_average_times] produces [IndexError]
        scheduling.shortest_job_first.calculate_average_times([1, -1, -1, -1], [170141183460469231731687303715884105727, -170141183460469231731687303715884105728, -1, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], 19807040628566084398385987584)
    
    def test_calculate_average_times_with_exception1(self):
        """
        waiting_time = builtins.list[builtins.int]
        turn_around_time = builtins.list[builtins.int]
        no_of_processes = zero (mutated from min)
        """
        # This test fails because function [scheduling.shortest_job_first.calculate_average_times] produces [ZeroDivisionError]
        scheduling.shortest_job_first.calculate_average_times([-1, -1, 1, 0, 1], [-170141183460469231731687303715884105728, 1, 0, 1, 170141183460469231731687303715884105727], 0)
    
    def test_calculate_average_times_with_exception2(self):
        """
        waiting_time = builtins.list[builtins.int]
        turn_around_time = builtins.list[builtins.int]
        no_of_processes = 159507359494189904748456847233641349119 (mutated from max)
        """
        # This test fails because function [scheduling.shortest_job_first.calculate_average_times] produces [IndexError]
        scheduling.shortest_job_first.calculate_average_times([], [0, -170141183460469231731687303715884105728, -1, -1], 159507359494189904748456847233641349119)
    # endregion
    
    # endregion

