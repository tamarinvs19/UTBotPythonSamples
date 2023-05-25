import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.credit_card_validator


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.credit_card_validator.validate_initial_digits
    
    # region FUZZER
    
    def test_validate_initial_digits(self):
        """
        credit_card_number = '€'
        """
        actual = strings.credit_card_validator.validate_initial_digits("€")
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.credit_card_validator.luhn_validation
    
    # region FUZZER
    
    def test_luhn_validation(self):
        """
        credit_card_number = ''
        """
        actual = strings.credit_card_validator.luhn_validation("")
        
        self.assertEqual(True, actual)
    
    def test_luhn_validation_with_exception(self):
        """
        credit_card_number = '€'
        """
        # This test fails because function [strings.credit_card_validator.luhn_validation] produces [ValueError]
        strings.credit_card_validator.luhn_validation("€")
    
    def test_luhn_validation_with_exception1(self):
        """
        credit_card_number = 'abcdefBhijklmnopqrst'
        """
        # This test fails because function [strings.credit_card_validator.luhn_validation] produces [ValueError]
        strings.credit_card_validator.luhn_validation("abcdefBhijklmnopqrst")
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.credit_card_validator.validate_credit_card_number
    
    # region FUZZER
    
    def test_validate_credit_card_number(self):
        """
        credit_card_number = '€'
        """
        actual = strings.credit_card_validator.validate_credit_card_number("€")
        
        self.assertEqual(False, actual)
    
    def test_validate_credit_card_number_with_exception(self):
        """
        credit_card_number = 'abcdefBhijklmnopqrst'
        """
        # This test fails because function [strings.credit_card_validator.validate_credit_card_number] produces [UnicodeEncodeError]
        strings.credit_card_validator.validate_credit_card_number("abcdefBhijklmnopqrst")
    # endregion
    
    # endregion

