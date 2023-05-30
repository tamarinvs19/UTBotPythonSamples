import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.barcode_validator


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.barcode_validator.get_check_digit
    
    # region FUZZER
    
    def test_get_check_digit(self):
        """
        barcode = 170141183460469231731687303715882008575 (mutated from max)
        """
        actual = strings.barcode_validator.get_check_digit(170141183460469231731687303715882008575)
        
        self.assertEqual(8, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_check_digit_with_exception(self):
        """
        barcode = -2097153 (mutated from 170141183460469231731687303715882008575)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.barcode_validator.get_check_digit(-2097153)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.barcode_validator.is_valid
    
    # region FUZZER
    
    def test_is_valid(self):
        """
        barcode = 170141183460469231731687303715882008575 (mutated from max)
        """
        actual = strings.barcode_validator.is_valid(170141183460469231731687303715882008575)
        
        self.assertEqual(False, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_is_valid_with_exception(self):
        """
        barcode = -549755813889 (mutated from -1)
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        strings.barcode_validator.is_valid(-549755813889)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.barcode_validator.get_barcode
    
    # region FUZZER
    
    def test_get_barcode(self):
        """
        barcode = '3'
        """
        actual = strings.barcode_validator.get_barcode("3")
        
        self.assertEqual(3, actual)
    
    def test_get_barcode_with_exception(self):
        """
        barcode = 'The entered bacode has a negative value. Try again.'
        """
        # This test fails because function [strings.barcode_validator.get_barcode] produces [ValueError]
        strings.barcode_validator.get_barcode("The entered bacode has a negative value. Try again.")
    
    def test_get_barcode_with_exception1(self):
        """
        barcode = 'pythön'
        """
        # This test fails because function [strings.barcode_validator.get_barcode] produces [ValueError]
        strings.barcode_validator.get_barcode("pythön")
    # endregion
    
    # endregion

