import sys
sys.path.append(r'../..')
import builtins
import data_structures.hashing.bloom_filter
import types
import data_structures
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable data_structures.hashing.bloom_filter.add
    
    # region FUZZER
    
    def test_add(self):
        """
        self = data_structures.hashing.bloom_filter.Bloom
        value = 'fo'
        """
        bloom = data_structures.hashing.bloom_filter.Bloom()
        
        actual = bloom.add("fo")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(bloom, bloom)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.hashing.bloom_filter.exists
    
    # region FUZZER
    
    def test_exists(self):
        """
        self = data_structures.hashing.bloom_filter.Bloom
        value = 'fo'
        """
        bloom = data_structures.hashing.bloom_filter.Bloom()
        
        actual = bloom.exists("fo")
        
        self.assertEqual(False, actual)
        
        self.assertEqual(bloom, bloom)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.hashing.bloom_filter.__contains__
    
    # region FUZZER
    
    def test___contains__(self):
        """
        self = data_structures.hashing.bloom_filter.Bloom
        other = 'fo'
        """
        bloom = data_structures.hashing.bloom_filter.Bloom()
        
        actual = bloom.__contains__("fo")
        
        self.assertEqual(False, actual)
        
        self.assertEqual(bloom, bloom)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.hashing.bloom_filter.format_bin
    
    # region FUZZER
    
    def test_format_bin(self):
        """
        self = data_structures.hashing.bloom_filter.Bloom
        bitarray = 64 (mutated from zero)
        """
        bloom = data_structures.hashing.bloom_filter.Bloom()
        
        actual = bloom.format_bin(64)
        
        self.assertEqual('01000000', actual)
        
        self.assertEqual(bloom, bloom)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.hashing.bloom_filter.hash_
    
    # region FUZZER
    
    def test_hash_(self):
        """
        self = data_structures.hashing.bloom_filter.Bloom
        value = 'abcdefghijklmnopqrs'
        """
        bloom = data_structures.hashing.bloom_filter.Bloom()
        
        actual = bloom.hash_("abcdefghijklmnopqrs")
        
        self.assertEqual(4, actual)
        
        self.assertEqual(bloom, bloom)
    # endregion
    
    # endregion
    
    # region Test suites for executable data_structures.hashing.bloom_filter.format_hash
    
    # region FUZZER
    
    def test_format_hash(self):
        """
        self = data_structures.hashing.bloom_filter.Bloom
        value = 'fo'
        """
        bloom = data_structures.hashing.bloom_filter.Bloom()
        
        actual = bloom.format_hash("fo")
        
        self.assertEqual('01010000', actual)
        
        self.assertEqual(bloom, bloom)
    # endregion
    
    # endregion

