import sys
sys.path.append(r'../../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.lempel_ziv_decompress.decompress_data
    
    # region FUZZER
    
    def test_decompress_data(self):
        """
        data_bits = '1'
        """
        actual = compression.lempel_ziv_decompress.decompress_data("1")
        
        self.assertEqual('1', actual)
    
    def test_decompress_data1(self):
        """
        data_bits = '+'
        """
        actual = compression.lempel_ziv_decompress.decompress_data("+")
        
        self.assertEqual('', actual)
    
    def test_decompress_data2(self):
        """
        data_bits = '1'
        """
        actual = compression.lempel_ziv_decompress.decompress_data("1")
        
        self.assertEqual('1', actual)
    
    def test_decompress_data3(self):
        """
        data_bits = ''
        """
        actual = compression.lempel_ziv_decompress.decompress_data("")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv_decompress.write_file_binary
    
    # region FUZZER
    
    def test_write_file_binary(self):
        """
        file_path = '€'
        to_write = 'pyth7ön'
        """
        actual = compression.lempel_ziv_decompress.write_file_binary("../../€", "pyth7ön")
        
        self.assertEqual(None, actual)
    
    def test_write_file_binary1(self):
        """
        file_path = 'oo'
        to_write = '10000000'
        """
        actual = compression.lempel_ziv_decompress.write_file_binary("../../oo", "10000000")
        
        self.assertEqual(None, actual)
    
    def test_write_file_binary_with_exception(self):
        """
        file_path = '0'
        to_write = 'abcdefghijklmnopqrst'
        """
        # This test fails because function [compression.lempel_ziv_decompress.write_file_binary] produces [ValueError]
        compression.lempel_ziv_decompress.write_file_binary("../../0", "abcdefghijklmnopqrst")
    
    def test_write_file_binary_with_exception1(self):
        """
        file_path = '₻€₤'
        to_write = 'yh7X¾;ön'
        """
        # This test fails because function [compression.lempel_ziv_decompress.write_file_binary] produces [ValueError]
        compression.lempel_ziv_decompress.write_file_binary("../../₻€₤", "yh7X¾;ön")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv_decompress.remove_prefix
    
    # region FUZZER
    
    def test_remove_prefix(self):
        """
        data_bits = ''
        """
        actual = compression.lempel_ziv_decompress.remove_prefix("")
        
        self.assertEqual('', actual)
    
    def test_remove_prefix1(self):
        """
        data_bits = '€'
        """
        actual = compression.lempel_ziv_decompress.remove_prefix("€")
        
        self.assertEqual('', actual)
    
    def test_remove_prefix2(self):
        """
        data_bits = '1.'
        """
        actual = compression.lempel_ziv_decompress.remove_prefix("1.")
        
        self.assertEqual('.', actual)
    
    def test_remove_prefix3(self):
        """
        data_bits = ' 1'
        """
        actual = compression.lempel_ziv_decompress.remove_prefix(" 1")
        
        self.assertEqual('', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv_decompress.compress
    
    # region FUZZER
    
    def test_compress_with_exception(self):
        """
        source_path = '€'
        destination_path = '-foo'
        """
        # This test fails because function [compression.lempel_ziv_decompress.compress] produces [IndexError]
        compression.lempel_ziv_decompress.compress("../../€", "-foo")
    # endregion
    
    # endregion

