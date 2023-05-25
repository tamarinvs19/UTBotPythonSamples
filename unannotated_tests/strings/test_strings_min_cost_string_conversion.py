import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.min_cost_string_conversion


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.min_cost_string_conversion.compute_transform_tables
    
    # region FUZZER
    
    def test_compute_transform_tables_with_exception(self):
        """
        source_string = '€'
        destination_string = 'foo'
        copy_cost = 2 (mutated from positive)
        replace_cost = 2 (mutated from positive)
        delete_cost = zero
        insert_cost = max
        """
        # This test fails because function [strings.min_cost_string_conversion.compute_transform_tables] produces [ValueError]
        strings.min_cost_string_conversion.compute_transform_tables("€", "foo", 2, 2, 0, 170141183460469231731687303715884105727)
    
    def test_compute_transform_tables_with_exception1(self):
        """
        source_string = ''
        destination_string = '0'
        copy_cost = 16777218 (mutated from 2)
        replace_cost = -1 (mutated from zero)
        delete_cost = -170141183460469231731687303715883843584 (mutated from min)
        insert_cost = min
        """
        # This test fails because function [strings.min_cost_string_conversion.compute_transform_tables] produces [ValueError]
        strings.min_cost_string_conversion.compute_transform_tables("", "0", 16777218, -1, -170141183460469231731687303715883843584, -170141183460469231731687303715884105728)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.min_cost_string_conversion.assemble_transformation
    
    # region FUZZER
    
    def test_assemble_transformation(self):
        """
        ops = builtins.list[builtins.list[typing.Any]]
        i = zero (mutated from min)
        j = zero
        """
        actual = strings.min_cost_string_conversion.assemble_transformation([[], [], [], []], 0, 0)
        
        self.assertEqual([], actual)
    
    def test_assemble_transformation_with_exception(self):
        """
        ops = builtins.list[typing.Any]
        i = 2 (mutated from positive)
        j = zero
        """
        # This test fails because function [strings.min_cost_string_conversion.assemble_transformation] produces [IndexError]
        strings.min_cost_string_conversion.assemble_transformation([], 2, 0)
    
    def test_assemble_transformation_with_exception1(self):
        """
        ops = builtins.list[builtins.list[builtins.str]]
        i = positive (mutated from zero)
        j = zero (mutated from min)
        """
        # This test fails because function [strings.min_cost_string_conversion.assemble_transformation] produces [IndexError]
        strings.min_cost_string_conversion.assemble_transformation([["abcdefghijklmnopqrst"], ["foo", "fKoo", "foo", "foo"], ["abcdefghijklmnopqrst"], ["pythön", "pyythön", "pythgön", "pythön"]], 1, 0)
    # endregion
    
    # endregion

