import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.excel_title_to_column


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.excel_title_to_column.excel_title_to_column
    
    # region FUZZER
    
    def test_excel_title_to_column(self):
        """
        column_title = ')O'
        """
        actual = conversions.excel_title_to_column.excel_title_to_column(")O")
        
        self.assertEqual(-583, actual)
    
    def test_excel_title_to_column_with_exception(self):
        """
        column_title = '€'
        """
        # This test fails because function [conversions.excel_title_to_column.excel_title_to_column] produces [AssertionError]
        conversions.excel_title_to_column.excel_title_to_column("€")
    # endregion
    
    # endregion

