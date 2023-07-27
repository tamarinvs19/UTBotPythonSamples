import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\..')
import genetic_algorithm
import unittest
import genetic_algorithm.basic_string


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable genetic_algorithm.basic_string.evaluate
    
    # region FUZZER
    
    def test_evaluate(self):
        """
        item = 'foo'
        main_target = 'npöyth'
        """
        actual = genetic_algorithm.basic_string.evaluate("foo", "npöyth")
        
        self.assertEqual(('foo', 0.0), actual)
    
    def test_evaluate_with_exception(self):
        """
        item = 'foo'
        main_target = ''
        """
        # This test fails because function [genetic_algorithm.basic_string.evaluate] produces [IndexError]
        genetic_algorithm.basic_string.evaluate("foo", "")
    # endregion
    
    # endregion
    
    # region Test suites for executable genetic_algorithm.basic_string.crossover
    
    # region FUZZER
    
    def test_crossover(self):
        """
        parent_1 = 'foo'
        parent_2 = 'npöyth'
        """
        actual = genetic_algorithm.basic_string.crossover("foo", "npöyth")
        
        self.assertEqual(('foöyth', 'npo'), actual)
    
    def test_crossover_with_exception(self):
        """
        parent_1 = ''
        parent_2 = 'Slice and combine two string at a random point.'
        """
        # This test fails because function [genetic_algorithm.basic_string.crossover] produces [ValueError]
        genetic_algorithm.basic_string.crossover("", "Slice and combine two string at a random point.")
    # endregion
    
    # endregion
    
    # region Test suites for executable genetic_algorithm.basic_string.mutate
    
    # region FUZZER
    
    def test_mutate(self):
        """
        child = 'ª' (mutated from '')
        genes = builtins.list[builtins.str]
        """
        actual = genetic_algorithm.basic_string.mutate("ª", ["", "pythön", "pythön"])
        
        self.assertEqual('ª', actual)
    
    def test_mutate1(self):
        """
        child = 'Mutate a random gene of a child wit another one from the list.'
        genes = builtins.list[builtins.str]
        """
        actual = genetic_algorithm.basic_string.mutate("Mutate a random gene of a child wit another one from the list.", ["pythön", "pythön", "pythön", "pythön"])
        
        self.assertEqual('Mutate a random gene of a pythönhild wit another one from the list.', actual)
    
    def test_mutate_with_exception(self):
        """
        child = ''
        genes = builtins.list[builtins.str]
        """
        # This test fails because function [genetic_algorithm.basic_string.mutate] produces [IndexError]
        genetic_algorithm.basic_string.mutate("", ["", "pythön", "pythön"])
    # endregion
    
    # endregion
    
    # region Test suites for executable genetic_algorithm.basic_string.select
    
    # region FUZZER
    
    def test_select(self):
        """
        parent_1 = typing.Tuple[builtins.str, builtins.float]
        population_score = builtins.list[typing.Tuple[builtins.str, builtins.float]]
        genes = builtins.list[builtins.str]
        """
        actual = genetic_algorithm.basic_string.select(("pythön", 0.0), [("", 10.00000000000091)], ["pythön", "", "pythön", ""])
        
        self.assertEqual(['pyth', 'n'], actual)
    
    def test_select1(self):
        """
        parent_1 = typing.Tuple[builtins.str, builtins.float]
        population_score = builtins.list[typing.Tuple[builtins.str, builtins.float]]
        genes = builtins.list[builtins.str]
        """
        actual = genetic_algorithm.basic_string.select(("Select the second parent and generate new population", -10.0), [("foo", float('nan')), ("foo", 100.0), ("", float('-inf')), ("", 10.0)], ["pythön"])
        
        self.assertEqual([], actual)
    
    def test_select_with_exception(self):
        """
        parent_1 = typing.Tuple[builtins.str, builtins.float]
        population_score = builtins.list[typing.Tuple[builtins.str, builtins.float]]
        genes = builtins.list[builtins.str]
        """
        # This test fails because function [genetic_algorithm.basic_string.select] produces [IndexError]
        genetic_algorithm.basic_string.select(("foo", 10.0), [("foo", float('-inf')), ("Select the second parent and generate new population", float('-inf')), ("foo", 0.0)], ["Select the second parent and generate new population"])
    
    def test_select_with_exception1(self):
        """
        parent_1 = typing.Tuple[builtins.str, builtins.float]
        population_score = builtins.list[typing.Tuple[builtins.str, builtins.float]]
        genes = builtins.list[builtins.str]
        """
        # This test fails because function [genetic_algorithm.basic_string.select] produces [ValueError]
        genetic_algorithm.basic_string.select(("pythön", float('nan')), [("", float('nan')), ("Select the second parent and generate new population", 100.0), ("foo", 1.0)], ["pythön", "pythön", "Select the second parent and generate new population", "foo", "Select the seond parent and generate new population"])
    
    def test_select_with_exception2(self):
        """
        parent_1 = typing.Tuple[builtins.str, builtins.float]
        population_score = builtins.list[typing.Tuple[builtins.str, builtins.float]]
        genes = builtins.list[builtins.str]
        """
        # This test fails because function [genetic_algorithm.basic_string.select] produces [IndexError]
        genetic_algorithm.basic_string.select(("foo", 1.0), [("Select the second parent and generate new population", 0.0), ("", 10.0), ("foo", 1.0), ("", 10.0), ("", 10.0)], ["", "", "Select the second parent and generate new population", "foo", ""])
    
    def test_select_with_exception3(self):
        """
        parent_1 = typing.Tuple[builtins.str, builtins.float]
        population_score = builtins.list[typing.Tuple[builtins.str, builtins.float]]
        genes = builtins.list[builtins.str]
        """
        # This test fails because function [genetic_algorithm.basic_string.select] produces [IndexError]
        genetic_algorithm.basic_string.select(("fo", 1.0000000000000284), [("Select the second parent and generate new populaion", 0.0), ("", 10.0), ("foo", 1.0), ("", 10.0), ("", 10.0)], ["", "Select the second parent and generate new population", "", "foo", ""])
    
    def test_select_with_exception4(self):
        """
        parent_1 = typing.Tuple[builtins.str, builtins.float]
        population_score = builtins.list[typing.Tuple[builtins.str, builtins.float]]
        genes = builtins.list[builtins.str]
        """
        # This test fails because function [genetic_algorithm.basic_string.select] produces [ValueError]
        genetic_algorithm.basic_string.select(("", 0.0), [("Select the second parent and generate new population", 0.0), ("", float('inf')), ("pythön", 0.0), ("", 0.0), ("pythön", 1.0)], ["foo", "", "pythön", "pythön"])
    # endregion
    
    # endregion
    
    # region Test suites for executable genetic_algorithm.basic_string.basic
    
    # region FUZZER
    
    def test_basic(self):
        """
        target = ''
        genes = builtins.list[builtins.str]
        """
        actual = genetic_algorithm.basic_string.basic("", ["", "pythön", "pythön"])
        
        self.assertEqual((1, 200, ''), actual)
    
    def test_basic_with_exception(self):
        """
        target = 'ª' (mutated from '')
        genes = builtins.list[builtins.str]
        """
        # This test fails because function [genetic_algorithm.basic_string.basic] produces [ValueError]
        genetic_algorithm.basic_string.basic("ª", ["", "pythön", "pythön"])
    # endregion
    
    # endregion

