import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.utils


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.utils.exists_case_sensitive
    
    # region FUZZER
    
    def test_exists_case_sensitive(self):
        """
        path = 'da5rin'
        """
        actual = isort.utils.exists_case_sensitive("da5rin")
        
        self.assertEqual(False, actual)
    
    def test_exists_case_sensitive_with_exception(self):
        """
        path = '€'
        """
        # This test fails because function [isort.utils.exists_case_sensitive] produces [FileNotFoundError]
        isort.utils.exists_case_sensitive("€")
    
    def test_exists_case_sensitive_with_exception1(self):
        """
        path = 170141183460469231731651274918865141759 (mutated from max)
        """
        # This test fails because function [isort.utils.exists_case_sensitive] produces [OverflowError]
        isort.utils.exists_case_sensitive(170141183460469231731651274918865141759)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_exists_case_sensitive_with_exception2(self):
        """
        path = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        isort.utils.exists_case_sensitive(bytes(268437520))
    # endregion
    
    # endregion

