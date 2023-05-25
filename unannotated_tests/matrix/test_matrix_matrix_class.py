import sys
sys.path.append(r'..\..\..')
import matrix.matrix_class
import builtins
import matrix
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.matrix_class.columns
    
    # region FUZZER
    
    def test_columns(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [-170141183460469231731687303715884105728, -169975029960996117247574327833349062656]])
        
        actual = matrix1.columns()
        
        self.assertEqual([[170141183460469231731687303715884105727, -170141183460469231731687303715884105728], [170141183460469231731687303715884105727, -169975029960996117247574327833349062656]], actual)
    
    def test_columns_with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([])
        # This test fails because function [matrix.matrix_class.columns] produces [IndexError]
        matrix1.columns()
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.identity
    
    # region FUZZER
    
    def test_identity(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[-170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [1, 166153499473114484112975882535043073]])
        
        actual = matrix1.identity()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = [[1, 0], [0, 1]]
        
        self.assertEqual(expected, actual)
    
    def test_identity1(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([])
        
        actual = matrix1.identity()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = []
        
        self.assertEqual(expected, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.is_invertable
    
    # region FUZZER
    
    def test_is_invertable(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [1, 166153499473114484112975882535043073]])
        
        actual = matrix1.is_invertable()
        
        self.assertEqual(True, actual)
    
    def test_is_invertable_with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([])
        # This test fails because function [matrix.matrix_class.is_invertable] produces [IndexError]
        matrix1.is_invertable()
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.minors
    
    # region FUZZER
    
    def test_minors(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [1, 166153499473114484112975882535043073]])
        
        actual = matrix1.minors()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = [[166153499473114484112975882535043073, 1], [170141183460469231731687303715884105727, 170141183460469231731687303715884105727]]
        
        self.assertEqual(expected, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.cofactors
    
    # region FUZZER
    
    def test_cofactors(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[-170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [3, 166153499473114484112975882535043075]])
        
        actual = matrix1.cofactors()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = [[166153499473114484112975882535043075, -3], [170141183460469231731687303715884105728, -170141183460469231731687303715884105728]]
        
        self.assertEqual(expected, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.adjugate
    
    # region FUZZER
    
    def test_adjugate(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [1, 166153499473114484112975882535043073]])
        
        actual = matrix1.adjugate()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = [[166153499473114484112975882535043073, -170141183460469231731687303715884105727], [-1, 170141183460469231731687303715884105727]]
        
        self.assertEqual(expected, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.inverse
    
    # region FUZZER
    
    def test_inverse(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[-1, -1], [2, 166153499473114484112975882535043074]])
        
        actual = matrix1.inverse()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = [[-1, 0], [0, 0]]
        
        self.assertEqual(expected, actual)
    # endregion
    
    # endregion

