import sys
sys.path.append(r'..\..\..')
import builtins
import data_structures.binary_tree.lazy_segment_tree
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.binary_tree.lazy_segment_tree.left
    
    # region FUZZER
    
    def test_left(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = zero (mutated from min)
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(0)
        
        actual = segment_tree.left(0)
        
        self.assertEqual(0, actual)
        
        self.assertEqual(segment_tree, segment_tree)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_left_with_exception(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = -164824271477329568240072075474762727424 (mutated from min)
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(170141183460469231731687303715884105727)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        segment_tree.left(-164824271477329568240072075474762727424)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_left_with_exception1(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = zero (mutated from min)
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(39614081257132168796771975168)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        segment_tree.left(0)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.lazy_segment_tree.right
    
    # region FUZZER
    
    def test_right(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = zero (mutated from min)
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(0)
        
        actual = segment_tree.right(0)
        
        self.assertEqual(1, actual)
        
        self.assertEqual(segment_tree, segment_tree)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_right_with_exception(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = -164824271477329568240072075474762727424 (mutated from min)
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(170141183460469231731687303715884105727)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        segment_tree.right(-164824271477329568240072075474762727424)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_right_with_exception1(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = zero (mutated from min)
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(39614081257132168796771975168)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        segment_tree.right(0)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.lazy_segment_tree.build
    
    # region FUZZER
    
    def test_build_with_exception(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = min
        left_element = -1 (mutated from max)
        right_element = -1
        a = builtins.list[typing.Any]
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(2)
        # This test fails because function [data_structures.binary_tree.lazy_segment_tree.build] produces [IndexError]
        segment_tree.build(-170141183460469231731687303715884105728, -1, -1, [])
        
        self.assertEqual(segment_tree, segment_tree)
    
    def test_build_with_exception1(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = min
        left_element = -1 (mutated from max)
        right_element = -1208925819614629174706177 (mutated from -1)
        a = builtins.list[typing.Any]
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(2)
        # This test fails because function [data_structures.binary_tree.lazy_segment_tree.build] produces [RecursionError]
        segment_tree.build(-170141183460469231731687303715884105728, -1, -1208925819614629174706177, [])
        
        self.assertEqual(segment_tree, segment_tree)
    
    def test_build_with_exception2(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = -169975029960996117247574327833348800512 (mutated from -169975029960996117247574327833349062656)
        left_element = -16777217 (mutated from -1)
        right_element = -1
        a = builtins.list[typing.Any]
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(2)
        # This test fails because function [data_structures.binary_tree.lazy_segment_tree.build] produces [IndexError]
        segment_tree.build(-169975029960996117247574327833348800512, -16777217, -1, [])
        
        self.assertEqual(segment_tree, segment_tree)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_build_with_exception3(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = min
        left_element = zero (mutated from positive)
        right_element = positive
        a = builtins.list[typing.Any]
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(170141183460469231731687303715884105727)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        segment_tree.build(-170141183460469231731687303715884105728, 0, 1, [])
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.lazy_segment_tree.update
    
    # region FUZZER
    
    def test_update_with_exception(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = min
        left_element = max
        right_element = max (mutated from -1)
        a = zero (mutated from positive)
        b = zero (mutated from positive)
        val = 3 (mutated from 2)
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(3)
        # This test fails because function [data_structures.binary_tree.lazy_segment_tree.update] produces [IndexError]
        segment_tree.update(-170141183460469231731687303715884105728, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 0, 0, 3)
        
        self.assertEqual(segment_tree, segment_tree)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.lazy_segment_tree.query
    
    # region FUZZER
    
    def test_query_with_exception(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = -1 (mutated from max)
        left_element = -1
        right_element = min
        a = zero (mutated from positive)
        b = -1
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(0)
        # This test fails because function [data_structures.binary_tree.lazy_segment_tree.query] produces [IndexError]
        segment_tree.query(-1, -1, -170141183460469231731687303715884105728, 0, -1)
        
        self.assertEqual(segment_tree, segment_tree)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_query_with_exception1(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        idx = positive (mutated from 2)
        left_element = 20769187434139310514121985316880385 (mutated from positive)
        right_element = 3 (mutated from 2)
        a = positive (mutated from 2)
        b = -1
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(170141183460469231731687303715884105727)
        segment_tree.size = 1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        segment_tree.query(1, 20769187434139310514121985316880385, 3, 1, -1)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.binary_tree.lazy_segment_tree.__str__
    
    # region FUZZER
    
    def test___str__(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(-170141183460469231731687303715884105728)
        
        actual = segment_tree.__str__()
        
        self.assertEqual('[]', actual)
        
        self.assertEqual(segment_tree, segment_tree)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___str___with_exception(self):
        """
        self = data_structures.binary_tree.lazy_segment_tree.SegmentTree
        """
        segment_tree = data_structures.binary_tree.lazy_segment_tree.SegmentTree(170141183460469231731687303715884105663)
        segment_tree.size = 1
        segment_tree.segment_tree = [-170141183460469231731687303715884105728, -170141102330830817125005607926878961664, -170141183460469231731687286123698061312, -170141183460469231731687303681524367360]
        segment_tree.flag = [0, -1, 2, 170141183460469231731687303715884105727]
        segment_tree.lazy = [0]
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        segment_tree.__str__()
    # endregion
    
    # endregion

