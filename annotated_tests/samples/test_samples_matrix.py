import sys
sys.path.append(r'../../..')
import samples.matrix
import builtins
import types
import samples
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.matrix.__repr__
    
    # region FUZZER
    
    def test___repr__(self):
        """
        self = samples.matrix.Matrix
        """
        matrix = samples.matrix.Matrix([[]])
        
        actual = matrix.__repr__()
        
        self.assertEqual('[[]]', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.matrix.__eq__
    
    # region FUZZER
    
    def test___eq__(self):
        """
        self = samples.matrix.Matrix
        other = samples.matrix.Matrix
        """
        matrix = samples.matrix.Matrix([[float('-inf'), float('nan')], [float('-inf'), float('-inf')]])
        other = samples.matrix.Matrix([[float('nan')]])
        
        actual = matrix.__eq__(other)
        
        self.assertEqual(False, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.matrix.__add__
    
    # region FUZZER
    
    def test___add__(self):
        """
        self = samples.matrix.Matrix
        other = samples.matrix.Matrix
        """
        matrix = samples.matrix.Matrix([[float('nan'), float('nan'), float('nan'), float('nan')], [0.0, 1.1126727369842225E-308, 1.1125369333981237E-308, 1.1125369292536165E-308, 2.0522684006491881E-289], [float('inf'), float('inf'), float('-inf'), float('nan'), float('inf')], [float('inf'), float('nan'), 0.0, float('nan'), float('nan')], [float('-inf'), float('nan'), float('inf'), float('inf'), float('inf')]])
        other = samples.matrix.Matrix([[float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')]])
        
        actual = matrix.__add__(other)
        
        expected = object.__new__(samples.matrix.Matrix)
        expected.dim = (5, 5)
        expected.elements = [[float('nan'), float('nan'), float('nan'), float('nan'), float('-inf')], [float('-inf'), float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('nan'), float('nan'), float('-inf'), float('nan'), float('nan')], [float('nan'), float('nan'), float('-inf'), float('nan'), float('nan')], [float('-inf'), float('nan'), float('nan'), float('nan'), float('nan')]]
        actual_dim = actual.dim
        expected_dim = expected.dim
        
        self.assertEqual(expected_dim, actual_dim)
        actual_elements = actual.elements
        expected_elements = expected.elements
        expected_list = expected_elements
        expected_length = len(expected_list)
        actual_length = len(actual_elements)
        
        self.assertEqual(expected_length, actual_length)
        
        self.assertTrue(isinstance(actual_elements, builtins.list))
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.matrix.__mul__
    
    # region FUZZER
    
    def test___mul__(self):
        """
        self = samples.matrix.Matrix
        other = max (mutated from -1)
        """
        matrix = samples.matrix.Matrix([[float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('inf'), float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan')]])
        
        actual = matrix.__mul__(170141183460469231731687303715884105727)
        
        expected = object.__new__(samples.matrix.Matrix)
        expected.dim = (4, 4)
        expected.elements = [[float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('-inf'), float('-inf'), float('-inf'), float('-inf')], [float('inf'), float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan'), 0]]
        actual_dim = actual.dim
        expected_dim = expected.dim
        
        self.assertEqual(expected_dim, actual_dim)
        actual_elements = actual.elements
        expected_elements = expected.elements
        expected_list = expected_elements
        expected_length = len(expected_list)
        actual_length = len(actual_elements)
        
        self.assertEqual(expected_length, actual_length)
        
        self.assertTrue(isinstance(actual_elements, builtins.list))
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.matrix.__matmul__
    
    # region FUZZER
    
    def test___matmul__(self):
        """
        self = samples.matrix.Matrix
        other = samples.matrix.Matrix
        """
        matrix = samples.matrix.Matrix([[1.0, 7.458340731200207E-155, 1.0000000004656613, 0.5], [float('-inf'), float('-inf')], [0.0, 1.112536929253601E-308, -1.1125369292536007E-308, 7.2911220195563975E-304], [1.0, 0.0, 1.0, float('nan')]])
        other = samples.matrix.Matrix([[1.0, -1.0, 1.0000000000002274, 1.0000001192092896, 2.9387358770557188E-39], [1.0000001192092896, -1.0, 1.0, 2.9387358770557188E-39, 1.0000000000002274], [1.0, 2.9387358770557188E-39, -1.0, 1.0000000000002274, 1.0000001192092896], [1.0000000000002274, 1.0000001192092896, 1.0, -1.0, 2.9387358770557188E-39], [-1.0, 2.938735888003363E-39, 1.0, 1.0000001192092896, 1.0000000000002274]])
        
        actual = matrix.__matmul__(other)
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.matrix.is_diagonal
    
    # region FUZZER
    
    def test_is_diagonal(self):
        """
        self = samples.matrix.Matrix
        """
        matrix = samples.matrix.Matrix([[float('-inf'), 0.0], [float('-inf'), 2.8480945388892178E-306]])
        
        actual = matrix.is_diagonal()
        
        self.assertEqual(False, actual)
    
    def test_is_diagonal1(self):
        """
        self = samples.matrix.Matrix
        """
        matrix = samples.matrix.Matrix([[0.0, 0.0], [0.0, 1.129920318773188E-308]])
        
        actual = matrix.is_diagonal()
        
        self.assertEqual(True, actual)
    
    def test_is_diagonal2(self):
        """
        self = samples.matrix.Matrix
        """
        matrix = samples.matrix.Matrix([])
        
        actual = matrix.is_diagonal()
        
        self.assertEqual(True, actual)
    
    def test_is_diagonal_with_exception(self):
        """
        self = samples.matrix.Matrix
        """
        matrix = samples.matrix.Matrix([[0.0, 1.1125369292546125E-308, 4.7783097267364807E-299, -1.1125369292536007E-308], [float('nan'), float('-inf'), 1.0], [0.0, 0.0, float('nan')]])
        # This test fails because function [samples.matrix.is_diagonal] produces [samples.matrix.MatrixException]
        matrix.is_diagonal()
    # endregion
    
    # endregion

