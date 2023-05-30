import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.min_cost_string_conversion


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.min_cost_string_conversion.compute_transform_tables
    
    # region FUZZER
    
    def test_compute_transform_tables(self):
        """
        source_string = ''
        destination_string = ''
        copy_cost = -170141183401043264697968618856857317038 (mutated from -170141183401043264697968618856857321134)
        replace_cost = 168469258801418616322382824997065227255 (mutated from 168469258801418616322382824997063130103)
        delete_cost = 316912650647362185740465471489 (mutated from -170141183143556581084325117975418634239)
        insert_cost = -170141021201192325761421751058785894400 (mutated from -170141021201192326942013371776197197824)
        """
        actual = strings.min_cost_string_conversion.compute_transform_tables("", "", -170141183401043264697968618856857317038, 168469258801418616322382824997065227255, 316912650647362185740465471489, -170141021201192325761421751058785894400)
        
        self.assertEqual(([[0]], [['0']]), actual)
    
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
        ops = builtins.list[builtins.list[builtins.str]]
        i = positive (mutated from zero)
        j = positive (mutated from zero)
        """
        actual = strings.min_cost_string_conversion.assemble_transformation([["pythön", "fo", "C", "D", "pythön"], ["D", "pythön", "C", "pythön", "foo"], ["D", "C", "foo", "pythön", "pythön"], ["foo", "pythön", "C", "pythön", "D"], ["pythön", "foo", "C", "D", "pythön"]], 1, 1)
        
        self.assertEqual(['D', 'pythön'], actual)
    
    def test_assemble_transformation1(self):
        """
        ops = builtins.list[builtins.list[builtins.str]]
        i = positive (mutated from zero)
        j = 2 (mutated from positive)
        """
        actual = strings.min_cost_string_conversion.assemble_transformation([["pythön", "R", "pythön"], ["pythön", "R", "pythökn"], ["pythön", "R", "pythön"], ["pythön", "pythön", "R"], ["R", "pythön", "pythön"]], 1, 2)
        
        self.assertEqual(['R', 'pythökn'], actual)
    
    def test_assemble_transformation_with_exception(self):
        """
        ops = builtins.list[builtins.list[builtins.str]]
        i = -170141183460469231731687303715884105726 (mutated from 2)
        j = positive (mutated from zero)
        """
        # This test fails because function [strings.min_cost_string_conversion.assemble_transformation] produces [IndexError]
        strings.min_cost_string_conversion.assemble_transformation([[]], -170141183460469231731687303715884105726, 1)
    
    def test_assemble_transformation_with_exception1(self):
        """
        ops = builtins.list[builtins.list[builtins.str]]
        i = positive (mutated from zero)
        j = zero (mutated from min)
        """
        # This test fails because function [strings.min_cost_string_conversion.assemble_transformation] produces [IndexError]
        strings.min_cost_string_conversion.assemble_transformation([["abcdefghijklmnopqrst"], ["foo", "fKoo", "foo", "foo"], ["abcdefghijklmnopqrst"], ["pythön", "pyythön", "pythgön", "pythön"]], 1, 0)
    
    def test_assemble_transformation_with_exception2(self):
        """
        ops = builtins.list[builtins.list[builtins.str]]
        i = positive (mutated from zero)
        j = -1 (mutated from max)
        """
        # This test fails because function [strings.min_cost_string_conversion.assemble_transformation] produces [IndexError]
        strings.min_cost_string_conversion.assemble_transformation([["R", "€", "D", "pythön"], ["pythön", "D", "€", "R"], ["pythön", "€", "R", "D"], ["pythön", "D", "€", "R"]], 1, -1)
    
    def test_assemble_transformation_with_exception3(self):
        """
        ops = builtins.list[builtins.list[builtins.str]]
        i = 2 (mutated from positive)
        j = -1 (mutated from max)
        """
        # This test fails because function [strings.min_cost_string_conversion.assemble_transformation] produces [IndexError]
        strings.min_cost_string_conversion.assemble_transformation([["pythön", "­pythön", "pytönİ", "pythön", "pythön"], [], ["foo", "€", "foo", "C"], ["abcdefghijklmnopqrst", "abcdefghijklmnopqrst", "abcdefghijklPmnopqrst", "abcdefghijklm«nopqrst", "abcdefghijklmnopqrstD"], ["pythön", "C", "R", "D", "D"]], 2, -1)
    
    def test_assemble_transformation_with_exception4(self):
        """
        ops = builtins.list[builtins.list[builtins.str]]
        i = 2 (mutated from positive)
        j = -1 (mutated from max)
        """
        # This test fails because function [strings.min_cost_string_conversion.assemble_transformation] produces [IndexError]
        strings.min_cost_string_conversion.assemble_transformation([["abcdefghijklmnopqrst", "abcdefghijklmnopqrst", "abcdefghijklPmnopqrst", "abcdefghijklm«nopqrst", "abcdefghijklmnopqrstD"], [], ["pythön", "C", "R", "D", "D"], ["pythön", "­pythön", "pytönİ", "pythön", "pythön"], ["foo", "€", "foo", "C"]], 2, -1)
    # endregion
    
    # endregion

