import sys
sys.path.append(r'../..')
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
    
    def test_hsv_to_rgb2(self):
        """
        hue = 180.0000000000001 (mutated from 360.0000000000002)
        saturation = 4.616685427259908E-237 (mutated from 4.616685427259907E-237)
        value = 5.254876311849987E-152 (mutated from 5.254410165554287E-152)
        """
        actual = conversions.rgb_hsv_conversion.hsv_to_rgb(180.0000000000001, 4.616685427259908E-237, 5.254876311849987E-152)
        
        self.assertEqual([0, 0, 0], actual)
    
    def test_hsv_to_rgb3(self):
        """
        hue = 180.0 (mutated from 360.0)
        saturation = 4.616685427259908E-237 (mutated from 4.616685427259907E-237)
        value = 5.254876311905556E-152 (mutated from 5.254876311849987E-152)
        """
        actual = conversions.rgb_hsv_conversion.hsv_to_rgb(180.0, 4.616685427259908E-237, 5.254876311905556E-152)
        
        self.assertEqual([0, 0, 0], actual)
    
    def test_hsv_to_rgb4(self):
        """
        hue = 255.00390625 (mutated from 255.0)
        saturation = positive
        value = positive
        """
        actual = conversions.rgb_hsv_conversion.hsv_to_rgb(255.00390625, 1.0, 1.0)
        
        self.assertEqual([64, 0, 255], actual)
    
    def test_hsv_to_rgb5(self):
        """
        hue = 63.75099182128906 (mutated from 255.00396728515625)
        saturation = 5.960464566356904E-8 (mutated from 1.5258789289873675E-5)
        value = 0.003906250363798776 (mutated from 2.1175825653514624E-22)
        """
        actual = conversions.rgb_hsv_conversion.hsv_to_rgb(63.75099182128906, 5.960464566356904E-8, 0.003906250363798776)
        
        self.assertEqual([1, 1, 1], actual)
    
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
    
    def test_hsv_to_rgb_with_exception3(self):
        """
        hue = float('nan')
        saturation = positive
        value = zero
        """
        hue = float('nan')
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [ValueError]
        conversions.rgb_hsv_conversion.hsv_to_rgb(hue, 1.0, 0.0)
        
        self.assertEqual(float('nan'), hue)
    
    def test_hsv_to_rgb_with_exception4(self):
        """
        hue = 247.0 (mutated from 255.0)
        saturation = float('nan')
        value = positive
        """
        saturation = float('nan')
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [ValueError]
        conversions.rgb_hsv_conversion.hsv_to_rgb(247.0, saturation, 1.0)
        
        self.assertEqual(float('nan'), saturation)
    
    def test_hsv_to_rgb_with_exception5(self):
        """
        hue = 231.01611328125 (mutated from 247.01611328125)
        saturation = float('nan')
        value = 0.003906250465661287 (mutated from 0.00390625)
        """
        saturation = float('nan')
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [ValueError]
        conversions.rgb_hsv_conversion.hsv_to_rgb(231.01611328125, saturation, 0.003906250465661287)
        
        self.assertEqual(float('nan'), saturation)
    
    def test_hsv_to_rgb_with_exception6(self):
        """
        hue = 1.2850698347981482E-306 (mutated from 231.01612198352814)
        saturation = float('nan')
        value = 5.690401931602565E-159 (mutated from 7.629581614310155E-5)
        """
        saturation = float('nan')
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [ValueError]
        conversions.rgb_hsv_conversion.hsv_to_rgb(1.2850698347981482E-306, saturation, 5.690401931602565E-159)
        
        self.assertEqual(float('nan'), saturation)
    
    def test_hsv_to_rgb_with_exception7(self):
        """
        hue = 167.01612198352814 (mutated from 231.01612198352814)
        saturation = float('nan')
        value = 7.887493519159221E-235 (mutated from 7.887494269007628E-235)
        """
        saturation = float('nan')
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [ValueError]
        conversions.rgb_hsv_conversion.hsv_to_rgb(167.01612198352814, saturation, 7.887493519159221E-235)
        
        self.assertEqual(float('nan'), saturation)
    
    def test_hsv_to_rgb_with_exception8(self):
        """
        hue = 350.0322439824249 (mutated from 175.01612199121246)
        saturation = float('nan')
        value = 1.2035359984068772E-239 (mutated from 1.2035359984068636E-239)
        """
        saturation = float('nan')
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [ValueError]
        conversions.rgb_hsv_conversion.hsv_to_rgb(350.0322439824249, saturation, 1.2035359984068772E-239)
        
        self.assertEqual(float('nan'), saturation)
    
    def test_hsv_to_rgb_with_exception9(self):
        """
        hue = 87.50806099560623 (mutated from 350.0322439824249)
        saturation = float('nan')
        value = 7.8874935193481E-235 (mutated from 7.887493519342379E-235)
        """
        saturation = float('nan')
        # This test fails because function [conversions.rgb_hsv_conversion.hsv_to_rgb] produces [ValueError]
        conversions.rgb_hsv_conversion.hsv_to_rgb(87.50806099560623, saturation, 7.8874935193481E-235)
        
        self.assertEqual(float('nan'), saturation)
    # endregion
    
    # endregion
    
    # region Test suites for executable conversions.rgb_hsv_conversion.rgb_to_hsv
    
    # region FUZZER
    
    def test_rgb_to_hsv(self):
        """
        red = 3 (mutated from positive)
        green = 3 (mutated from 2)
        blue = 5 (mutated from 4)
        """
        actual = conversions.rgb_hsv_conversion.rgb_to_hsv(3, 3, 5)
        
        self.assertEqual([240.0, 0.4, 0.0196078431372549], actual)
    
    def test_rgb_to_hsv1(self):
        """
        red = 59 (mutated from 60)
        green = 60
        blue = zero (mutated from 2)
        """
        actual = conversions.rgb_hsv_conversion.rgb_to_hsv(59, 60, 0)
        
        self.assertEqual([61.0, 1.0, 0.23529411764705882], actual)
    
    def test_rgb_to_hsv2(self):
        """
        red = 123 (mutated from 59)
        green = 60
        blue = zero (mutated from 2)
        """
        actual = conversions.rgb_hsv_conversion.rgb_to_hsv(123, 60, 0)
        
        self.assertEqual([29.268292682926813, 1.0, 0.4823529411764706], actual)
    
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
        hsv_1 = builtins.list[builtins.float]
        hsv_2 = builtins.list[builtins.float]
        """
        # This test fails because function [conversions.rgb_hsv_conversion.approximately_equal_hsv] produces [IndexError]
        conversions.rgb_hsv_conversion.approximately_equal_hsv([float('-inf')], [float('-inf')])
    
    def test_approximately_equal_hsv_with_exception1(self):
        """
        hsv_1 = builtins.list[builtins.float]
        hsv_2 = builtins.list[builtins.float]
        """
        # This test fails because function [conversions.rgb_hsv_conversion.approximately_equal_hsv] produces [IndexError]
        conversions.rgb_hsv_conversion.approximately_equal_hsv([], [2.0625, 2.001953125, -2.0, 2.000000000014552, 2.0])
    
    def test_approximately_equal_hsv_with_exception2(self):
        """
        hsv_1 = builtins.list[builtins.float]
        hsv_2 = builtins.list[builtins.float]
        """
        # This test fails because function [conversions.rgb_hsv_conversion.approximately_equal_hsv] produces [IndexError]
        conversions.rgb_hsv_conversion.approximately_equal_hsv([float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [0.002, -0.002])
    # endregion
    
    # endregion

