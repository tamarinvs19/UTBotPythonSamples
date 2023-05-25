import sys
sys.path.append(r'../../..')
import builtins
import conversions
import unittest
import conversions.rgb_hsv_conversion


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable conversions.rgb_hsv_conversion.hsv_to_rgb
    
    # region FUZZER
    
    def test_hsv_to_rgb(self):
        """
        hue = 360.0
        saturation = 3.337610787760802E-307 (mutated from 60.0)
        value = zero
        """
        actual = conversions.rgb_hsv_conversion.hsv_to_rgb(360.0, 3.337610787760802E-307, 0.0)
        
        self.assertEqual([0, 0, 0], actual)
    
    def test_hsv_to_rgb1(self):
        """
        hue = 2.0
        saturation = 1.112536929257648E-308 (mutated from zero)
        value = 1.4184845847983409E-306 (mutated from 255.0)
        """
        actual = conversions.rgb_hsv_conversion.hsv_to_rgb(2.0, 1.112536929257648E-308, 1.4184845847983409E-306)
        
        self.assertEqual([0, 0, 0], actual)
    
    def test_hsv_to_rgb_with_exception(self):
        """
        hue = 360.00000000000006 (mutated from 360.0)
        saturation = 3.337610787760802E-307 (mutated from 60.0)
        value = zero
        """
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [Exception]
        conversions.rgb_hsv_conversion.hsv_to_rgb(360.00000000000006, 3.337610787760802E-307, 0.0)
    
    def test_hsv_to_rgb_with_exception1(self):
        """
        hue = 5.0
        saturation = 255.0
        value = 4.450147717014403E-308 (mutated from zero)
        """
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [Exception]
        conversions.rgb_hsv_conversion.hsv_to_rgb(5.0, 255.0, 4.450147717014403E-308)
    
    def test_hsv_to_rgb_with_exception2(self):
        """
        hue = 360.0
        saturation = 3.337610787760802E-307 (mutated from 60.0)
        value = 2.0 (mutated from zero)
        """
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [Exception]
        conversions.rgb_hsv_conversion.hsv_to_rgb(360.0, 3.337610787760802E-307, 2.0)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.rgb_hsv_conversion.rgb_to_hsv
    
    # region FUZZER
    
    def test_rgb_to_hsv(self):
        """
        red = 1.11253692926979E-308 (mutated from zero)
        green = 2
        blue = 59 (mutated from 60)
        """
        actual = conversions.rgb_hsv_conversion.rgb_to_hsv(1.11253692926979E-308, 2, 59)
        
        self.assertEqual([237.96610169491532, 1.0, 0.23137254901960785], actual)
    
    def test_rgb_to_hsv_with_exception(self):
        """
        red = 5 (mutated from 4)
        green = min (mutated from zero)
        blue = 255
        """
        # This test fails because function [conversions.rgb_hsv_conversion.rgb_to_hsv] produces [Exception]
        conversions.rgb_hsv_conversion.rgb_to_hsv(5, -170141183460469231731687303715884105728, 255)
    
    def test_rgb_to_hsv_with_exception1(self):
        """
        red = 36028797018963973 (mutated from 5)
        green = min (mutated from zero)
        blue = 255
        """
        # This test fails because function [conversions.rgb_hsv_conversion.rgb_to_hsv] produces [Exception]
        conversions.rgb_hsv_conversion.rgb_to_hsv(36028797018963973, -170141183460469231731687303715884105728, 255)
    
    def test_rgb_to_hsv_with_exception2(self):
        """
        red = 4
        green = 61 (mutated from 60)
        blue = -170141183460469231731687303715884105472 (mutated from 256)
        """
        # This test fails because function [conversions.rgb_hsv_conversion.rgb_to_hsv] produces [Exception]
        conversions.rgb_hsv_conversion.rgb_to_hsv(4, 61, -170141183460469231731687303715884105472)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.rgb_hsv_conversion.approximately_equal_hsv
    
    # region FUZZER
    
    def test_approximately_equal_hsv(self):
        """
        hsv_1 = builtins.list[builtins.float]
        hsv_2 = builtins.list[builtins.float]
        """
        actual = conversions.rgb_hsv_conversion.approximately_equal_hsv([1.0, 1.0000000018626451, 1.0000000009313226, -1.0, 1.0001220703125], [2.8480945388892178E-306, 2.0, float('inf'), float('nan'), 1.0])
        
        self.assertEqual(False, actual)
    
    def test_approximately_equal_hsv_with_exception(self):
        """
        hsv_1 = builtins.list[typing.Any]
        hsv_2 = builtins.list[typing.Any]
        """
        # This test fails because function [conversions.rgb_hsv_conversion.approximately_equal_hsv] produces [IndexError]
        conversions.rgb_hsv_conversion.approximately_equal_hsv([], [])
    
    def test_approximately_equal_hsv_with_exception1(self):
        """
        hsv_1 = builtins.list[builtins.float]
        hsv_2 = builtins.list[builtins.float]
        """
        # This test fails because function [conversions.rgb_hsv_conversion.approximately_equal_hsv] produces [IndexError]
        conversions.rgb_hsv_conversion.approximately_equal_hsv([float('-inf')], [float('-inf')])
    
    def test_approximately_equal_hsv_with_exception2(self):
        """
        hsv_1 = builtins.list[builtins.float]
        hsv_2 = builtins.list[builtins.float]
        """
        # This test fails because function [conversions.rgb_hsv_conversion.approximately_equal_hsv] produces [IndexError]
        conversions.rgb_hsv_conversion.approximately_equal_hsv([float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [0.002, -0.002])
    # endregion
    
    # endregion

