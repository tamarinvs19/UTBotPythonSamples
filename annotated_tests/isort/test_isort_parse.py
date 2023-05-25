import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.parse


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.parse._infer_line_separator
    
    # region FUZZER
    
    def test__infer_line_separator(self):
        """
        contents = '9r'
        """
        actual = isort.parse._infer_line_separator("9r")
        
        self.assertEqual('\n', actual)
    
    def test__infer_line_separator1(self):
        """
        contents = '\r'
        """
        actual = isort.parse._infer_line_separator("\r")
        
        self.assertEqual('\r', actual)
    
    def test__infer_line_separator2(self):
        """
        contents = '\r\n'
        """
        actual = isort.parse._infer_line_separator("\r\n")
        
        self.assertEqual('\r\n', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.parse._normalize_line
    
    # region FUZZER
    
    def test__normalize_line(self):
        """
        raw_line = ' .0impot '
        """
        actual = isort.parse._normalize_line(" .0impot ")
        
        self.assertEqual((' .0impot ', ' .0impot '), actual)
    # endregion
    
    # endregion

