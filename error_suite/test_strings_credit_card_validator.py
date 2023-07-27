import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import strings
import unittest
import strings.credit_card_validator


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.credit_card_validator.validate_initial_digits
    
    # region FUZZER
    
    def test_validate_initial_digits(self):
        """
        credit_card_number = '>4' (mutated from '4')
        """
        actual = strings.credit_card_validator.validate_initial_digits(">4")
        
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
    
    def test_luhn_validation1(self):
        """
        credit_card_number = '70' (mutated from '0')
        """
        actual = strings.credit_card_validator.luhn_validation("70")
        
        self.assertEqual(False, actual)
    
    def test_luhn_validation2(self):
        """
        credit_card_number = '07'
        """
        actual = strings.credit_card_validator.luhn_validation("07")
        
        self.assertEqual(False, actual)
    
    def test_luhn_validation_with_exception(self):
        """
        credit_card_number = 'pfoo' (mutated from 'foo')
        """
        # This test fails because function [strings.credit_card_validator.luhn_validation] produces [ValueError]
        strings.credit_card_validator.luhn_validation("pfoo")
    
    def test_luhn_validation_with_exception1(self):
        """
        credit_card_number = '' (mutated from '')
        """
        # This test fails because function [strings.credit_card_validator.luhn_validation] produces [ValueError]
        strings.credit_card_validator.luhn_validation("")
    
    def test_luhn_validation_with_exception2(self):
        """
        credit_card_number = '�20*' (mutated from '�20')
        """
        # This test fails because function [strings.credit_card_validator.luhn_validation] produces [ValueError]
        strings.credit_card_validator.luhn_validation("�20*")
    
    def test_luhn_validation_with_exception3(self):
        """
        credit_card_number = '+70' (mutated from '70')
        """
        # This test fails because function [strings.credit_card_validator.luhn_validation] produces [ValueError]
        strings.credit_card_validator.luhn_validation("+70")
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.credit_card_validator.validate_credit_card_number
    
    # region FUZZER
    
    def test_validate_credit_card_number(self):
        """
        credit_card_number = 'pfoo' (mutated from 'foo')
        """
        actual = strings.credit_card_validator.validate_credit_card_number("pfoo")
        
        self.assertEqual(False, actual)
    
    def test_validate_credit_card_number_with_exception(self):
        """
        credit_card_number = 'foo' (mutated from 'foo')
        """
        # This test fails because function [strings.credit_card_validator.validate_credit_card_number] produces [UnicodeEncodeError]
        strings.credit_card_validator.validate_credit_card_number("foo")
    # endregion
    
    # endregion

