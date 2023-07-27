import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import datetime
import caldav
import unittest
import caldav.elements.cdav


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable caldav.elements.cdav._to_utc_date_string
    
    # region FUZZER
    
    def test__to_utc_date_string_with_exception(self):
        """
        ts = datetime.datetime(1, 1, 1)
        """
        # This test fails because function [caldav.elements.cdav._to_utc_date_string] produces [OverflowError]
        caldav.elements.cdav._to_utc_date_string(datetime.datetime(1, 1, 1))
    # endregion
    
    # endregion

