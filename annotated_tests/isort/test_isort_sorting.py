import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.sorting


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.sorting._atoi
    
    # region FUZZER
    
    def test__atoi(self):
        """
        text = 'oo6'
        """
        actual = isort.sorting._atoi("oo6")
        
        self.assertEqual('oo6', actual)
    
    def test__atoi_with_exception(self):
        """
        text = '₈'
        """
        # This test fails because function [isort.sorting._atoi] produces [ValueError]
        isort.sorting._atoi("₈")
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.sorting._natural_keys
    
    # region FUZZER
    
    def test__natural_keys(self):
        """
        text = '€'
        """
        actual = isort.sorting._natural_keys("€")
        
        self.assertEqual(['€'], actual)
    
    def test__natural_keys_with_exception(self):
        """
        text = '⁸'
        """
        # This test fails because function [isort.sorting._natural_keys] produces [ValueError]
        isort.sorting._natural_keys("⁸")
    # endregion
    
    # endregion

