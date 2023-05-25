import sys
sys.path.append(r'../../..')
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
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_excel_title_to_column_with_exception1(self):
        """
        column_title = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.excel_title_to_column.excel_title_to_column(bytes(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_excel_title_to_column_with_exception2(self):
        """
        column_title = builtins.bytes
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.excel_title_to_column.excel_title_to_column(bytes(33554433))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_excel_title_to_column_with_exception3(self):
        """
        column_title = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.excel_title_to_column.excel_title_to_column(bytearray(1073741824))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_excel_title_to_column_with_exception4(self):
        """
        column_title = builtins.bytearray
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        conversions.excel_title_to_column.excel_title_to_column(bytearray(33554433))
    # endregion
    
    # endregion

