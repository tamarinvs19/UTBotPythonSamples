import sys
sys.path.append(r'..\..\..')
import builtins
import strings
import unittest
import strings.dna


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.dna.dna
    
    # region FUZZER
    
    def test_dna(self):
        """
        dna = 'TGC'
        """
        actual = strings.dna.dna("TGC")
        
        self.assertEqual('ACG', actual)
    
    def test_dna_with_exception(self):
        """
        dna = 'TCG'
        """
        # This test fails because function [strings.dna.dna] produces [ValueError]
        strings.dna.dna("TCG")
    # endregion
    
    # endregion

