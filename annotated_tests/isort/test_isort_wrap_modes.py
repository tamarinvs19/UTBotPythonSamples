import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.wrap_modes


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.wrap_modes.from_string
    
    # region FUZZER
    
    def test_from_string_with_exception(self):
        """
        value = 'oo6'
        """
        # This test fails because function [isort.wrap_modes.from_string] produces [ValueError]
        isort.wrap_modes.from_string("oo6")
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.wrap_modes._wrap_mode_interface
    
    # region FUZZER
    
    def test__wrap_mode_interface(self):
        """
        statement = 'Defines the common interface used by all wrap mode functions'
        imports = 'Defines the common interface used by all wrap mode functions'
        white_space = 'abcdefghijklmnopqrst'
        indent = 'abcdefghijklmnopqrst'
        line_length = 'Defines the common interface used by all wrap mode functions'
        comments = '€'
        line_separator = 'abcdefghijklmnopqrst'
        comment_prefix = ''
        include_trailing_comma = 'Defines the common interface used by all wrap mode functions'
        remove_comments = '€'
        """
        actual = isort.wrap_modes._wrap_mode_interface("Defines the common interface used by all wrap mode functions", "Defines the common interface used by all wrap mode functions", "abcdefghijklmnopqrst", "abcdefghijklmnopqrst", "Defines the common interface used by all wrap mode functions", "€", "abcdefghijklmnopqrst", "", "Defines the common interface used by all wrap mode functions", "€")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion

