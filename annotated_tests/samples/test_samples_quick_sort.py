import sys
sys.path.append(r'../../..')
import builtins
import samples
import unittest
import samples.quick_sort


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.quick_sort.quick_sort
    
    # region FUZZER
    
    def test_quick_sort(self):
        """
        array = builtins.list[builtins.int]
        """
        actual = samples.quick_sort.quick_sort([-1])
        
        self.assertEqual([-1], actual)
    
    def test_quick_sort1(self):
        """
        array = builtins.list[builtins.int]
        """
        array = [-170141183460469231731687303715884105728, 0, 0, -170141183459231291692401923440984981504]
        
        actual = samples.quick_sort.quick_sort(array)
        
        self.assertEqual([-170141183460469231731687303715884105728, -170141183459231291692401923440984981504, 0, 0], actual)
        
        self.assertEqual([-170141183460469231731687303715884105728, -170141183459231291692401923440984981504, 0, 0], array)
    
    def test_quick_sort2(self):
        """
        array = builtins.list[builtins.int]
        """
        actual = samples.quick_sort.quick_sort([-170141183460469231731687303715884105728, 0, 68719476737])
        
        self.assertEqual([-170141183460469231731687303715884105728, 0, 68719476737], actual)
    
    def test_quick_sort3(self):
        """
        array = builtins.list[builtins.int]
        """
        actual = samples.quick_sort.quick_sort([])
        
        self.assertEqual([], actual)
    # endregion
    
    # endregion

