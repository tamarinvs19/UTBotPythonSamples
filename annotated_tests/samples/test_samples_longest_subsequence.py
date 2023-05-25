import sys
sys.path.append(r'../../..')
import builtins
import samples
import unittest
import samples.longest_subsequence


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.longest_subsequence.longest_subsequence
    
    # region FUZZER
    
    def test_longest_subsequence(self):
        """
        array = builtins.list[builtins.int]
        """
        actual = samples.longest_subsequence.longest_subsequence([-170141183460469231731687303715884105728, 68719476737, 0])
        
        self.assertEqual([-170141183460469231731687303715884105728, 0], actual)
    
    def test_longest_subsequence1(self):
        """
        array = builtins.list[builtins.int]
        """
        actual = samples.longest_subsequence.longest_subsequence([-170141183460469231731687303715884105728, 0, 68719476737])
        
        self.assertEqual([-170141183460469231731687303715884105728, 0, 68719476737], actual)
    
    def test_longest_subsequence2(self):
        """
        array = builtins.list[builtins.int]
        """
        actual = samples.longest_subsequence.longest_subsequence([2, -170141183460469231731687303715884105728])
        
        self.assertEqual([-170141183460469231731687303715884105728], actual)
    # endregion
    
    # endregion

