import sys
sys.path.append(r'../../..')
import builtins
import samples
import unittest
import samples.arithmetic


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.arithmetic.calculate_function_value
    
    # region FUZZER
    
    def test_calculate_function_value(self):
        """
        x = 99 (mutated from 100)
        y = -69 (mutated from -101)
        """
        actual = samples.arithmetic.calculate_function_value(99, -69)
        
        self.assertEqual(-47863.96405999798, actual)
    
    def test_calculate_function_value1(self):
        """
        x = 302231454903657293676643 (mutated from 99)
        y = -69 (mutated from -101)
        """
        actual = samples.arithmetic.calculate_function_value(302231454903657293676643, -69)
        
        self.assertEqual(549755813888.0, actual)
    
    def test_calculate_function_value2(self):
        """
        x = -1124 (mutated from -100)
        y = 2
        """
        actual = samples.arithmetic.calculate_function_value(-1124, 2)
        
        self.assertEqual(-11.24, actual)
    
    def test_calculate_function_value_with_exception(self):
        """
        x = -170141183460468929500232400058590429085 (mutated from 302231454903657293676643)
        y = -69 (mutated from -101)
        """
        # This test fails because function [samples.arithmetic.calculate_function_value] produces [ValueError]
        samples.arithmetic.calculate_function_value(-170141183460468929500232400058590429085, -69)
    
    def test_calculate_function_value_with_exception1(self):
        """
        x = zero (mutated from min)
        y = 3 (mutated from 2)
        """
        # This test fails because function [samples.arithmetic.calculate_function_value] produces [ZeroDivisionError]
        samples.arithmetic.calculate_function_value(0, 3)
    
    def test_calculate_function_value_with_exception2(self):
        """
        x = 536871011 (mutated from 99)
        y = max (mutated from -1)
        """
        # This test fails because function [samples.arithmetic.calculate_function_value] produces [ValueError]
        samples.arithmetic.calculate_function_value(536871011, 170141183460469231731687303715884105727)
    # endregion
    
    # endregion
    
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

