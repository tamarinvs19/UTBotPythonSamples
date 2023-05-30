import sys
sys.path.append(r'../../..')
import matrix.sherman_morrison
import builtins
import matrix
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable matrix.sherman_morrison.__str__
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___str___with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, -170141183460469231731687299317837594624)
        matrix1.array = [[float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [0.0, 1.1125369292546125E-308, 1.4916681462400413E-154, 1.1125369292556244E-308, 1.7800590868057611E-307], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]]
        matrix1.column = -170141183460469231731687303715884105728
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__str__()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___str___with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, -170141183460469231731687303715850551296)
        matrix1.row = -1
        matrix1.array = []
        matrix1.column = 0
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__str__()
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.__repr__
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___repr___with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 1)
        matrix1.array = [[float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('nan'), float('nan'), float('-inf')]]
        matrix1.column = 170141183460469231731687303715884105727
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__repr__()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___repr___with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(1, 170141183460469231731687303715884105727)
        matrix1.row = 0
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__repr__()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___repr___with_exception2(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(1, 170141183460469231731687303715884105719)
        matrix1.row = -170141183460469231731687303715884105728
        matrix1.array = [[float('inf'), float('inf')], [float('inf'), float('inf')]]
        matrix1.column = -1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__repr__()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___repr___with_exception3(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 170141183460469231731687303715884105727)
        matrix1.row = -1
        matrix1.column = 170141183460469231731687303715884105727
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__repr__()
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.validate_indicies
    
    # region FUZZER
    
    def test_validate_indicies(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        """
        matrix1 = matrix.sherman_morrison.Matrix(-1, -170141183460469231731687303715884105728)
        
        actual = matrix1.validate_indicies((67108867, 1))
        
        self.assertEqual(False, actual)
        
        self.assertEqual(matrix1, matrix1)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_validate_indicies_with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 2)
        matrix1.array = [[2.0, 0.0, -2.0, -2.0], [-2.0, -2.0, 0.0, 2.0], [-2.0, -2.0, 0.0, 2.0], [2.6815615859885194E154, 0.0, -2.0, -2.0]]
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.validate_indicies((-1, 0))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_validate_indicies_with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, -1)
        matrix1.row = 0
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.validate_indicies((-1, -17179869185))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_validate_indicies_with_exception2(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 0)
        matrix1.array = [[float('-inf')]]
        matrix1.row = 3
        matrix1.column = 0
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.validate_indicies((170141183460469231731687303715884105727, -170141183460469231731687303715884105728))
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.__getitem__
    
    # region FUZZER
    
    def test___getitem___with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        """
        matrix1 = matrix.sherman_morrison.Matrix(2, 2)
        # This test fails because function [matrix.sherman_morrison.__getitem__] produces [AssertionError]
        matrix1.__getitem__((2, -170141183460469231731687303715884105728))
        
        self.assertEqual(matrix1, matrix1)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___getitem___with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        """
        matrix1 = matrix.sherman_morrison.Matrix(2, 332306998946228968225951765070086146)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__getitem__((-170141183460469231731687303715884105726, -127605887595351923798765477786913079296))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___getitem___with_exception2(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        """
        matrix1 = matrix.sherman_morrison.Matrix(2, 131074)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__getitem__((-170141183460469231731687303715884105726, -127605887595351923798765477786913079296))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___getitem___with_exception3(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 170141183460469231731687303715884105727)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__getitem__((2, 8589934592))
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.__setitem__
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___setitem___with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        value = float('-inf')
        """
        matrix1 = matrix.sherman_morrison.Matrix(1, 170141183460469231731687303715884105727)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__setitem__((170141183460469231731687303715867328511, 0), float('-inf'))
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___setitem___with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        loc = typing.Tuple[builtins.int, builtins.int]
        value = float('-inf')
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 2)
        matrix1.row = -1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__setitem__((0, -170141183460469231731687303715884105727), float('-inf'))
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.__add__
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___add___with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        another = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 1)
        matrix1.array = [[float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('-inf'), float('nan'), float('inf'), float('nan')]]
        matrix1.column = 170141183460469231731687303715884105727
        another = matrix.sherman_morrison.Matrix(-1, -1)
        another.column = 1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__add__(another)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___add___with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        another = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(-1, 170141183460469231731687303715884105727)
        another = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 0)
        another.row = -170141183460469231731687303715884105728
        another.column = 1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__add__(another)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___add___with_exception2(self):
        """
        self = matrix.sherman_morrison.Matrix
        another = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(0, 1)
        another = matrix.sherman_morrison.Matrix(158456325028528675187087900672, 0)
        another.array = []
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__add__(another)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.__neg__
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___neg___with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 1)
        matrix1.array = [[float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('nan'), float('nan'), float('-inf')]]
        matrix1.column = 170141183460469231731687303715884105727
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__neg__()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___neg___with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(1, 170141183460469231731687303715884105727)
        matrix1.row = 0
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__neg__()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___neg___with_exception2(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(1, 170141183460469231731687303715884105719)
        matrix1.row = -170141183460469231731687303715884105728
        matrix1.array = [[float('inf'), float('inf')], [float('inf'), float('inf')]]
        matrix1.column = -1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__neg__()
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.__sub__
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___sub___with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        another = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 1)
        matrix1.array = [[float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('-inf'), float('nan'), float('inf'), float('nan')]]
        matrix1.column = 170141183460469231731687303715884105727
        another = matrix.sherman_morrison.Matrix(-1, -1)
        another.column = 1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__sub__(another)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___sub___with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        another = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(-1, 170141183460469231731687303715884105727)
        another = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 0)
        another.row = -170141183460469231731687303715884105728
        another.column = 1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__sub__(another)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___sub___with_exception2(self):
        """
        self = matrix.sherman_morrison.Matrix
        another = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(0, 1)
        another = matrix.sherman_morrison.Matrix(158456325028528675187087900672, 0)
        another.array = []
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__sub__(another)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.__mul__
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test___mul___with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        another = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 4722366482869645213697)
        matrix1.array = [[float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('-inf'), float('nan'), float('inf'), float('nan')]]
        matrix1.column = 170141183460469231731687303715884105727
        another = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 0)
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.__mul__(another)
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.transpose
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_transpose_with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 1)
        matrix1.array = [[float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [float('inf'), float('inf'), float('nan'), float('nan'), float('-inf')]]
        matrix1.column = 170141183460469231731687303715884105727
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.transpose()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_transpose_with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(1, 170141183460469231731687303715884105727)
        matrix1.row = 0
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.transpose()
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_transpose_with_exception2(self):
        """
        self = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(1, 170141183460469231731687303715884105719)
        matrix1.row = -170141183460469231731687303715884105728
        matrix1.array = [[float('inf'), float('inf')], [float('inf'), float('inf')]]
        matrix1.column = -1
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.transpose()
    # endregion
    
    # endregion
    
    # region Test suites for executable matrix.sherman_morrison.sherman_morrison
    
    # region FUZZER
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_sherman_morrison_with_exception(self):
        """
        self = matrix.sherman_morrison.Matrix
        u = matrix.sherman_morrison.Matrix
        v = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(1, 68719476737)
        matrix1.array = [[0.0, 1.112570881186256E-308, 1.1125369292536046E-308, 1.2882297539194267E-231, 1.7800590868057611E-307], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [1.0, 1.000000000001819, 0.0625, 2.9387358770557188E-39, 7.458340731200207E-155], [float('nan'), float('nan'), float('nan'), float('nan'), float('nan')], [1.0, 1.0009765625, 1.000000000007276, 1.03125, -1.0]]
        matrix1.column = -170141183460469231731687303715884105728
        u = matrix.sherman_morrison.Matrix(-170141183460469231731687303715884105728, 1)
        u.array = [[float('inf'), 1.0, 0.0, 0.0], [float('inf'), 0.0, 0.0, 1.0], [0.0, 0.0, float('inf'), 1.0], [float('inf'), 0.0, 0.0, 1.0]]
        u.column = 1
        u.row = 1
        v = matrix.sherman_morrison.Matrix(-170141183460469231731687303715884105728, -1)
        v.row = 0
        v.column = -170141183460469231731687303715884105728
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.sherman_morrison(u, v)
    
    @unittest.skip(reason='Disabled due to the fact that the execution is longer then 1000 ms')
    def test_sherman_morrison_with_exception1(self):
        """
        self = matrix.sherman_morrison.Matrix
        u = matrix.sherman_morrison.Matrix
        v = matrix.sherman_morrison.Matrix
        """
        matrix1 = matrix.sherman_morrison.Matrix(170141183460469231731687303715884105727, 170141183460469231731687303715884105727)
        matrix1.row = 0
        matrix1.column = 0
        matrix1.array = [[1.0, 1.0], [0.0, -1.1125369292536007E-308]]
        u = matrix.sherman_morrison.Matrix(2, 0)
        u.array = [[float('nan'), float('nan'), float('nan')], [float('nan'), float('nan')], [float('nan'), float('nan'), float('nan')]]
        u.row = 1
        u.column = -1
        v = matrix.sherman_morrison.Matrix(2, -1)
        v.row = 0
        
        """This execution may take longer than the 1000 ms timeout
         and therefore fail due to exceeding the timeout."""
        matrix1.sherman_morrison(u, v)
    # endregion
    
    # endregion

