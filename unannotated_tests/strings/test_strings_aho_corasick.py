import sys
sys.path.append(r'..\..\..')
import builtins
import strings.aho_corasick
import types
import strings
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.aho_corasick.find_next_state
    
    # region FUZZER
    
    def test_find_next_state(self):
        """
        self = strings.aho_corasick.Automaton
        current_state = -1
        char = '€'
        """
        automaton = strings.aho_corasick.Automaton(["pythön", "abcdefghijklmnopqrst", "next_states", "pythön", "€"])
        
        actual = automaton.find_next_state(-1, "€")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(automaton, automaton)
    
    def test_find_next_state1(self):
        """
        self = strings.aho_corasick.Automaton
        current_state = -2 (mutated from -1)
        char = '₂€'
        """
        automaton = strings.aho_corasick.Automaton(["abcdefghijklmnopqrst", "€", "pythön", "pythön", "next_states"])
        
        actual = automaton.find_next_state(-2, "₂€")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(automaton, automaton)
    
    def test_find_next_state_with_exception(self):
        """
        self = strings.aho_corasick.Automaton
        current_state = min
        char = 'abcdefghijklmnopqrst'
        """
        automaton = strings.aho_corasick.Automaton(["v#alue", "value", "walue", "vmalue", "valuIe"])
        # This test fails because function [strings.aho_corasick.find_next_state] produces [IndexError]
        automaton.find_next_state(-170141183460469231731687303715884105728, "abcdefghijklmnopqrst")
        
        self.assertEqual(automaton, automaton)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.aho_corasick.add_keyword
    
    # region FUZZER
    
    def test_add_keyword(self):
        """
        self = strings.aho_corasick.Automaton
        keyword = 'next_states'
        """
        automaton = strings.aho_corasick.Automaton(["next_states", "fail_state"])
        
        actual = automaton.add_keyword("next_states")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(automaton, automaton)
    
    def test_add_keyword1(self):
        """
        self = strings.aho_corasick.Automaton
        keyword = 'fail_stat-e'
        """
        automaton = strings.aho_corasick.Automaton(["next_states", "ex&t_states", "next_states", "next_sttes"])
        
        actual = automaton.add_keyword("fail_stat-e")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(automaton, automaton)
    
    def test_add_keyword2(self):
        """
        self = strings.aho_corasick.Automaton
        keyword = 'fail_tate'
        """
        automaton = strings.aho_corasick.Automaton(["value", "foo", "value"])
        
        actual = automaton.add_keyword("fail_tate")
        
        self.assertEqual(None, actual)
        
        self.assertEqual(automaton, automaton)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.aho_corasick.set_fail_transitions
    
    # region FUZZER
    
    def test_set_fail_transitions(self):
        """
        self = strings.aho_corasick.Automaton
        """
        automaton = strings.aho_corasick.Automaton(["pythnv", "pythön", "pythön", "fail_state", "€"])
        
        actual = automaton.set_fail_transitions()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(automaton, automaton)
    
    def test_set_fail_transitions1(self):
        """
        self = strings.aho_corasick.Automaton
        """
        automaton = strings.aho_corasick.Automaton(["abcdefghijklmnopqrst", "output", "next_states", "next_states"])
        
        actual = automaton.set_fail_transitions()
        
        self.assertEqual(None, actual)
        
        self.assertEqual(automaton, automaton)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.aho_corasick.search_in
    
    # region FUZZER
    
    def test_search_in(self):
        """
        self = strings.aho_corasick.Automaton
        string = 'pyCthön'
        """
        automaton = strings.aho_corasick.Automaton(["output", "outp<ut", "output°", "utput", "outpt"])
        
        actual = automaton.search_in("pyCthön")
        
        self.assertEqual({}, actual)
        
        self.assertEqual(automaton, automaton)
    
    def test_search_in1(self):
        """
        self = strings.aho_corasick.Automaton
        string = 'pythön'
        """
        automaton = strings.aho_corasick.Automaton(["pythön", "pythön", "pytwhöhn"])
        
        actual = automaton.search_in("pythön")
        
        self.assertEqual({'pythön': [0, 0], }, actual)
        
        self.assertEqual(automaton, automaton)
    
    def test_search_in2(self):
        """
        self = strings.aho_corasick.Automaton
        string = 'pythn'
        """
        automaton = strings.aho_corasick.Automaton(["pythön", "pythön", "pytwhöhn"])
        
        actual = automaton.search_in("pythn")
        
        self.assertEqual({}, actual)
        
        self.assertEqual(automaton, automaton)
    
    def test_search_in3(self):
        """
        self = strings.aho_corasick.Automaton
        string = 'pythönD'
        """
        automaton = strings.aho_corasick.Automaton(["fail_state", "pythön", "foo", "fail_state", "€"])
        
        actual = automaton.search_in("pythönD")
        
        self.assertEqual({'pythön': [0], }, actual)
        
        self.assertEqual(automaton, automaton)
    # endregion
    
    # endregion

