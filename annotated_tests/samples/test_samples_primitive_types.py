import sys
sys.path.append(r'../../..')
import builtins
import datetime
import samples
import unittest
import samples.primitive_types


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.primitive_types.pretty_print
    
    # region FUZZER
    
    def test_pretty_print(self):
        """
        x = object()
        """
        x = object()
        
        actual = samples.primitive_types.pretty_print(x)
        
        self.assertEqual('I do not have any variants', actual)
        
        x_modified = object.__new__(object)
        
        self.assertTrue(isinstance(x, builtins.object))
    
    def test_pretty_print1(self):
        """
        x = datetime.datetime(1995, 4, 12)
        """
        actual = samples.primitive_types.pretty_print(datetime.datetime(1995, 4, 12))
        
        self.assertEqual('Date 1995-04-12T00:00:00', actual)
    
    def test_pretty_print2(self):
        """
        x = complex(real=float('-inf'), imag=float('-inf'))
        """
        actual = samples.primitive_types.pretty_print(complex(real=float('-inf'), imag=float('-inf')))
        
        self.assertEqual('It is complex.\nValue (-inf + -infi)', actual)
    
    def test_pretty_print3(self):
        """
        x = 170141183460469231731651274918865141759 (mutated from max)
        """
        actual = samples.primitive_types.pretty_print(170141183460469231731651274918865141759)
        
        self.assertEqual('It is integer.\nValue 170141183460469231731651274918865141759', actual)
    
    def test_pretty_print4(self):
        """
        x = builtins.list[typing.Any]
        """
        actual = samples.primitive_types.pretty_print([])
        
        self.assertEqual('It is list.\nValue []', actual)
    
    def test_pretty_print5(self):
        """
        x = 'i)'
        """
        actual = samples.primitive_types.pretty_print("i)")
        
        self.assertEqual('It is string.\nValue <<i)>>', actual)
    # endregion
    
    # endregion

