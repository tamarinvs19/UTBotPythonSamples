import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.temperature_conversions


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.temperature_conversions.celsius_to_fahrenheit
    
    # region FUZZER
    
    def test_celsius_to_fahrenheit(self):
        """
        celsius = -9.0 (mutated from 9.0)
        """
        actual = conversions.temperature_conversions.celsius_to_fahrenheit(-9.0)
        
        self.assertEqual(15.8, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.celsius_to_kelvin
    
    # region FUZZER
    
    def test_celsius_to_kelvin(self):
        """
        celsius = float('inf')
        """
        actual = conversions.temperature_conversions.celsius_to_kelvin(float('inf'))
        
        self.assertEqual(float('inf'), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.celsius_to_rankine
    
    # region FUZZER
    
    def test_celsius_to_rankine(self):
        """
        celsius = -491.67 (mutated from 491.67)
        """
        actual = conversions.temperature_conversions.celsius_to_rankine(-491.67)
        
        self.assertEqual(-393.34, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.fahrenheit_to_celsius
    
    # region FUZZER
    
    def test_fahrenheit_to_celsius(self):
        """
        fahrenheit = -32.0 (mutated from 32.0)
        """
        actual = conversions.temperature_conversions.fahrenheit_to_celsius(-32.0)
        
        self.assertEqual(-35.56, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.fahrenheit_to_kelvin
    
    # region FUZZER
    
    def test_fahrenheit_to_kelvin(self):
        """
        fahrenheit = -5.0 (mutated from 5.0)
        """
        actual = conversions.temperature_conversions.fahrenheit_to_kelvin(-5.0)
        
        self.assertEqual(252.59, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.fahrenheit_to_rankine
    
    # region FUZZER
    
    def test_fahrenheit_to_rankine(self):
        """
        fahrenheit = float('inf')
        """
        actual = conversions.temperature_conversions.fahrenheit_to_rankine(float('inf'))
        
        self.assertEqual(float('inf'), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.kelvin_to_celsius
    
    # region FUZZER
    
    def test_kelvin_to_celsius(self):
        """
        kelvin = float('inf')
        """
        actual = conversions.temperature_conversions.kelvin_to_celsius(float('inf'))
        
        self.assertEqual(float('inf'), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.kelvin_to_fahrenheit
    
    # region FUZZER
    
    def test_kelvin_to_fahrenheit(self):
        """
        kelvin = -5.0 (mutated from 5.0)
        """
        actual = conversions.temperature_conversions.kelvin_to_fahrenheit(-5.0)
        
        self.assertEqual(-468.67, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.kelvin_to_rankine
    
    # region FUZZER
    
    def test_kelvin_to_rankine(self):
        """
        kelvin = float('nan')
        """
        kelvin = float('nan')
        
        actual = conversions.temperature_conversions.kelvin_to_rankine(kelvin)
        
        self.assertTrue(isinstance(actual, builtins.float))
        
        self.assertEqual(float('nan'), kelvin)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.rankine_to_celsius
    
    # region FUZZER
    
    def test_rankine_to_celsius(self):
        """
        rankine = -491.67 (mutated from 491.67)
        """
        actual = conversions.temperature_conversions.rankine_to_celsius(-491.67)
        
        self.assertEqual(-546.3, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.rankine_to_fahrenheit
    
    # region FUZZER
    
    def test_rankine_to_fahrenheit(self):
        """
        rankine = float('inf')
        """
        actual = conversions.temperature_conversions.rankine_to_fahrenheit(float('inf'))
        
        self.assertEqual(float('inf'), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.rankine_to_kelvin
    
    # region FUZZER
    
    def test_rankine_to_kelvin(self):
        """
        rankine = float('nan')
        """
        rankine = float('nan')
        
        actual = conversions.temperature_conversions.rankine_to_kelvin(rankine)
        
        self.assertTrue(isinstance(actual, builtins.float))
        
        self.assertEqual(float('nan'), rankine)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.reaumur_to_kelvin
    
    # region FUZZER
    
    def test_reaumur_to_kelvin(self):
        """
        reaumur = float('nan')
        """
        reaumur = float('nan')
        
        actual = conversions.temperature_conversions.reaumur_to_kelvin(reaumur)
        
        self.assertTrue(isinstance(actual, builtins.float))
        
        self.assertEqual(float('nan'), reaumur)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.reaumur_to_fahrenheit
    
    # region FUZZER
    
    def test_reaumur_to_fahrenheit(self):
        """
        reaumur = float('nan')
        """
        reaumur = float('nan')
        
        actual = conversions.temperature_conversions.reaumur_to_fahrenheit(reaumur)
        
        self.assertTrue(isinstance(actual, builtins.float))
        
        self.assertEqual(float('nan'), reaumur)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.reaumur_to_celsius
    
    # region FUZZER
    
    def test_reaumur_to_celsius(self):
        """
        reaumur = float('inf')
        """
        actual = conversions.temperature_conversions.reaumur_to_celsius(float('inf'))
        
        self.assertEqual(float('inf'), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.temperature_conversions.reaumur_to_rankine
    
    # region FUZZER
    
    def test_reaumur_to_rankine(self):
        """
        reaumur = -2.25 (mutated from 2.25)
        """
        actual = conversions.temperature_conversions.reaumur_to_rankine(-2.25)
        
        self.assertEqual(486.61, actual)
    # endregion
    
    # endregion

