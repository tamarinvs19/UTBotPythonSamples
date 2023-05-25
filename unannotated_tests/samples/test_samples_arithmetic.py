import sys
sys.path.append(r'../..')
import builtins
import samples
import unittest
import samples.arithmetic


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.arithmetic.f
    
    # region FUZZER
    
    def test_f(self):
        """
        x = 2197652 (mutated from 100500)
        """
        actual = samples.arithmetic.f(2197652)
        
        self.assertEqual(239, actual)
    
    def test_f1(self):
        """
        x = -170141183460469231731687303715881908076 (mutated from 2197652)
        """
        actual = samples.arithmetic.f(-170141183460469231731687303715881908076)
        
        self.assertEqual(28948022309329048855892746252171229141093267632154033797731624366534514021776, actual)
    
    def test_f2(self):
        """
        x = zero (mutated from min)
        """
        actual = samples.arithmetic.f(0)
        
        self.assertEqual(100500, actual)
    
    def test_f3(self):
        """
        x = 60 (mutated from -170141183460469231731687303715884105668)
        """
        actual = samples.arithmetic.f(60)
        
        self.assertEqual(600, actual)
    # endregion
    
    # endregion

