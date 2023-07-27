import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import electronics
import unittest
import electronics.coulombs_law


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable electronics.coulombs_law.couloumbs_law
    
    # region FUZZER
    
    def test_couloumbs_law(self):
        """
        force = float('inf')
        charge1 = 0.001953125 (mutated from 0.5)
        charge2 = zero
        distance = 1.7800590868057611E-307 (mutated from zero)
        """
        actual = electronics.coulombs_law.couloumbs_law(float('inf'), 0.001953125, 0.0, 1.7800590868057611E-307)
        
        expected_dict = {'charge2': float('nan'), }
        expected_length = len(expected_dict)
        actual_length = len(actual)
        
        self.assertEqual(expected_length, actual_length)
        
        key = None
        for key in {'charge2': float('nan'), }:
            expected_element = expected_dict[key]
            actual_element = actual[key]
            
            self.assertTrue(isinstance(actual_element, float))
    
    def test_couloumbs_law1(self):
        """
        force = 1.112570881186256E-308 (mutated from zero)
        charge1 = 1.1125411732451826E-308 (mutated from zero)
        charge2 = 0.5
        distance = zero
        """
        actual = electronics.coulombs_law.couloumbs_law(1.112570881186256E-308, 1.1125411732451826E-308, 0.5, 0.0)
        
        self.assertEqual({'distance': 67036.40802515823, }, actual)
    
    def test_couloumbs_law2(self):
        """
        force = 0.5
        charge1 = zero
        charge2 = 6.805647338418769E38 (mutated from 2.0)
        distance = 0.5
        """
        actual = electronics.coulombs_law.couloumbs_law(0.5, 0.0, 6.805647338418769E38, 0.5)
        
        self.assertEqual({'charge1': 2.0435134881617982e-50, }, actual)
    
    def test_couloumbs_law3(self):
        """
        force = zero
        charge1 = 2.0
        charge2 = 2.0
        distance = 131072.0 (mutated from 2.0)
        """
        actual = electronics.coulombs_law.couloumbs_law(0.0, 2.0, 2.0, 131072.0)
        
        self.assertEqual({'force': 2.0926818251609802, }, actual)
    
    def test_couloumbs_law_with_exception(self):
        """
        force = 1.0000001192092896 (mutated from positive)
        charge1 = zero
        charge2 = 2.0
        distance = zero
        """
        # This test fails because function [electronics.coulombs_law.couloumbs_law] produces [ValueError]
        electronics.coulombs_law.couloumbs_law(1.0000001192092896, 0.0, 2.0, 0.0)
    
    def test_couloumbs_law_with_exception1(self):
        """
        force = float('inf')
        charge1 = -0.0019531250145519152 (mutated from 0.0019531250145519152)
        charge2 = zero
        distance = -3.560118173715135E-307 (mutated from 3.560118173715135E-307)
        """
        # This test fails because function [electronics.coulombs_law.couloumbs_law] produces [ValueError]
        electronics.coulombs_law.couloumbs_law(float('inf'), -0.0019531250145519152, 0.0, -3.560118173715135E-307)
    
    def test_couloumbs_law_with_exception2(self):
        """
        force = zero
        charge1 = 2.00390625 (mutated from 2.0)
        charge2 = 2.000000000000007 (mutated from 2.0)
        distance = 1.757388200993486E159 (mutated from 131072.00000000373)
        """
        # This test fails because function [electronics.coulombs_law.couloumbs_law] produces [OverflowError]
        electronics.coulombs_law.couloumbs_law(0.0, 2.00390625, 2.000000000000007, 1.757388200993486E159)
    
    def test_couloumbs_law_with_exception3(self):
        """
        force = float('-inf')
        charge1 = zero
        charge2 = float('nan')
        distance = 1.8427555295919435E165 (mutated from 1.3743898624E11)
        """
        charge2 = float('nan')
        # This test fails because function [electronics.coulombs_law.couloumbs_law] produces [OverflowError]
        electronics.coulombs_law.couloumbs_law(float('-inf'), 0.0, charge2, 1.8427555295919435E165)
    
    def test_couloumbs_law_with_exception4(self):
        """
        force = 2.0
        charge1 = 0.5
        charge2 = zero
        distance = 2.6815615859885194E154 (mutated from 2.0)
        """
        # This test fails because function [electronics.coulombs_law.couloumbs_law] produces [OverflowError]
        electronics.coulombs_law.couloumbs_law(2.0, 0.5, 0.0, 2.6815615859885194E154)
    # endregion
    
    # endregion

