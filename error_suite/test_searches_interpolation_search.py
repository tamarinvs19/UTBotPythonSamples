import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import searches
import unittest
import searches.interpolation_search


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable searches.interpolation_search.interpolation_search
    
    # region FUZZER
    
    def test_interpolation_search(self):
        """
        sorted_collection = ''
        item = max
        """
        actual = searches.interpolation_search.interpolation_search("", 170141183460469231731687303715884105727)
        
        self.assertEqual(None, actual)
    
    def test_interpolation_search1(self):
        """
        sorted_collection = 'b' (mutated from '')
        item = 170141183460469231731687162978395734015 (mutated from 170141183460469231731687162978395750399)
        """
        actual = searches.interpolation_search.interpolation_search("b", 170141183460469231731687162978395734015)
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.interpolation_search.interpolation_search_by_recursion
    
    # region FUZZER
    
    def test_interpolation_search_by_recursion(self):
        """
        sorted_collection = 'pythön'
        item = min
        left = zero
        right = zero (mutated from min)
        """
        actual = searches.interpolation_search.interpolation_search_by_recursion("pythön", -170141183460469231731687303715884105728, 0, 0)
        
        self.assertEqual(None, actual)
    
    def test_interpolation_search_by_recursion_with_exception(self):
        """
        sorted_collection = 'fo'
        item = zero
        left = 2 (mutated from positive)
        right = 2 (mutated from positive)
        """
        # This test fails because function [searches.interpolation_search.interpolation_search_by_recursion] produces [IndexError]
        searches.interpolation_search.interpolation_search_by_recursion("fo", 0, 2, 2)
    # endregion
    
    # endregion

