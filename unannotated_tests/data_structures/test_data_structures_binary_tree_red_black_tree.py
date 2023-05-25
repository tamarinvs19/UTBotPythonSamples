import sys
sys.path.append(r'..\..\..')
import builtins
import types
import data_structures
import unittest
import data_structures.binary_tree.red_black_tree


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_rotations
    
    # region FUZZER
    
    def test_test_rotations(self):
        actual = data_structures.binary_tree.red_black_tree.test_rotations()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_insertion_speed
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_test_insertion_speed_with_exception(self):
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        data_structures.binary_tree.red_black_tree.test_insertion_speed()
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_insert
    
    # region FUZZER
    
    def test_test_insert(self):
        actual = data_structures.binary_tree.red_black_tree.test_insert()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_insert_and_search
    
    # region FUZZER
    
    def test_test_insert_and_search(self):
        actual = data_structures.binary_tree.red_black_tree.test_insert_and_search()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_insert_delete
    
    # region FUZZER
    
    def test_test_insert_delete(self):
        actual = data_structures.binary_tree.red_black_tree.test_insert_delete()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_floor_ceil
    
    # region FUZZER
    
    def test_test_floor_ceil(self):
        actual = data_structures.binary_tree.red_black_tree.test_floor_ceil()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_min_max
    
    # region FUZZER
    
    def test_test_min_max(self):
        actual = data_structures.binary_tree.red_black_tree.test_min_max()
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_tree_traversal
    
    # region FUZZER
    
    def test_test_tree_traversal(self):
        actual = data_structures.binary_tree.red_black_tree.test_tree_traversal()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.test_tree_chaining
    
    # region FUZZER
    
    def test_test_tree_chaining(self):
        actual = data_structures.binary_tree.red_black_tree.test_tree_chaining()
        
        self.assertEqual(True, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.print_results
    
    # region FUZZER
    
    def test_print_results(self):
        """
        msg = 'works!'
        passes = zero (mutated from min)
        """
        actual = data_structures.binary_tree.red_black_tree.print_results("works!", True)
        
        self.assertEqual(None, actual)
    
    def test_print_results_with_exception(self):
        """
        msg = 'fo'
        passes = zero (mutated from min)
        """
        # This test fails because function [data_structures.binary_tree.red_black_tree.print_results] produces [UnicodeEncodeError]
        data_structures.binary_tree.red_black_tree.print_results("fo", True)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.pytests
    
    # region FUZZER
    
    def test_pytests(self):
        actual = data_structures.binary_tree.red_black_tree.pytests()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.red_black_tree.main
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_main_with_exception(self):
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        data_structures.binary_tree.red_black_tree.main()
    # endregion
    
    # endregion

