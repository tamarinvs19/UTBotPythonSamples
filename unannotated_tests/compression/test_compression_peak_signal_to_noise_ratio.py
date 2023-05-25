import sys
sys.path.append(r'../../..')
import builtins
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio
    
    # region FUZZER
    
    def test_peak_signal_to_noise_ratio(self):
        """
        original = float('-inf')
        contrast = float('nan')
        """
        contrast = float('nan')
        
        actual = compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio(float('-inf'), contrast)
        
        self.assertTrue(isinstance(actual, builtins.float))
        
        self.assertEqual(float('nan'), contrast)
    
    def test_peak_signal_to_noise_ratio1(self):
        """
        original = zero
        contrast = 1.251604045410301E-308 (mutated from zero)
        """
        actual = compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio(0.0, 1.251604045410301E-308)
        
        self.assertEqual(100, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_peak_signal_to_noise_ratio_with_exception(self):
        """
        original = 100.0
        contrast = -1.1125369292536007E-308 (mutated from zero)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio(100.0, -1.1125369292536007E-308)
    
    def test_peak_signal_to_noise_ratio_with_exception1(self):
        """
        original = -170141102330830817125005607926811852800 (mutated from -170141102330830817125005607926878961664)
        contrast = float('-inf')
        """
        # This test fails because function [compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio] produces [ValueError]
        compression.peak_signal_to_noise_ratio.peak_signal_to_noise_ratio(-170141102330830817125005607926811852800, float('-inf'))
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.peak_signal_to_noise_ratio.main
    
    # region FUZZER
    
    def test_main(self):
        actual = compression.peak_signal_to_noise_ratio.main()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

