import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import scheduling
import unittest
import scheduling.highest_response_ratio_next


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable scheduling.highest_response_ratio_next.calculate_turn_around_time
    
    # region FUZZER
    
    def test_calculate_turn_around_time(self):
        """
        process_name = builtins.list[typing.Any]
        arrival_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = -70368744177665 (mutated from 170141183460469231731687233347139928063)
        """
        actual = scheduling.highest_response_ratio_next.calculate_turn_around_time([], [], [], -70368744177665)
        
        self.assertEqual([], actual)
    
    def test_calculate_turn_around_time_with_exception(self):
        """
        process_name = builtins.list[typing.Any]
        arrival_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = -170141183460469231731651274918865141760 (mutated from min)
        """
        # This test fails because function [scheduling.highest_response_ratio_next.calculate_turn_around_time] produces [OverflowError]
        scheduling.highest_response_ratio_next.calculate_turn_around_time([], [], [], -170141183460469231731651274918865141760)
    
    def test_calculate_turn_around_time_with_exception1(self):
        """
        process_name = builtins.list[typing.Any]
        arrival_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = 32770 (mutated from 2)
        """
        # This test fails because function [scheduling.highest_response_ratio_next.calculate_turn_around_time] produces [IndexError]
        scheduling.highest_response_ratio_next.calculate_turn_around_time([], [], [], 32770)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_turn_around_time_with_exception2(self):
        """
        process_name = builtins.list[typing.Any]
        arrival_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = 1073872896 (mutated from 131072)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.highest_response_ratio_next.calculate_turn_around_time([], [], [], 1073872896)
    # endregion
    
    # endregion
    
    # region Test suites for executable scheduling.highest_response_ratio_next.calculate_waiting_time
    
    # region FUZZER
    
    def test_calculate_waiting_time(self):
        """
        process_name = builtins.list[typing.Any]
        turn_around_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = -70368744177665 (mutated from 170141183460469231731687233347139928063)
        """
        actual = scheduling.highest_response_ratio_next.calculate_waiting_time([], [], [], -70368744177665)
        
        self.assertEqual([], actual)
    
    def test_calculate_waiting_time_with_exception(self):
        """
        process_name = builtins.list[typing.Any]
        turn_around_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = -170141183460469231731651274918865141760 (mutated from min)
        """
        # This test fails because function [scheduling.highest_response_ratio_next.calculate_waiting_time] produces [OverflowError]
        scheduling.highest_response_ratio_next.calculate_waiting_time([], [], [], -170141183460469231731651274918865141760)
    
    def test_calculate_waiting_time_with_exception1(self):
        """
        process_name = builtins.list[typing.Any]
        turn_around_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = 32768 (mutated from zero)
        """
        # This test fails because function [scheduling.highest_response_ratio_next.calculate_waiting_time] produces [IndexError]
        scheduling.highest_response_ratio_next.calculate_waiting_time([], [], [], 32768)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_waiting_time_with_exception2(self):
        """
        process_name = builtins.list[typing.Any]
        turn_around_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = 1208156160 (mutated from 134414336)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.highest_response_ratio_next.calculate_waiting_time([], [], [], 1208156160)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_calculate_waiting_time_with_exception3(self):
        """
        process_name = builtins.list[typing.Any]
        turn_around_time = builtins.list[typing.Any]
        burst_time = builtins.list[typing.Any]
        no_of_process = 134414592 (mutated from 134414336)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        scheduling.highest_response_ratio_next.calculate_waiting_time([], [], [], 134414592)
    # endregion
    
    # endregion

