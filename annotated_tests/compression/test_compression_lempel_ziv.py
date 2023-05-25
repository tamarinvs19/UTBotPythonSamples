import sys
sys.path.append(r'../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.lempel_ziv.add_key_to_lexicon
    
    # region FUZZER
    
    def test_add_key_to_lexicon(self):
        """
        lexicon = builtins.dict[builtins.str, builtins.str]
        curr_string = '0'
        index = 3 (mutated from 2)
        last_match_id = ''
        """
        lexicon = {"0": "0", }
        
        actual = compression.lempel_ziv.add_key_to_lexicon(lexicon, "0", 3, "")
        
        self.assertEqual(None, actual)
        
        self.assertEqual({'00': '', '01': '11', }, lexicon)
    
    def test_add_key_to_lexicon1(self):
        """
        lexicon = builtins.dict[builtins.str, builtins.str]
        curr_string = '0'
        index = 295147905179352825859 (mutated from 3)
        last_match_id = ''
        """
        lexicon = {"0": "￸0", }
        
        actual = compression.lempel_ziv.add_key_to_lexicon(lexicon, "0", 295147905179352825859, "")
        
        self.assertEqual(None, actual)
        
        self.assertEqual({'00': '0', '01': '100000000000000000000000000000000000000000000000000000000000000000011', }, lexicon)
    
    def test_add_key_to_lexicon_with_exception(self):
        """
        lexicon = builtins.dict[builtins.str, builtins.str]
        curr_string = ''
        index = max
        last_match_id = '0'
        """
        # This test fails because function [compression.lempel_ziv.add_key_to_lexicon] produces [KeyError]
        compression.lempel_ziv.add_key_to_lexicon({"pythön": "0", }, "", 170141183460469231731687303715884105727, "0")
    
    def test_add_key_to_lexicon_with_exception1(self):
        """
        lexicon = builtins.dict[builtins.str, builtins.str]
        curr_string = '1'
        index = -170141183460469231731687303715884105600 (mutated from min)
        last_match_id = 'pythön'
        """
        lexicon = {"1": "1", }
        # This test fails because function [compression.lempel_ziv.add_key_to_lexicon] produces [ValueError]
        compression.lempel_ziv.add_key_to_lexicon(lexicon, "1", -170141183460469231731687303715884105600, "pythön")
        
        self.assertEqual({'10': 'pythön', }, lexicon)
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
        data_bits = '0￸'
        """
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        compression.lempel_ziv.compress_data("0￸")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv.add_file_length
    
    # region FUZZER
    
    def test_add_file_length_with_exception(self):
        """
        source_path = '€'
        compressed = 'fo'
        """
        # This test fails because function [compression.lempel_ziv.add_file_length] produces [FileNotFoundError]
        compression.lempel_ziv.add_file_length("../€", "fo")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv.write_file_binary
    
    # region FUZZER
    
    def test_write_file_binary(self):
        """
        file_path = '1'
        to_write = '1'
        """
        actual = compression.lempel_ziv.write_file_binary("../1", "1")
        
        self.assertEqual(None, actual)
    
    def test_write_file_binary1(self):
        """
        file_path = '10000000'
        to_write = '10000000'
        """
        actual = compression.lempel_ziv.write_file_binary("../10000000", "10000000")
        
        self.assertEqual(None, actual)
    
    def test_write_file_binary_with_exception(self):
        """
        file_path = '€'
        to_write = 'pyth7ön'
        """
        # This test fails because function [compression.lempel_ziv.write_file_binary] produces [ValueError]
        compression.lempel_ziv.write_file_binary("../€", "pyth7ön")
    
    def test_write_file_binary_with_exception1(self):
        """
        file_path = '0'
        to_write = ''
        """
        # This test fails because function [compression.lempel_ziv.write_file_binary] produces [IndexError]
        compression.lempel_ziv.write_file_binary("../0", "")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lempel_ziv.compress
    
    # region FUZZER
    
    def test_compress(self):
        """
        source_path = '€'
        destination_path = '-foo'
        """
        actual = compression.lempel_ziv.compress("../€", "-foo")
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

