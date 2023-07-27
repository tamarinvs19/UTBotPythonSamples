import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import electronics
import unittest
import electronics.electric_conductivity


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable electronics.electric_conductivity.electric_conductivity
    
    # region FUZZER
    
    def test_electric_conductivity(self):
        """
        conductivity = positive
        electron_conc = 7.2911220195563975E-304 (mutated from zero)
        mobility = zero
        """
        actual = electronics.electric_conductivity.electric_conductivity(1.0, 7.2911220195563975E-304, 0.0)
        
        self.assertEqual(('mobility', float('inf')), actual)
    
    def test_electric_conductivity1(self):
        """
        conductivity = 1.0009765625 (mutated from positive)
        electron_conc = zero
        mobility = float('inf')
        """
        actual = electronics.electric_conductivity.electric_conductivity(1.0009765625, 0.0, float('inf'))
        
        self.assertEqual(('electron_conc', 0.0), actual)
    
    def test_electric_conductivity2(self):
        """
        conductivity = zero
        electron_conc = 1.251604045410301E-308 (mutated from zero)
        mobility = float('inf')
        """
        actual = electronics.electric_conductivity.electric_conductivity(0.0, 1.251604045410301E-308, float('inf'))
        
        self.assertEqual(('conductivity', float('inf')), actual)
    
    def test_electric_conductivity_with_exception(self):
        """
        conductivity = -1.1125369292536007E-308 (mutated from zero)
        electron_conc = float('inf')
        mobility = float('-inf')
        """
        # This test fails because function [electronics.electric_conductivity.electric_conductivity] produces [ValueError]
        electronics.electric_conductivity.electric_conductivity(-1.1125369292536007E-308, float('inf'), float('-inf'))
    
    def test_electric_conductivity_with_exception1(self):
        """
        conductivity = -1.1125369292536007E-308 (mutated from zero)
        electron_conc = 2.8480945388892178E-306 (mutated from zero)
        mobility = zero
        """
        # This test fails because function [electronics.electric_conductivity.electric_conductivity] produces [ValueError]
        electronics.electric_conductivity.electric_conductivity(-1.1125369292536007E-308, 2.8480945388892178E-306, 0.0)
    
    def test_electric_conductivity_with_exception2(self):
        """
        conductivity = zero
        electron_conc = 1.1125539052199284E-308 (mutated from zero)
        mobility = float('-inf')
        """
        # This test fails because function [electronics.electric_conductivity.electric_conductivity] produces [ValueError]
        electronics.electric_conductivity.electric_conductivity(0.0, 1.1125539052199284E-308, float('-inf'))
    
    def test_electric_conductivity_with_exception3(self):
        """
        conductivity = float('inf')
        electron_conc = 1.1125369292536017E-308 (mutated from zero)
        mobility = zero
        """
        # This test fails because function [electronics.electric_conductivity.electric_conductivity] produces [ZeroDivisionError]
        electronics.electric_conductivity.electric_conductivity(float('inf'), 1.1125369292536017E-308, 0.0)
    
    def test_electric_conductivity_with_exception4(self):
        """
        conductivity = 1.1125369292536165E-308 (mutated from zero)
        electron_conc = float('-inf')
        mobility = zero
        """
        # This test fails because function [electronics.electric_conductivity.electric_conductivity] produces [ValueError]
        electronics.electric_conductivity.electric_conductivity(1.1125369292536165E-308, float('-inf'), 0.0)
    
    def test_electric_conductivity_with_exception5(self):
        """
        conductivity = float('inf')
        electron_conc = zero
        mobility = 1.129920318773188E-308 (mutated from zero)
        """
        # This test fails because function [electronics.electric_conductivity.electric_conductivity] produces [ZeroDivisionError]
        electronics.electric_conductivity.electric_conductivity(float('inf'), 0.0, 1.129920318773188E-308)
    # endregion
    
    # endregion

