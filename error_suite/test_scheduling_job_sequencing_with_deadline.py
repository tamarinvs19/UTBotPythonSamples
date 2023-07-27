import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import scheduling
import unittest
import scheduling.job_sequencing_with_deadline


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines
    
    # region FUZZER
    
    def test_job_sequencing_with_deadlines(self):
        """
        num_jobs = 295147905179352825857 (mutated from positive)
        jobs = builtins.list[builtins.list[builtins.int]]
        """
        actual = scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines(295147905179352825857, [[-170141183460469231731687303715884105728, 2, -1], [-1, -2, 2], [1, 0, -1]])
        
        self.assertEqual([1, -1], actual)
    
    def test_job_sequencing_with_deadlines1(self):
        """
        num_jobs = 258 (mutated from 2)
        jobs = builtins.list[builtins.list[builtins.int]]
        """
        actual = scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines(258, [[3, -2, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [3, -2, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [3, -2, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [3, -2, -170141183460469231731687303715884105728, -170141183460469231731687303715884105728]])
        
        self.assertEqual([0, 0], actual)
    
    def test_job_sequencing_with_deadlines_with_exception(self):
        """
        num_jobs = -134217729 (mutated from -1)
        jobs = builtins.list[typing.Any]
        """
        # This test fails because function [scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines] produces [ValueError]
        scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines(-134217729, [])
    
    def test_job_sequencing_with_deadlines_with_exception1(self):
        """
        num_jobs = -8796093022209 (mutated from -1)
        jobs = builtins.list[builtins.list[typing.Any]]
        """
        # This test fails because function [scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines] produces [IndexError]
        scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines(-8796093022209, [[], [], []])
    
    def test_job_sequencing_with_deadlines_with_exception2(self):
        """
        num_jobs = -1 (mutated from max)
        jobs = builtins.list[builtins.list[builtins.int]]
        """
        # This test fails because function [scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines] produces [OverflowError]
        scheduling.job_sequencing_with_deadline.job_sequencing_with_deadlines(-1, [[170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [1, -1, 0, -2, 3], [-1, -170141183460469231731687303715884105728, -1, -2, -2], [1, -170141183460469231731687303715884105728, 0, 170141183460469231731687303715884105727, 0], [-1, -2, -1, 1, 1]])
    # endregion
    
    # endregion

