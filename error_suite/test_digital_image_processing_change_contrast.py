import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import digital_image_processing
import unittest
import digital_image_processing.change_contrast


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable digital_image_processing.change_contrast.change_contrast
    
    # region FUZZER
    
    def test_change_contrast_with_exception(self):
        """
        img = -158456325028528675187087900673 (mutated from -1)
        level = 259
        """
        # This test fails because function [digital_image_processing.change_contrast.change_contrast] produces [ZeroDivisionError]
        digital_image_processing.change_contrast.change_contrast(-158456325028528675187087900673, 259)
    # endregion
    
    # endregion

