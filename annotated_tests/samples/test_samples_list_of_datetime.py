import sys
sys.path.append(r'../../..')
import builtins
import datetime
import types
import samples
import unittest
import samples.list_of_datetime


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.list_of_datetime.get_data_labels
    
    # region FUZZER
    
    def test_get_data_labels(self):
        """
        dates = builtins.list[typing.Any]
        """
        dates = []
        
        actual = samples.list_of_datetime.get_data_labels(dates)
        
        self.assertEqual(None, actual)
        
        time = datetime.time(b'\x17;\x00\x00\x00\x00')
        
        self.assertEqual([time], dates)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_data_labels_with_exception(self):
        """
        dates = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        samples.list_of_datetime.get_data_labels(bytearray(268435456))
    # endregion
    
    # endregion

