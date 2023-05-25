import sys
sys.path.append(r'../../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
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
    # endregion
    
    # endregion

