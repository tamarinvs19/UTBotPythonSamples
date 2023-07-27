import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import electronics
import unittest
import electronics.electrical_impedance


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable electronics.electrical_impedance.electrical_impedance
    
    # region FUZZER
    
    def test_electrical_impedance(self):
        """
        resistance = zero
        reactance = -1.1125369292536007E-308 (mutated from zero)
        impedance = 2.0
        """
        actual = electronics.electrical_impedance.electrical_impedance(0.0, -1.1125369292536007E-308, 2.0)
        
        self.assertEqual({'resistance': 2.0, }, actual)
    
    def test_electrical_impedance1(self):
        """
        resistance = 2.0625 (mutated from 2.0)
        reactance = 2.0
        impedance = zero
        """
        actual = electronics.electrical_impedance.electrical_impedance(2.0625, 2.0, 0.0)
        
        self.assertEqual({'impedance': 2.872961233640301, }, actual)
    
    def test_electrical_impedance2(self):
        """
        resistance = 1.1125369292536017E-308 (mutated from zero)
        reactance = zero
        impedance = 2.0
        """
        actual = electronics.electrical_impedance.electrical_impedance(1.1125369292536017E-308, 0.0, 2.0)
        
        self.assertEqual({'reactance': 2.0, }, actual)
    
    def test_electrical_impedance_with_exception(self):
        """
        resistance = 1.1125369292536007E-308 (mutated from zero)
        reactance = -1.1125369292536007E-308 (mutated from zero)
        impedance = 2.0
        """
        # This test fails because function [electronics.electrical_impedance.electrical_impedance] produces [ValueError]
        electronics.electrical_impedance.electrical_impedance(1.1125369292536007E-308, -1.1125369292536007E-308, 2.0)
    
    def test_electrical_impedance_with_exception1(self):
        """
        resistance = float('-inf')
        reactance = zero
        impedance = 131072.0 (mutated from 2.0)
        """
        # This test fails because function [electronics.electrical_impedance.electrical_impedance] produces [ValueError]
        electronics.electrical_impedance.electrical_impedance(float('-inf'), 0.0, 131072.0)
    
    def test_electrical_impedance_with_exception2(self):
        """
        resistance = zero
        reactance = float('inf')
        impedance = 2.000030517578125 (mutated from 2.0)
        """
        # This test fails because function [electronics.electrical_impedance.electrical_impedance] produces [ValueError]
        electronics.electrical_impedance.electrical_impedance(0.0, float('inf'), 2.000030517578125)
    
    def test_electrical_impedance_with_exception3(self):
        """
        resistance = 2.5000001192094032 (mutated from -2.5000001192094032)
        reactance = -2.6815615859885194E154 (mutated from -2.0)
        impedance = zero
        """
        # This test fails because function [electronics.electrical_impedance.electrical_impedance] produces [OverflowError]
        electronics.electrical_impedance.electrical_impedance(2.5000001192094032, -2.6815615859885194E154, 0.0)
    # endregion
    
    # endregion

