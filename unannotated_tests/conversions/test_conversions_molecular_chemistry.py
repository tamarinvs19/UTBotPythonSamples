import sys
sys.path.append(r'../../..')
import builtins
import conversions
import unittest
import conversions.molecular_chemistry


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.molecular_chemistry.molarity_to_normality
    
    # region FUZZER
    
    def test_molarity_to_normality_with_exception(self):
        """
        nfactor = max
        moles = float('-inf')
        volume = float('-inf')
        """
        # This test fails because function [conversions.molecular_chemistry.molarity_to_normality] produces [ValueError]
        conversions.molecular_chemistry.molarity_to_normality(170141183460469231731687303715884105727, float('-inf'), float('-inf'))
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.molecular_chemistry.moles_to_pressure
    
    # region FUZZER
    
    def test_moles_to_pressure(self):
        """
        volume = float('-inf')
        moles = 0.08210000000001422 (mutated from 0.0821)
        temperature = 0.0821
        """
        actual = conversions.molecular_chemistry.moles_to_pressure(float('-inf'), 0.08210000000001422, 0.0821)
        
        self.assertEqual(0, actual)
    
    def test_moles_to_pressure_with_exception(self):
        """
        volume = float('inf')
        moles = float('-inf')
        temperature = float('nan')
        """
        temperature = float('nan')
        # This test fails because function [conversions.molecular_chemistry.moles_to_pressure] produces [ValueError]
        conversions.molecular_chemistry.moles_to_pressure(float('inf'), float('-inf'), temperature)
        
        self.assertEqual(float('nan'), temperature)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.molecular_chemistry.moles_to_volume
    
    # region FUZZER
    
    def test_moles_to_volume(self):
        """
        pressure = float('-inf')
        moles = 0.08210000000001422 (mutated from 0.0821)
        temperature = 0.0821
        """
        actual = conversions.molecular_chemistry.moles_to_volume(float('-inf'), 0.08210000000001422, 0.0821)
        
        self.assertEqual(0, actual)
    
    def test_moles_to_volume_with_exception(self):
        """
        pressure = float('inf')
        moles = float('-inf')
        temperature = float('nan')
        """
        temperature = float('nan')
        # This test fails because function [conversions.molecular_chemistry.moles_to_volume] produces [ValueError]
        conversions.molecular_chemistry.moles_to_volume(float('inf'), float('-inf'), temperature)
        
        self.assertEqual(float('nan'), temperature)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.molecular_chemistry.pressure_and_volume_to_temperature
    
    # region FUZZER
    
    def test_pressure_and_volume_to_temperature(self):
        """
        pressure = 0.08210011920928956 (mutated from 0.0821)
        moles = float('inf')
        volume = 0.0821
        """
        actual = conversions.molecular_chemistry.pressure_and_volume_to_temperature(0.08210011920928956, float('inf'), 0.0821)
        
        self.assertEqual(0, actual)
    
    def test_pressure_and_volume_to_temperature_with_exception(self):
        """
        pressure = float('inf')
        moles = float('-inf')
        volume = float('nan')
        """
        volume = float('nan')
        # This test fails because function [conversions.molecular_chemistry.pressure_and_volume_to_temperature] produces [ValueError]
        conversions.molecular_chemistry.pressure_and_volume_to_temperature(float('inf'), float('-inf'), volume)
        
        self.assertEqual(float('nan'), volume)
    # endregion
    
    # endregion

