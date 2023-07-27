import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import searches
import unittest
import searches.binary_search


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable searches.binary_search.bisect_left
    
    # region FUZZER
    
    def test_bisect_left(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from zero)
        """
        actual = searches.binary_search.bisect_left([36028797018963970, -1, 3, 170141183460469231731687303715884105727], -1)
        
        self.assertEqual(0, actual)
    
    def test_bisect_left1(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = max (mutated from -1)
        """
        actual = searches.binary_search.bisect_left([36028797018963970, -1, 3, 170141183460469231731687303715884105727], 170141183460469231731687303715884105727)
        
        self.assertEqual(3, actual)
    
    def test_bisect_left2(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = 16 (mutated from zero)
        """
        actual = searches.binary_search.bisect_left([-1, -1, -1, -1, -1], 16)
        
        self.assertEqual(5, actual)
    
    def test_bisect_left3(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from zero)
        lo = zero (mutated from min)
        hi = zero
        """
        actual = searches.binary_search.bisect_left([2, -1, 3, 170141183460469231731687303715884105727], -1, 0, 0)
        
        self.assertEqual(0, actual)
    
    def test_bisect_left_with_exception(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from max)
        lo = 2
        hi = 10 (mutated from 2)
        """
        # This test fails because function [searches.binary_search.bisect_left] produces [IndexError]
        searches.binary_search.bisect_left([3, -170141183460469231731687303715884105728], -1, 2, 10)
    
    def test_bisect_left_with_exception1(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = 33554435 (mutated from 3)
        lo = -41538374868278621028243970633760769 (mutated from 170099645085600953110659059745250344959)
        hi = -10141204801825835211973625643009 (mutated from -1)
        """
        # This test fails because function [searches.binary_search.bisect_left] produces [IndexError]
        searches.binary_search.bisect_left([170141183460469231731687303715884105727, 1, 3], 33554435, -41538374868278621028243970633760769, -10141204801825835211973625643009)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.binary_search.bisect_right
    
    # region FUZZER
    
    def test_bisect_right(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from zero)
        """
        actual = searches.binary_search.bisect_right([36028797018963970, -1, 3, 170141183460469231731687303715884105727], -1)
        
        self.assertEqual(2, actual)
    
    def test_bisect_right1(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = max (mutated from -1)
        """
        actual = searches.binary_search.bisect_right([36028797018963970, -1, 3, 170141183460469231731687303715884105727], 170141183460469231731687303715884105727)
        
        self.assertEqual(4, actual)
    
    def test_bisect_right2(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from max)
        """
        actual = searches.binary_search.bisect_right([1], -1)
        
        self.assertEqual(0, actual)
    
    def test_bisect_right3(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from zero)
        lo = zero (mutated from min)
        hi = zero
        """
        actual = searches.binary_search.bisect_right([2, -1, 3, 170141183460469231731687303715884105727], -1, 0, 0)
        
        self.assertEqual(0, actual)
    
    def test_bisect_right_with_exception(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from max)
        lo = 2
        hi = 10 (mutated from 2)
        """
        # This test fails because function [searches.binary_search.bisect_right] produces [IndexError]
        searches.binary_search.bisect_right([3, -170141183460469231731687303715884105728], -1, 2, 10)
    
    def test_bisect_right_with_exception1(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = 33554435 (mutated from 3)
        lo = -41538374868278621028243970633760769 (mutated from 170099645085600953110659059745250344959)
        hi = -10141204801825835211973625643009 (mutated from -1)
        """
        # This test fails because function [searches.binary_search.bisect_right] produces [IndexError]
        searches.binary_search.bisect_right([170141183460469231731687303715884105727, 1, 3], 33554435, -41538374868278621028243970633760769, -10141204801825835211973625643009)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.binary_search.insort_left
    
    # region FUZZER
    
    def test_insort_left(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = max
        """
        sorted_collection = [-36028797018963969, -1, -1, -170141183460469231731687303715884105728]
        
        actual = searches.binary_search.insort_left(sorted_collection, 170141183460469231731687303715884105727)
        
        self.assertEqual(None, actual)
    
    def test_insort_left_with_exception(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = min (mutated from zero)
        lo = 85070591730234615865843651857942052865 (mutated from positive)
        hi = -170141183460469231731687303715884105720 (mutated from min)
        """
        # This test fails because function [searches.binary_search.insort_left] produces [OverflowError]
        searches.binary_search.insort_left([170141183460469231731687303715884105727, 1], -170141183460469231731687303715884105728, 85070591730234615865843651857942052865, -170141183460469231731687303715884105720)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.binary_search.insort_right
    
    # region FUZZER
    
    def test_insort_right(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = max
        """
        sorted_collection = [-36028797018963969, -1, -1, -170141183460469231731687303715884105728]
        
        actual = searches.binary_search.insort_right(sorted_collection, 170141183460469231731687303715884105727)
        
        self.assertEqual(None, actual)
    
    def test_insort_right_with_exception(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = min (mutated from zero)
        lo = 85070591730234615865843651857942052865 (mutated from positive)
        hi = -170141183460469231731687303715884105720 (mutated from min)
        """
        # This test fails because function [searches.binary_search.insort_right] produces [OverflowError]
        searches.binary_search.insort_right([170141183460469231731687303715884105727, 1], -170141183460469231731687303715884105728, 85070591730234615865843651857942052865, -170141183460469231731687303715884105720)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.binary_search.binary_search
    
    # region FUZZER
    
    def test_binary_search(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from zero)
        """
        actual = searches.binary_search.binary_search([36028797018963970, -1, 3, 170141183460469231731687303715884105727], -1)
        
        self.assertEqual(1, actual)
    
    def test_binary_search1(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = max (mutated from -1)
        """
        actual = searches.binary_search.binary_search([36028797018963970, -1, 3, 170141183460469231731687303715884105727], 170141183460469231731687303715884105727)
        
        self.assertEqual(3, actual)
    
    def test_binary_search2(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from max)
        """
        actual = searches.binary_search.binary_search([1], -1)
        
        self.assertEqual(None, actual)
    
    def test_binary_search3(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = 170141178389866830818769697729071284223 (mutated from max)
        """
        actual = searches.binary_search.binary_search([36028797018963970, 170141183460469231731687303715884105727, -1, 3], 170141178389866830818769697729071284223)
        
        self.assertEqual(None, actual)
    
    def test_binary_search4(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from max)
        """
        actual = searches.binary_search.binary_search([-1, 170141183460469231731687303715884105727, -1, 170141183460469231731687303715884105727], -1)
        
        self.assertEqual(0, actual)
    
    def test_binary_search5(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = 64 (mutated from zero)
        """
        actual = searches.binary_search.binary_search([], 64)
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.binary_search.binary_search_std_lib
    
    # region FUZZER
    
    def test_binary_search_std_lib(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = max
        """
        actual = searches.binary_search.binary_search_std_lib([-36028797018963969, -1, -1, -170141183460469231731687303715884105728], 170141183460469231731687303715884105727)
        
        self.assertEqual(None, actual)
    
    def test_binary_search_std_lib1(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -1 (mutated from max)
        """
        actual = searches.binary_search.binary_search_std_lib([-36028797018963969, -1, -1, -170141183460469231731687303715884105728], -1)
        
        self.assertEqual(1, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable searches.binary_search.binary_search_by_recursion
    
    # region FUZZER
    
    def test_binary_search_by_recursion(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = positive (mutated from 2)
        left = max (mutated from -1)
        right = 2
        """
        actual = searches.binary_search.binary_search_by_recursion([0, 1, -170141183460469231731687303715884105728, 170141183460469231731687303715884105727], 1, 170141183460469231731687303715884105727, 2)
        
        self.assertEqual(None, actual)
    
    def test_binary_search_by_recursion1(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -9671406556917033397649409 (mutated from -1)
        left = zero (mutated from positive)
        right = 3 (mutated from 2)
        """
        actual = searches.binary_search.binary_search_by_recursion([2, 170141183460469231731687303715884105727], -9671406556917033397649409, 0, 3)
        
        self.assertEqual(None, actual)
    
    def test_binary_search_by_recursion2(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = 2
        left = positive (mutated from 2)
        right = 2
        """
        actual = searches.binary_search.binary_search_by_recursion([0, 1, 2, -170141183460469231731687303715884105725, 1], 2, 1, 2)
        
        self.assertEqual(2, actual)
    
    def test_binary_search_by_recursion3(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = 2
        left = positive (mutated from 2)
        right = 2
        """
        actual = searches.binary_search.binary_search_by_recursion([1, 2, 0, -170141183460469231731687303715884105725, 1], 2, 1, 2)
        
        self.assertEqual(1, actual)
    
    def test_binary_search_by_recursion_with_exception(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = max (mutated from -1)
        left = zero (mutated from positive)
        right = 65536 (mutated from zero)
        """
        # This test fails because function [searches.binary_search.binary_search_by_recursion] produces [IndexError]
        searches.binary_search.binary_search_by_recursion([-170141183460469231731687303715884105728, -1], 170141183460469231731687303715884105727, 0, 65536)
    
    def test_binary_search_by_recursion_with_exception1(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = min
        left = min
        right = max
        """
        # This test fails because function [searches.binary_search.binary_search_by_recursion] produces [IndexError]
        searches.binary_search.binary_search_by_recursion([2, -1, -170141183460469231731687303715884105728, 9, 170141183460469231731687303715884105727], -170141183460469231731687303715884105728, -170141183460469231731687303715884105728, 170141183460469231731687303715884105727)
    
    def test_binary_search_by_recursion_with_exception2(self):
        """
        sorted_collection = builtins.list[builtins.int]
        item = -170141183460469231731687303715741499391 (mutated from -170141183460469231731687303715749887999)
        left = min
        right = max
        """
        # This test fails because function [searches.binary_search.binary_search_by_recursion] produces [IndexError]
        searches.binary_search.binary_search_by_recursion([9, 2, 170141183460469229370504062281061498879, -1, -170141183460469231731687303715884105728], -170141183460469231731687303715741499391, -170141183460469231731687303715884105728, 170141183460469231731687303715884105727)
    # endregion
    
    # endregion

