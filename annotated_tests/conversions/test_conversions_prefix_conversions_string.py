import sys
sys.path.append(r'../..')
import builtins
import conversions
import unittest
import conversions.prefix_conversions_string


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.prefix_conversions_string.add_si_prefix
    
    # region FUZZER
    
    def test_add_si_prefix(self):
        """
        value = -1.1125369292536007E-308 (mutated from zero)
        """
        actual = conversions.prefix_conversions_string.add_si_prefix(-1.1125369292536007E-308)
        
        self.assertEqual('-1.1125369292536007e-308', actual)
    
    def test_add_si_prefix1(self):
        """
        value = float('inf')
        """
        actual = conversions.prefix_conversions_string.add_si_prefix(float('inf'))
        
        self.assertEqual('inf yotta', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.prefix_conversions_string.add_binary_prefix
    
    # region FUZZER
    
    def test_add_binary_prefix(self):
        """
        value = float('nan')
        """
        value = float('nan')
        
        actual = conversions.prefix_conversions_string.add_binary_prefix(value)
        
        self.assertEqual('nan', actual)
        
        self.assertEqual(float('nan'), value)
    
    def test_add_binary_prefix1(self):
        """
        value = float('inf')
        """
        actual = conversions.prefix_conversions_string.add_binary_prefix(float('inf'))
        
        self.assertEqual('inf yotta', actual)
    # endregion
    
    # endregion

