import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import electronics
import unittest
import electronics.carrier_concentration


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable electronics.carrier_concentration.carrier_concentration
    
    # region FUZZER
    
    def test_carrier_concentration(self):
        """
        electron_conc = positive
        hole_conc = 512.0 (mutated from 2.0)
        intrinsic_conc = zero
        """
        actual = electronics.carrier_concentration.carrier_concentration(1.0, 512.0, 0.0)
        
        self.assertEqual(('intrinsic_conc', 22.627416997969522), actual)
    
    def test_carrier_concentration1(self):
        """
        electron_conc = zero
        hole_conc = float('inf')
        intrinsic_conc = 1.52587890625E-5 (mutated from positive)
        """
        actual = electronics.carrier_concentration.carrier_concentration(0.0, float('inf'), 1.52587890625E-5)
        
        self.assertEqual(('electron_conc', 0.0), actual)
    
    def test_carrier_concentration2(self):
        """
        electron_conc = 1.03125 (mutated from positive)
        hole_conc = zero
        intrinsic_conc = float('inf')
        """
        actual = electronics.carrier_concentration.carrier_concentration(1.03125, 0.0, float('inf'))
        
        self.assertEqual(('hole_conc', float('inf')), actual)
    
    def test_carrier_concentration_with_exception(self):
        """
        electron_conc = negative
        hole_conc = -0.5 (mutated from 0.5)
        intrinsic_conc = zero
        """
        # This test fails because function [electronics.carrier_concentration.carrier_concentration] produces [ValueError]
        electronics.carrier_concentration.carrier_concentration(-1.0, -0.5, 0.0)
    
    def test_carrier_concentration_with_exception1(self):
        """
        electron_conc = 1.0000000000000002 (mutated from -1.0000000000000002)
        hole_conc = -0.5 (mutated from 0.5)
        intrinsic_conc = zero
        """
        # This test fails because function [electronics.carrier_concentration.carrier_concentration] produces [ValueError]
        electronics.carrier_concentration.carrier_concentration(1.0000000000000002, -0.5, 0.0)
    
    def test_carrier_concentration_with_exception2(self):
        """
        electron_conc = positive
        hole_conc = 512.0 (mutated from 2.0)
        intrinsic_conc = -1.1125369292536007E-308 (mutated from zero)
        """
        # This test fails because function [electronics.carrier_concentration.carrier_concentration] produces [ValueError]
        electronics.carrier_concentration.carrier_concentration(1.0, 512.0, -1.1125369292536007E-308)
    
    def test_carrier_concentration_with_exception3(self):
        """
        electron_conc = zero
        hole_conc = 0.5
        intrinsic_conc = -1.1125369292536007E-308 (mutated from zero)
        """
        # This test fails because function [electronics.carrier_concentration.carrier_concentration] produces [ValueError]
        electronics.carrier_concentration.carrier_concentration(0.0, 0.5, -1.1125369292536007E-308)
    
    def test_carrier_concentration_with_exception4(self):
        """
        electron_conc = zero
        hole_conc = positive
        intrinsic_conc = 2.6815615859885194E154 (mutated from 2.0)
        """
        # This test fails because function [electronics.carrier_concentration.carrier_concentration] produces [OverflowError]
        electronics.carrier_concentration.carrier_concentration(0.0, 1.0, 2.6815615859885194E154)
    
    def test_carrier_concentration_with_exception5(self):
        """
        electron_conc = 0.5
        hole_conc = zero
        intrinsic_conc = 2.6815615859885194E154 (mutated from 2.0)
        """
        # This test fails because function [electronics.carrier_concentration.carrier_concentration] produces [OverflowError]
        electronics.carrier_concentration.carrier_concentration(0.5, 0.0, 2.6815615859885194E154)
    # endregion
    
    # endregion

