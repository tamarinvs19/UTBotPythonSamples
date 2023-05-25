import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.output


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.output._output_as_string
    
    # region FUZZER
    
    def test__output_as_string(self):
        """
        lines = builtins.list[typing.Any]
        line_separator = 'fo'
        """
        lines = []
        
        actual = isort.output._output_as_string(lines, "fo")
        
        self.assertEqual('', actual)
        
        self.assertEqual([''], lines)
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.output._normalize_empty_lines
    
    # region FUZZER
    
    def test__normalize_empty_lines(self):
        """
        lines = builtins.list[typing.Any]
        """
        lines = []
        
        actual = isort.output._normalize_empty_lines(lines)
        
        self.assertEqual([''], actual)
        
        self.assertEqual([''], lines)
    # endregion
    
    # endregion

