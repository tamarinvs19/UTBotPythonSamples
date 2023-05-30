import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.is_srilankan_phone_number


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.is_srilankan_phone_number.is_sri_lankan_phone_number
    
    # region FUZZER
    
    def test_is_sri_lankan_phone_number(self):
        """
        phone = 'r"￯(-| )"'
        """
        actual = strings.is_srilankan_phone_number.is_sri_lankan_phone_number("r\"￯(-| )\"")
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion

