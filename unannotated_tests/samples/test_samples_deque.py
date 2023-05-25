import sys
sys.path.append(r'../..')
import builtins
import collections
import samples
import unittest
import samples.deque


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.deque.generate_people_deque
    
    # region FUZZER
    
    def test_generate_people_deque(self):
        """
        people_count = -170141183460469231731687303715882008576 (mutated from min)
        """
        actual = samples.deque.generate_people_deque(-170141183460469231731687303715882008576)
        
        expected = collections.deque()
        
        self.assertEqual(expected, actual)
    
    def test_generate_people_deque1(self):
        """
        people_count = 2097152 (mutated from -170141183460469231731687303715882008576)
        """
        actual = samples.deque.generate_people_deque(2097152)
        
        expected = collections.deque()
        expected.append('Alex')
        expected.append('Bob')
        expected.append('Cate')
        expected.append('Daisy')
        expected.append('Ed')
        
        self.assertEqual(expected, actual)
    # endregion
    
    # endregion

