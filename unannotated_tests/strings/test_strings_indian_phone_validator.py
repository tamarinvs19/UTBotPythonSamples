import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.indian_phone_validator


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.indian_phone_validator.indian_phone_validator
    
    # region FUZZER
    
    def test_indian_phone_validator(self):
        """
        phone = '"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"'
        """
        actual = strings.indian_phone_validator.indian_phone_validator("\"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$\"")
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion

