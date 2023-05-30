import sys
sys.path.append(r'../../..')
import builtins
import strings
import unittest
import strings.z_function


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.z_function.z_function
    
    # region FUZZER
    
    def test_z_function(self):
        """
        input_str = '€'
        """
        actual = strings.z_function.z_function("€")
        
        self.assertEqual([0], actual)
    
    def test_z_function1(self):
        """
        input_str = '€ₐ'
        """
        actual = strings.z_function.z_function("€ₐ")
        
        self.assertEqual([0, 0], actual)
    
    def test_z_function2(self):
        """
        input_str = 'o2o2'
        """
        actual = strings.z_function.z_function("o2o2")
        
        self.assertEqual([0, 0, 2, 0, 0], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.z_function.go_next
    
    # region FUZZER
    
    def test_go_next(self):
        """
        i = positive
        z_result = builtins.list[builtins.int]
        s = 'oo'
        """
        actual = strings.z_function.go_next(1, [1, 562949953421313], "oo")
        
        self.assertEqual(False, actual)
    
    def test_go_next_with_exception(self):
        """
        i = 170141183460391860479231967448702910463 (mutated from max)
        z_result = builtins.list[builtins.int]
        s = 'abcdefghijklmnopqrst'
        """
        # This test fails because function [strings.z_function.go_next] produces [IndexError]
        strings.z_function.go_next(170141183460391860479231967448702910463, [], "abcdefghijklmnopqrst")
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.z_function.find_pattern
    
    # region FUZZER
    
    def test_find_pattern(self):
        """
        pattern = '€'
        input_str = '-foo'
        """
        actual = strings.z_function.find_pattern("€", "-foo")
        
        self.assertEqual(0, actual)
    
    def test_find_pattern1(self):
        """
        pattern = 'foo'
        input_str = 'foo'
        """
        actual = strings.z_function.find_pattern("foo", "foo")
        
        self.assertEqual(1, actual)
    
    def test_find_pattern2(self):
        """
        pattern = ''
        input_str = ''
        """
        actual = strings.z_function.find_pattern("", "")
        
        self.assertEqual(0, actual)
    # endregion
    
    # endregion

