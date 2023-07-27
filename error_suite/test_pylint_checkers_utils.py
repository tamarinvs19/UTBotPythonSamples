import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import pylint
import unittest
import pylint.checkers.utils


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable pylint.checkers.utils.is_builtin
    
    # region FUZZER
    
    def test_is_builtin(self):
        """
        name = 'pythön'
        """
        actual = pylint.checkers.utils.is_builtin("pythön")
        
        self.assertEqual(False, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_builtin_with_exception(self):
        """
        name = 'pfoo' (mutated from 'foo')
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        pylint.checkers.utils.is_builtin("pfoo")
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_builtin_with_exception1(self):
        """
        name = ''
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        pylint.checkers.utils.is_builtin("")
    # endregion
    
    # endregion
    
    # region Test suites for executable pylint.checkers.utils.parse_format_string
    
    # region FUZZER
    
    def test_parse_format_string(self):
        """
        format_string = 'rhlL' (mutated from 'hlL')
        """
        actual = pylint.checkers.utils.parse_format_string("rhlL")
        
        self.assertEqual((set(), 0, {}, []), actual)
    
    def test_parse_format_string1(self):
        """
        format_string = ''
        """
        actual = pylint.checkers.utils.parse_format_string("")
        
        self.assertEqual((set(), 0, {}, []), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable pylint.checkers.utils.parse_format_method_string
    
    # region FUZZER
    
    def test_parse_format_method_string(self):
        """
        format_string = 'pfoo' (mutated from 'foo')
        """
        actual = pylint.checkers.utils.parse_format_method_string("pfoo")
        
        self.assertEqual(([], 0, 0), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable pylint.checkers.utils.is_attr_protected
    
    # region FUZZER
    
    def test_is_attr_protected(self):
        """
        attrname = '__i' (mutated from '__')
        """
        actual = pylint.checkers.utils.is_attr_protected("__i")
        
        self.assertEqual(True, actual)
    
    def test_is_attr_protected1(self):
        """
        attrname = '_'
        """
        actual = pylint.checkers.utils.is_attr_protected("_")
        
        self.assertEqual(False, actual)
    
    def test_is_attr_protected2(self):
        """
        attrname = 'a__i' (mutated from '__i')
        """
        actual = pylint.checkers.utils.is_attr_protected("a__i")
        
        self.assertEqual(False, actual)
    
    def test_is_attr_protected_with_exception(self):
        """
        attrname = ''
        """
        # This test fails because function [pylint.checkers.utils.is_attr_protected] produces [IndexError]
        pylint.checkers.utils.is_attr_protected("")
    # endregion
    
    # endregion
    
    # region Test suites for executable pylint.checkers.utils.is_attr_private
    
    # region FUZZER
    
    def test_is_attr_private(self):
        """
        attrname = '' (mutated from '')
        """
        actual = pylint.checkers.utils.is_attr_private("")
        
        self.assertEqual(None, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_attr_private_with_exception(self):
        """
        attrname = '￻^_{2,10}.*[^_]+_?'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        pylint.checkers.utils.is_attr_private("￻^_{2,10}.*[^_]+_?")
    # endregion
    
    # endregion
    
    # region Test suites for executable pylint.checkers.utils._is_abstract_class_name
    
    # region FUZZER
    
    def test__is_abstract_class_name(self):
        """
        name = 'balse' (mutated from 'base')
        """
        actual = pylint.checkers.utils._is_abstract_class_name("balse")
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion

