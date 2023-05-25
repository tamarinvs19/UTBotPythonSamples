import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.is_spain_national_id


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.is_spain_national_id.is_spain_national_id
    
    # region FUZZER
    
    def test_is_spain_national_id_with_exception(self):
        """
        spanish_id = ''
        """
        # This test fails because function [strings.is_spain_national_id.is_spain_national_id] produces [ValueError]
        strings.is_spain_national_id.is_spain_national_id("")
    
    def test_is_spain_national_id_with_exception1(self):
        """
        spanish_id = 'pytÚhön0'
        """
        # This test fails because function [strings.is_spain_national_id.is_spain_national_id] produces [ValueError]
        strings.is_spain_national_id.is_spain_national_id("pytÚhön0")
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_spain_national_id_with_exception2(self):
        """
        spanish_id = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.is_spain_national_id.is_spain_national_id(bytes(268435466))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_spain_national_id_with_exception3(self):
        """
        spanish_id = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.is_spain_national_id.is_spain_national_id(bytearray(268435466))
    # endregion
    
    # endregion

