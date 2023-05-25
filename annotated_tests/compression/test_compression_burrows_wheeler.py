import sys
sys.path.append(r'../..')
from annotated_tests import compression
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable compression.burrows_wheeler.all_rotations
    
    # region FUZZER
    
    def test_all_rotations(self):
        """
        s = 'The parameter s type must be st.'
        """
        actual = compression.burrows_wheeler.all_rotations("The parameter s type must be st.")
        
        self.assertEqual(['The parameter s type must be st.', 'he parameter s type must be st.T', 'e parameter s type must be st.Th', ' parameter s type must be st.The', 'parameter s type must be st.The ', 'arameter s type must be st.The p', 'rameter s type must be st.The pa', 'ameter s type must be st.The par', 'meter s type must be st.The para', 'eter s type must be st.The param', 'ter s type must be st.The parame', 'er s type must be st.The paramet', 'r s type must be st.The paramete', ' s type must be st.The parameter', 's type must be st.The parameter ', ' type must be st.The parameter s', 'type must be st.The parameter s ', 'ype must be st.The parameter s t', 'pe must be st.The parameter s ty', 'e must be st.The parameter s typ', ' must be st.The parameter s type', 'must be st.The parameter s type ', 'ust be st.The parameter s type m', 'st be st.The parameter s type mu', 't be st.The parameter s type mus', ' be st.The parameter s type must', 'be st.The parameter s type must ', 'e st.The parameter s type must b', ' st.The parameter s type must be', 'st.The parameter s type must be ', 't.The parameter s type must be s', '.The parameter s type must be st'], actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.burrows_wheeler.bwt_transform
    
    # region FUZZER
    
    def test_bwt_transform(self):
        """
        s = 'abcdefBhijklmnopqrst'
        """
        actual = compression.burrows_wheeler.bwt_transform("abcdefBhijklmnopqrst")
        
        self.assertEqual({'bwt_string': 'ftabcdeBhijklmnopqrs', 'idx_original_string': 1, }, actual)
    
    def test_bwt_transform_with_exception(self):
        """
        s = ''
        """
        # This test fails because function [compression.burrows_wheeler.bwt_transform] produces [ValueError]
        compression.burrows_wheeler.bwt_transform("")
    # endregion
    
    # endregion
    
    # region Test suites for executable compression.burrows_wheeler.reverse_bwt
    
    # region FUZZER
    
    def test_reverse_bwt(self):
        """
        bwt_string = 'The parameter bwt_string type must be str.'
        idx_original_string = zero (mutated from min)
        """
        actual = compression.burrows_wheeler.reverse_bwt("The parameter bwt_string type must be str.", 0)
        
        self.assertEqual('  rwebea ttaT  rwebea ttaT  rwebea ttaT  r', actual)
    
    def test_reverse_bwt_with_exception(self):
        """
        bwt_string = 'The parameter dx_original_string must be lower than'
        idx_original_string = -1 (mutated from zero)
        """
        # This test fails because function [compression.burrows_wheeler.reverse_bwt] produces [ValueError]
        compression.burrows_wheeler.reverse_bwt("The parameter dx_original_string must be lower than", -1)
    
    def test_reverse_bwt_with_exception1(self):
        """
        bwt_string = ''
        idx_original_string = 19807040628566084398385987584 (mutated from zero)
        """
        # This test fails because function [compression.burrows_wheeler.reverse_bwt] produces [ValueError]
        compression.burrows_wheeler.reverse_bwt("", 19807040628566084398385987584)
    
    def test_reverse_bwt_with_exception2(self):
        """
        bwt_string = '¨'
        idx_original_string = 19807040628566084398385987584 (mutated from zero)
        """
        # This test fails because function [compression.burrows_wheeler.reverse_bwt] produces [ValueError]
        compression.burrows_wheeler.reverse_bwt("¨", 19807040628566084398385987584)
    # endregion
    
    # endregion

