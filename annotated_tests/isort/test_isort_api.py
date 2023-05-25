import sys
sys.path.append(r'..')
import builtins
import pathlib
import isort
import unittest
import isort.api


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.api.sort_code_string
    
    # region FUZZER
    
    def test_sort_code_string(self):
        """
        code = '€'
        """
        actual = isort.api.sort_code_string("€")
        
        self.assertEqual('€', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.api.check_code_string
    
    # region FUZZER
    
    def test_check_code_string(self):
        """
        code = '€'
        """
        actual = isort.api.check_code_string("€")
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.api.check_file
    
    # region FUZZER
    
    def test_check_file_with_exception(self):
        """
        filename = pathlib.Path
        """
        filename = pathlib.Path()
        # This test fails because function [isort.api.check_file] produces [PermissionError]
        isort.api.check_file(filename)
    # endregion
    
    # endregion

