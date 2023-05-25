import sys
sys.path.append(r'..')
import builtins
import isort
import unittest
import isort.literal


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable isort.literal.assignments
    
    # region FUZZER
    
    def test_assignments(self):
        """
        code = ''
        """
        actual = isort.literal.assignments("")
        
        self.assertEqual('', actual)
    
    def test_assignments1(self):
        """
        code = ''
        """
        actual = isort.literal.assignments("")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable isort.literal.assignment
    
    # region FUZZER
    
    def test_assignment_with_exception(self):
        """
        code = 'pythön'
        sort_type = 'Trying tosort using an undefined sort_type. '
        extension = 'foo'
        """
        # This test fails because function [isort.literal.assignment] produces [ValueError]
        isort.literal.assignment("pythön", "Trying tosort using an undefined sort_type. ", "foo")
    # endregion
    
    # endregion

