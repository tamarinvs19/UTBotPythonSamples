import sys
sys.path.append(r'../../..')
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
    
    # region Test suites for executable matrix.matrix_class.get_minor
    
    # region FUZZER
    
    def test_get_minor(self):
        """
        self = matrix.matrix_class.Matrix
        row = positive
        column = max
        """
        matrix1 = matrix.matrix_class.Matrix([[1], [1], [32769], [576460752303423489]])
        
        actual = matrix1.get_minor(1, 170141183460469231731687303715884105727)
        
        self.assertEqual(0, actual)
    
    def test_get_minor_with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        row = min
        column = -524289 (mutated from -1)
        """
        matrix1 = matrix.matrix_class.Matrix([])
        # This test fails because function [matrix.matrix_class.get_minor] produces [IndexError]
        matrix1.get_minor(-170141183460469231731687303715884105728, -524289)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_minor_with_exception1(self):
        """
        self = matrix.matrix_class.Matrix
        row = min
        column = -1
        """
        matrix1 = matrix.matrix_class.Matrix([[1, -1, -1, 1, 170141183460469231731687303715884105727], [1237940039285380274899124225, -1, -1, 1, 170141183460469231731687303715884105727], [-1, 170141183460469231731687303715884105727, 1, 1, -1], [1, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 1, 170141183460469231731687303715884105727], [-1, 170141183460469231731687303715884105727, -1, 1, 1]])
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.get_minor(-170141183460469231731687303715884105728, -1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.get_cofactor
    
    # region FUZZER
    
    def test_get_cofactor(self):
        """
        self = matrix.matrix_class.Matrix
        row = 3 (mutated from 2)
        column = positive (mutated from 2)
        """
        matrix1 = matrix.matrix_class.Matrix([[2], [2], [32770], [576460752303423490]])
        
        actual = matrix1.get_cofactor(3, 1)
        
        self.assertEqual(0, actual)
    
    def test_get_cofactor1(self):
        """
        self = matrix.matrix_class.Matrix
        row = zero
        column = -1 (mutated from zero)
        """
        matrix1 = matrix.matrix_class.Matrix([[-1, -170141183460469231731687303715884105728, -2, -1, 2], [-1237940039285380274899124225, -170141183460469231731687303715884105728, -2, -1, 2], [-2, 2, -1, -1, -170141183460469231731687303715884105728], [-1, 0, 170141183460469231731687303715884105726, -1, 2], [-2, 2, -170141183460469231731687303715884105728, -1, -1]])
        
        actual = matrix1.get_cofactor(0, -1)
        
        self.assertEqual(0, actual)
    
    def test_get_cofactor_with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        row = positive (mutated from 2)
        column = 524291 (mutated from 3)
        """
        matrix1 = matrix.matrix_class.Matrix([])
        # This test fails because function [matrix.matrix_class.get_cofactor] produces [IndexError]
        matrix1.get_cofactor(1, 524291)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_get_cofactor_with_exception1(self):
        """
        self = matrix.matrix_class.Matrix
        row = 8 (mutated from zero)
        column = -1 (mutated from zero)
        """
        matrix1 = matrix.matrix_class.Matrix([[-1, -170141183460469231731687303715884105728, -2, -1, 2], [-1237940039285380274899124225, -170141183460469231731687303715884105728, -2, -1, 2], [-2, 2, -1, -1, -170141183460469231731687303715884105728], [-1, 0, 170141183460469231731687303715884105726, -1, 2], [-2, 2, -170141183460469231731687303715884105728, -1, -1]])
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.get_cofactor(8, -1)
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
    
    def test_minors1(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([])
        
        actual = matrix1.minors()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = []
        
        self.assertEqual(expected, actual)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_minors_with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[1, -170141183460469231731687303715884105728, 1, -1, 170141183460469231731687303715884105727], [-1, -170141183460469231731687303715884105728, 1, 1, 170141183460469231731687303715884105727], [-1, 1, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728, 1], [170141183460469231731687303715884105727, 1, -159507359494189904748456847233641349120, -1, 1], [170141183460469231731687303715884105727, 1, -170141183460469231731687303715884105728, -9, 1]])
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.minors()
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
    
    def test_cofactors1(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([])
        
        actual = matrix1.cofactors()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = []
        
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
    
    def test_adjugate1(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([])
        
        actual = matrix1.adjugate()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = []
        
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
    
    # region Test suites for executable matrix.matrix_class.__repr__
    
    # region FUZZER
    
    def test___repr__(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [1, 166153499473114484112975882535043073]])
        
        actual = matrix1.__repr__()
        
        self.assertEqual('[[170141183460469231731687303715884105727, 170141183460469231731687303715884105727], [1, 166153499473114484112975882535043073]]', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.__str__
    
    # region FUZZER
    
    def test___str__(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[-170141183460469231731687303715884105728, -170141183460469231731687303715884105728], [1, 166153499473114484112975882535043073]])
        
        actual = matrix1.__str__()
        
        self.assertEqual('[[-170141183460469231731687303715884105728. -170141183460469231731687303715884105728.]\n [1. 166153499473114484112975882535043073.]]', actual)
    
    def test___str__1(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([])
        
        actual = matrix1.__str__()
        
        self.assertEqual('[]', actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.__ne__
    
    # region FUZZER
    
    def test___ne__(self):
        """
        self = matrix.matrix_class.Matrix
        other = builtins.object
        """
        matrix1 = matrix.matrix_class.Matrix([[0, -170141183460469231731687303715884105728], [-1, 1]])
        other = builtins.object()
        other1 = other
        
        actual = matrix1.__ne__(other1)
        
        self.assertEqual(True, actual)
        
        self.assertEqual(other, other1)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.__neg__
    
    # region FUZZER
    
    def test___neg__(self):
        """
        self = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[-2, -2], [2, 166153499473114484112975882535043074]])
        
        actual = matrix1.__neg__()
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = [[2, 2], [-2, -166153499473114484112975882535043074]]
        
        self.assertEqual(expected, actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.__add__
    
    # region FUZZER
    
    def test___add___with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        other = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[-1, 0, 170141183460469231731687303715884105727], [0, 170141183460469231731687303715884105727, -1], [170141183460469231731687303715884105727, 0, -1], [-1, 0, 170141183457993351653116543166085857279], [-1, 0, -1]])
        other = matrix.matrix_class.Matrix([[0, 170141183460469080615959851887237267455, 170141183460469231731687303715884105727, 0], [170141183460469231731687303715884105727, 0, 170141183460469231731687303715884105727, 0], [0, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 0], [0, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 0]])
        # This test fails because function [matrix.matrix_class.__add__] produces [ValueError]
        matrix1.__add__(other)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.__sub__
    
    # region FUZZER
    
    def test___sub___with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        other = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[-1, 0, 170141183460469231731687303715884105727], [0, 170141183460469231731687303715884105727, -1], [170141183460469231731687303715884105727, 0, -1], [-1, 0, 170141183457993351653116543166085857279], [-1, 0, -1]])
        other = matrix.matrix_class.Matrix([[0, 170141183460469080615959851887237267455, 170141183460469231731687303715884105727, 0], [170141183460469231731687303715884105727, 0, 170141183460469231731687303715884105727, 0], [0, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 0], [0, 170141183460469231731687303715884105727, 170141183460469231731687303715884105727, 0]])
        # This test fails because function [matrix.matrix_class.__sub__] produces [ValueError]
        matrix1.__sub__(other)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.__mul__
    
    # region FUZZER
    
    def test___mul__(self):
        """
        self = matrix.matrix_class.Matrix
        other = zero
        """
        matrix1 = matrix.matrix_class.Matrix([[-170141183460469231731687303715884105728, -1], [170141183460469231731687303715884105727, -1]])
        
        actual = matrix1.__mul__(0)
        
        expected = object.__new__(matrix.matrix_class.Matrix)
        expected.rows = [[0, 0], [0, 0]]
        
        self.assertEqual(expected, actual)
    
    def test___mul___with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        other = float('inf')
        """
        matrix1 = matrix.matrix_class.Matrix([[1]])
        # This test fails because function [matrix.matrix_class.__mul__] produces [OverflowError]
        matrix1.__mul__(float('inf'))
    
    def test___mul___with_exception1(self):
        """
        self = matrix.matrix_class.Matrix
        other = matrix.matrix_class.Matrix
        """
        matrix1 = matrix.matrix_class.Matrix([[1]])
        other = matrix.matrix_class.Matrix([[-170141183460469231731687303715884105728, -170141183460469231731687233347139928064, 0], [-170141183460469231731687303715884105728, 1, 0], [170141183460469231731687303715884105727, 170141183460469231731687303715883057151, 170141183460469231731687303698704236543]])
        # This test fails because function [matrix.matrix_class.__mul__] produces [ValueError]
        matrix1.__mul__(other)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.matrix_class.__pow__
    
    # region FUZZER
    
    def test___pow___with_exception(self):
        """
        self = matrix.matrix_class.Matrix
        other = -170141183460469231731687303715884105726 (mutated from 2)
        """
        matrix1 = matrix.matrix_class.Matrix([[2]])
        # This test fails because function [matrix.matrix_class.__pow__] produces [IndexError]
        matrix1.__pow__(-170141183460469231731687303715884105726)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___pow___with_exception1(self):
        """
        self = matrix.matrix_class.Matrix
        other = 38685626227668137885827074 (mutated from -170141183460430546105459635577998278654)
        """
        matrix1 = matrix.matrix_class.Matrix([[2]])
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__pow__(38685626227668137885827074)
    # endregion
    
    # endregion

