import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.alternative_string_arrange


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.alternative_string_arrange.alternative_string_arrange
    
    # region FUZZER
    
    def test_alternative_string_arrange(self):
        """
        first_str = '€'
        second_str = 'fo'
        """
        actual = strings.alternative_string_arrange.alternative_string_arrange("€", "fo")
        
        self.assertEqual('€fo\x94', actual)
    
    def test_alternative_string_arrange1(self):
        """
        first_str = ''
        second_str = '€'
        """
        actual = strings.alternative_string_arrange.alternative_string_arrange("", "€")
        
        self.assertEqual('€', actual)
    
    def test_alternative_string_arrange2(self):
        """
        first_str = ''
        second_str = ''
        """
        actual = strings.alternative_string_arrange.alternative_string_arrange("", "")
        
        self.assertEqual('', actual)
    
    def test_alternative_string_arrange3(self):
        """
        first_str = ''
        second_str = ''
        """
        actual = strings.alternative_string_arrange.alternative_string_arrange("", "")
        
        self.assertEqual('\x06', actual)
    # endregion
    
    # endregion

