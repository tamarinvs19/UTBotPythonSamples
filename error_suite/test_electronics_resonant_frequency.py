import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import electronics
import unittest
import electronics.resonant_frequency


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable electronics.resonant_frequency.resonant_frequency
    
    # region FUZZER
    
    def test_resonant_frequency(self):
        """
        inductance = positive
        capacitance = 2.0 (mutated from zero)
        """
        actual = electronics.resonant_frequency.resonant_frequency(1.0, 2.0)
        
        self.assertEqual(('Resonant frequency', 0.11253953951963826), actual)
    
    def test_resonant_frequency_with_exception(self):
        """
        inductance = -1.9113238906945923E-298 (mutated from 1.9113238906945923E-298)
        capacitance = float('nan')
        """
        capacitance = float('nan')
        # This test fails because function [electronics.resonant_frequency.resonant_frequency] produces [ValueError]
        electronics.resonant_frequency.resonant_frequency(-1.9113238906945923E-298, capacitance)
    
    def test_resonant_frequency_with_exception1(self):
        """
        inductance = 2.000000238418579 (mutated from 2.0)
        capacitance = float('-inf')
        """
        # This test fails because function [electronics.resonant_frequency.resonant_frequency] produces [ValueError]
        electronics.resonant_frequency.resonant_frequency(2.000000238418579, float('-inf'))
    
    def test_resonant_frequency_with_exception2(self):
        """
        inductance = 1.7800590868057611E-307 (mutated from zero)
        capacitance = 1.1474395160233975E-308 (mutated from 1.1473037082927757E-308)
        """
        # This test fails because function [electronics.resonant_frequency.resonant_frequency] produces [ZeroDivisionError]
        electronics.resonant_frequency.resonant_frequency(1.7800590868057611E-307, 1.1474395160233975E-308)
    # endregion
    
    # endregion

