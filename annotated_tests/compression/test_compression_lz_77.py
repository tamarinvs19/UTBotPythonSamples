import sys
sys.path.append(r'../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.lz77.__repr__
    
    # region FUZZER
    
    def test___repr__(self):
        """
        self = compression.lz77.Token
        """
        token = compression.lz77.Token(170141183460469231731687303715884105727, 1, "abcdefghijklmnopqrst")
        
        actual = token.__repr__()
        
        self.assertEqual('(170141183460469231731687303715884105727, 1, abcdefghijklmnopqrst)', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lz77.compress
    
    # region FUZZER
    
    def test_compress(self):
        """
        self = compression.lz77.LZ77Compressor
        text = 'fo'
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        
        actual = l_z77_compressor.compress("fo")
        
        token = object.__new__(compression.lz77.Token)
        token.offset = 0
        token.length = 0
        token.indicator = 'f'
        token1 = object.__new__(compression.lz77.Token)
        token1.offset = 0
        token1.length = 0
        token1.indicator = 'o'
        token2 = object.__new__(compression.lz77.Token)
        token2.offset = 0
        token2.length = 0
        token2.indicator = '\x94'
        
        self.assertEqual([token, token1, token2], actual)
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    
    def test_compress1(self):
        """
        self = compression.lz77.LZ77Compressor
        text = '«ly<o_Ê'
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        
        actual = l_z77_compressor.compress("«ly<o_Ê")
        
        token = object.__new__(compression.lz77.Token)
        token.offset = 0
        token.length = 0
        token.indicator = '«'
        token1 = object.__new__(compression.lz77.Token)
        token1.offset = 0
        token1.length = 0
        token1.indicator = 'l'
        token2 = object.__new__(compression.lz77.Token)
        token2.offset = 0
        token2.length = 0
        token2.indicator = 'y'
        token3 = object.__new__(compression.lz77.Token)
        token3.offset = 0
        token3.length = 0
        token3.indicator = '<'
        token4 = object.__new__(compression.lz77.Token)
        token4.offset = 0
        token4.length = 0
        token4.indicator = 'o'
        token5 = object.__new__(compression.lz77.Token)
        token5.offset = 0
        token5.length = 0
        token5.indicator = '_'
        token6 = object.__new__(compression.lz77.Token)
        token6.offset = 0
        token6.length = 0
        token6.indicator = '\x91'
        token7 = object.__new__(compression.lz77.Token)
        token7.offset = 0
        token7.length = 0
        token7.indicator = 'Ê'
        
        self.assertEqual([token, token1, token2, token3, token4, token5, token6, token7], actual)
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    
    def test_compress2(self):
        """
        self = compression.lz77.LZ77Compressor
        text = ''
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        
        actual = l_z77_compressor.compress("")
        
        self.assertEqual([], actual)
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lz77.decompress
    
    # region FUZZER
    
    def test_decompress(self):
        """
        self = compression.lz77.LZ77Compressor
        tokens = builtins.list[compression.lz77.Token]
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        token = compression.lz77.Token(-170141183460469231731687303715884105728, -170141183460469231731687303715884105728, "foo")
        token1 = compression.lz77.Token(-170141183460469231731687303715884105728, -170141183460469231731687303715883974656, "foo")
        
        actual = l_z77_compressor.decompress([token, token1])
        
        self.assertEqual('foofoo', actual)
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lz77._find_encoding_token
    
    # region FUZZER
    
    def test__find_encoding_token(self):
        """
        self = compression.lz77.LZ77Compressor
        text = 'foo'
        search_buffer = 'pytönP'
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        
        actual = l_z77_compressor._find_encoding_token("foo", "pytönP")
        
        expected = object.__new__(compression.lz77.Token)
        expected.offset = 0
        expected.length = 0
        expected.indicator = 'f'
        
        self.assertEqual(expected, actual)
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    
    def test__find_encoding_token1(self):
        """
        self = compression.lz77.LZ77Compressor
        text = 'yq'
        search_buffer = 'yötnZĲP'
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        
        actual = l_z77_compressor._find_encoding_token("yq", "yötnZĲP")
        
        expected = object.__new__(compression.lz77.Token)
        expected.offset = 7
        expected.length = 1
        expected.indicator = 'q'
        
        self.assertEqual(expected, actual)
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    
    def test__find_encoding_token_with_exception(self):
        """
        self = compression.lz77.LZ77Compressor
        text = 'y'
        search_buffer = 'ø<yötnZ cĲP'
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        # This test fails because function [compression.lz77._find_encoding_token] produces [IndexError]
        l_z77_compressor._find_encoding_token("y", "ø<yötnZ cĲP")
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    
    def test__find_encoding_token_with_exception1(self):
        """
        self = compression.lz77.LZ77Compressor
        text = ''
        search_buffer = '<yötnZ cĲP'
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        # This test fails because function [compression.lz77._find_encoding_token] produces [ValueError]
        l_z77_compressor._find_encoding_token("", "<yötnZ cĲP")
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.lz77._match_length_from_index
    
    # region FUZZER
    
    def test__match_length_from_index(self):
        """
        self = compression.lz77.LZ77Compressor
        text = 'foo'
        window = '€'
        text_index = -1 (mutated from zero)
        window_index = -1 (mutated from max)
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        
        actual = l_z77_compressor._match_length_from_index("foo", "€", -1, -1)
        
        self.assertEqual(0, actual)
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    
    def test__match_length_from_index_with_exception(self):
        """
        self = compression.lz77.LZ77Compressor
        text = 'foo'
        window = 'pytMhö'
        text_index = -1 (mutated from zero)
        window_index = min
        """
        l_z77_compressor = compression.lz77.LZ77Compressor()
        # This test fails because function [compression.lz77._match_length_from_index] produces [IndexError]
        l_z77_compressor._match_length_from_index("foo", "pytMhö", -1, -170141183460469231731687303715884105728)
        
        self.assertEqual(l_z77_compressor, l_z77_compressor)
    # endregion
    
    # endregion

