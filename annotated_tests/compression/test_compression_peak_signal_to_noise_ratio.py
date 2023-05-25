import sys
sys.path.append(r'../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio
    
    # region FUZZER
    
    def test_peak_signal_to_noise_ratio(self):
        """
        original = 100.0
        contrast = -1.1125369292536007E-308 (mutated from zero)
        """
        actual = compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio(100.0, -1.1125369292536007E-308)
        
        self.assertEqual(8.130803608679102, actual)
    
    def test_peak_signal_to_noise_ratio1(self):
        """
        original = 1.390671161567001E-308 (mutated from zero)
        contrast = zero
        """
        actual = compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio(1.390671161567001E-308, 0.0)
        
        self.assertEqual(100, actual)
    
    def test_peak_signal_to_noise_ratio_with_exception(self):
        """
        original = zero
        contrast = float('inf')
        """
        # This test fails because function [compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio] produces [ValueError]
        compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio(0.0, float('inf'))
    
    def test_peak_signal_to_noise_ratio_with_exception1(self):
        """
        original = 20.0
        contrast = 2.6815615859885194E155 (mutated from 20.0)
        """
        # This test fails because function [compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio] produces [OverflowError]
        compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio(20.0, 2.6815615859885194E155)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.peak_signal_to_noise_ratio.main
    
    # region FUZZER
    
    def test_main(self):
        actual = compression.peak_signal_to_noise_ratio.main()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

