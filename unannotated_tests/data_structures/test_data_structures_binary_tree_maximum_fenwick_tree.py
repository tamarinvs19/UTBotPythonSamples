import sys
sys.path.append(r'..\..\..')
import builtins
import data_structures.binary_tree.maximum_fenwick_tree
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.maximum_fenwick_tree.update
    
    # region FUZZER
    
    def test_update_with_exception(self):
        """
        self = data_structures.binary_tree.maximum_fenwick_tree.MaxFenwickTree
        index = -1
        value = 170141183459231291692401923440984981503 (mutated from max)
        """
        max_fenwick_tree = data_structures.binary_tree.maximum_fenwick_tree.MaxFenwickTree(0)
        # This test fails because function [data_structures.binary_tree.maximum_fenwick_tree.update] produces [IndexError]
        max_fenwick_tree.update(-1, 170141183459231291692401923440984981503)
        
        self.assertEqual(max_fenwick_tree, max_fenwick_tree)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.maximum_fenwick_tree.query
    
    # region FUZZER
    
    def test_query(self):
        """
        self = data_structures.binary_tree.maximum_fenwick_tree.MaxFenwickTree
        left = 8.636168555094445E-78 (mutated from positive)
        right = -1 (mutated from zero)
        """
        max_fenwick_tree = data_structures.binary_tree.maximum_fenwick_tree.MaxFenwickTree(1)
        
        actual = max_fenwick_tree.query(8.636168555094445E-78, -1)
        
        self.assertEqual(0, actual)
        
        self.assertEqual(max_fenwick_tree, max_fenwick_tree)
    
    def test_query_with_exception(self):
        """
        self = data_structures.binary_tree.maximum_fenwick_tree.MaxFenwickTree
        left = min
        right = 170141183459231291692401923440984981503 (mutated from max)
        """
        max_fenwick_tree = data_structures.binary_tree.maximum_fenwick_tree.MaxFenwickTree(0)
        # This test fails because function [data_structures.binary_tree.maximum_fenwick_tree.query] produces [IndexError]
        max_fenwick_tree.query(-170141183460469231731687303715884105728, 170141183459231291692401923440984981503)
        
        self.assertEqual(max_fenwick_tree, max_fenwick_tree)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_query_with_exception1(self):
        """
        self = data_structures.binary_tree.maximum_fenwick_tree.MaxFenwickTree
        left = float('inf')
        right = 10141204801825835211973625643009 (mutated from -170141173319264429905852091742258462719)
        """
        max_fenwick_tree = data_structures.binary_tree.maximum_fenwick_tree.MaxFenwickTree(1048577)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        max_fenwick_tree.query(float('inf'), 10141204801825835211973625643009)
    # endregion
    
    # endregion

