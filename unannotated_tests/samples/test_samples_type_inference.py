import sys
sys.path.append(r'../..')
import builtins
import samples
import unittest
import samples.type_inference


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.type_inference.type_inference
    
    # region FUZZER
    
    def test_type_inference(self):
        """
        number = zero (mutated from min)
        string = 'n_'
        string_sep = 'abcdefghijklmnopqrst'
        list_of_number = builtins.list[typing.Any]
        dict_str_to_list = builtins.dict[typing.Any, typing.Any]
        """
        list_of_number = []
        dict_str_to_list = {}
        
        actual = samples.type_inference.type_inference(0, "n_", "abcdefghijklmnopqrst", list_of_number, dict_str_to_list)
        
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'n_'], actual)
        
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'n_'], list_of_number)
        
        self.assertEqual({'n_': [], }, dict_str_to_list)
    
    def test_type_inference_with_exception(self):
        """
        number = min (mutated from zero)
        string = '_'
        string_sep = 'abcdefghijklmnopqrst'
        list_of_number = builtins.list[typing.Any]
        dict_str_to_list = builtins.dict[typing.Any, typing.Any]
        """
        # This test fails because function [samples.type_inference.type_inference] produces [OverflowError]
        samples.type_inference.type_inference(-170141183460469231731687303715884105728, "_", "abcdefghijklmnopqrst", [], {})
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_type_inference_with_exception1(self):
        """
        number = 262145 (mutated from positive)
        string = ''
        string_sep = 'pyÎhörn'
        list_of_number = builtins.list[typing.Any]
        dict_str_to_list = builtins.dict[typing.Any, typing.Any]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        samples.type_inference.type_inference(262145, "", "pyÎhörn", [], {})
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_type_inference_with_exception2(self):
        """
        number = 633825300114114700748351602689 (mutated from positive)
        string = ''
        string_sep = 'pyÎhörn'
        list_of_number = builtins.list[typing.Any]
        dict_str_to_list = builtins.dict[typing.Any, typing.Any]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        samples.type_inference.type_inference(633825300114114700748351602689, "", "pyÎhörn", [], {})
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_type_inference_with_exception3(self):
        """
        number = 9223372036854775873 (mutated from 9223372036854775809)
        string = ''
        string_sep = 'pyÎhönI'
        list_of_number = builtins.list[typing.Any]
        dict_str_to_list = builtins.dict[typing.Any, typing.Any]
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        samples.type_inference.type_inference(9223372036854775873, "", "pyÎhönI", [], {})
    # endregion
    
    # endregion

