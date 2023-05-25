import sys
sys.path.append(r'../../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.lempel_ziv.add_key_to_lexicon
    
    # region FUZZER
    
    def test_add_key_to_lexicon_with_exception(self):
        """
        lexicon = builtins.dict[typing.Any, typing.Any]
        curr_string = '0'
        index = 66 (mutated from 2)
        last_match_id = 'abcdefghijklmnopqrst'
        """
        # This test fails because function [compression.lempel_ziv.add_key_to_lexicon] produces [KeyError]
        compression.lempel_ziv.add_key_to_lexicon({}, "0", 66, "abcdefghijklmnopqrst")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv.compress_data
    
    # region FUZZER
    
    def test_compress_data(self):
        """
        data_bits = '0'
        """
        actual = compression.lempel_ziv.compress_data("0")
        
        self.assertEqual('0', actual)
    
    def test_compress_data1(self):
        """
        data_bits = ''
        """
        actual = compression.lempel_ziv.compress_data("")
        
        self.assertEqual('', actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_compress_data_with_exception(self):
        """
        data_bits = '+'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        compression.lempel_ziv.compress_data("+")
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_compress_data_with_exception1(self):
        """
        data_bits = ''
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        compression.lempel_ziv.compress_data("")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv.add_file_length
    
    # region FUZZER
    
    def test_add_file_length(self):
        """
        source_path = '€'
        compressed = 'fo'
        """
        actual = compression.lempel_ziv.add_file_length("../../€", "fo")
        
        self.assertEqual('0fo\x94', actual)
    
    def test_add_file_length_with_exception(self):
        """
        source_path = 'abcdefghijklmnopqrs+t'
        compressed = '+'
        """
        # This test fails because function [compression.lempel_ziv.add_file_length] produces [FileNotFoundError]
        compression.lempel_ziv.add_file_length("abcdefghijklmnopqrs+t", "+")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv.write_file_binary
    
    # region FUZZER
    
    def test_write_file_binary_with_exception(self):
        """
        file_path = '€'
        to_write = 'pyth7ön'
        """
        # This test fails because function [compression.lempel_ziv.write_file_binary] produces [ValueError]
        compression.lempel_ziv.write_file_binary("../../€", "pyth7ön")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv.compress
    
    # region FUZZER
    
    def test_compress(self):
        """
        source_path = '€'
        destination_path = '-foo'
        """
        actual = compression.lempel_ziv.compress("../../€", "-foo")
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

