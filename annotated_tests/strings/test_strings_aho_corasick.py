import sys
sys.path.append(r'../..')
import builtins
import strings.aho_corasick
import typing
import types
import copyreg
import strings
import unittest


class TestAutomaton(unittest.TestCase):
    # region Test suites for executable strings.aho_corasick.find_next_state
    
    # region FUZZER
    
    def test_find_next_state(self):
        """
        self = strings.aho_corasick.Automaton
        current_state = positive
        char = 'value'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 28], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [3, 19], 'fail_state': 28, 'output': [], }, {'value': 'x', 'next_states': [4], 'fail_state': 29, 'output': [], }, {'value': 't', 'next_states': [5, 12], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [7], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [11], 'fail_state': 28, 'output': [], }, {'value': 's', 'next_states': [], 'fail_state': 0, 'output': ['next_states', 'next_states'], }, {'value': '\x85', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [14], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [15], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [16], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [17], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [18], 'fail_state': 28, 'output': [], }, {'value': 's', 'next_states': [], 'fail_state': 0, 'output': ['next\x85_sttes'], }, {'value': "'", 'next_states': [20], 'fail_state': 0, 'output': [], }, {'value': 'x', 'next_states': [21], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [22], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [23], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [24], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [25], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [26], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [27], 'fail_state': 28, 'output': [], }, {'value': 's', 'next_states': [], 'fail_state': 0, 'output': ["ne'x_states"], }, {'value': 'e', 'next_states': [29], 'fail_state': 0, 'output': [], }, {'value': 'x', 'next_states': [30], 'fail_state': 0, 'output': [], }, {'value': 'B', 'next_states': [31], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [32], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [33], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [34], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [35], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [36], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [37], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [38], 'fail_state': 28, 'output': [], }, {'value': 's', 'next_states': [], 'fail_state': 0, 'output': ['exBt_states'], }]
        
        actual = automaton.find_next_state(1, 'value')
        
        self.assertEqual(None, actual)
    
    def test_find_next_state1(self):
        """
        self = strings.aho_corasick.Automaton
        current_state = zero
        char = '€'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1], 'fail_state': 0, 'output': [], }, {'value': '€', 'next_states': [2], 'fail_state': 0, 'output': ['€', '€'], }, {'value': 'ₛ', 'next_states': [], 'fail_state': 0, 'output': ['€ₛ'], }]
        
        actual = automaton.find_next_state(0, '€')
        
        self.assertEqual(1, actual)
    
    def test_find_next_state2(self):
        """
        self = strings.aho_corasick.Automaton
        current_state = -1
        char = 'value'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 7, 27], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'y', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': 'ö', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [], 'fail_state': 0, 'output': ['pythön'], }, {'value': 'a', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'b', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 'c', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'd', 'next_states': [11], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [12], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': 'g', 'next_states': [14], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [15], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [16], 'fail_state': 0, 'output': [], }, {'value': 'j', 'next_states': [17], 'fail_state': 0, 'output': [], }, {'value': 'k', 'next_states': [18], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [19], 'fail_state': 0, 'output': [], }, {'value': 'm', 'next_states': [20], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [21], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [22], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [23], 'fail_state': 1, 'output': [], }, {'value': 'q', 'next_states': [24], 'fail_state': 0, 'output': [], }, {'value': 'r', 'next_states': [25], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [26], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [], 'fail_state': 0, 'output': ['abcdefghijklmnopqrst', 'abcdefghijklmnopqrst'], }, {'value': 'v', 'next_states': [28], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [29], 'fail_state': 7, 'output': [], }, {'value': 'l', 'next_states': [30], 'fail_state': 0, 'output': [], }, {'value': 'u', 'next_states': [31], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [], 'fail_state': 0, 'output': ['value'], }]
        
        actual = automaton.find_next_state(-1, 'value')
        
        self.assertEqual(None, actual)
    
    def test_find_next_state_with_exception(self):
        """
        self = strings.aho_corasick.Automaton
        current_state = positive
        char = 'foo'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{}, {}, {}, {}, {}]
        
        automaton.find_next_state(1, 'foo')
        
        # raises builtins.KeyError
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.aho_corasick.add_keyword
    
    # region FUZZER
    
    def test_add_keyword(self):
        """
        self = strings.aho_corasick.Automaton
        keyword = '€'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 11, 31], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [3], 'fail_state': 11, 'output': [], }, {'value': 'i', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [7], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [9], 'fail_state': 11, 'output': [], }, {'value': 't', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [], 'fail_state': 0, 'output': ['fail_state'], }, {'value': 'a', 'next_states': [12], 'fail_state': 0, 'output': [], }, {'value': 'b', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': 'c', 'next_states': [14], 'fail_state': 0, 'output': [], }, {'value': 'd', 'next_states': [15], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [16], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [17], 'fail_state': 1, 'output': [], }, {'value': 'g', 'next_states': [18], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [19], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [20], 'fail_state': 0, 'output': [], }, {'value': 'j', 'next_states': [21], 'fail_state': 0, 'output': [], }, {'value': 'k', 'next_states': [22], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [23], 'fail_state': 0, 'output': [], }, {'value': 'm', 'next_states': [24], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [25], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [26], 'fail_state': 31, 'output': [], }, {'value': 'p', 'next_states': [27], 'fail_state': 0, 'output': [], }, {'value': 'q', 'next_states': [28], 'fail_state': 0, 'output': [], }, {'value': 'r', 'next_states': [29], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [30], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [], 'fail_state': 0, 'output': ['abcdefghijklmnopqrst'], }, {'value': 'o', 'next_states': [32], 'fail_state': 0, 'output': [], }, {'value': 'u', 'next_states': [33], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [34], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [35], 'fail_state': 0, 'output': [], }, {'value': 'u', 'next_states': [36], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [], 'fail_state': 0, 'output': ['output'], }]
        
        actual = automaton.add_keyword('€')
        
        self.assertEqual(None, actual)
    
    def test_add_keyword1(self):
        """
        self = strings.aho_corasick.Automaton
        keyword = 'abcdefghijklmnopqrst'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 7], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'y', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': 'ö', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [], 'fail_state': 0, 'output': ['pythön'], }, {'value': 'a', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'b', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 'c', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'd', 'next_states': [11], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [12], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': 'g', 'next_states': [14], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [15], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [16], 'fail_state': 0, 'output': [], }, {'value': 'j', 'next_states': [17], 'fail_state': 0, 'output': [], }, {'value': 'k', 'next_states': [18], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [19], 'fail_state': 0, 'output': [], }, {'value': 'm', 'next_states': [20], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [21], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [22], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [23], 'fail_state': 1, 'output': [], }, {'value': 'q', 'next_states': [24], 'fail_state': 0, 'output': [], }, {'value': 'r', 'next_states': [25], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [26], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [], 'fail_state': 0, 'output': ['abcdefghijklmnopqrst'], }]
        
        actual = automaton.add_keyword('abcdefghijklmnopqrst')
        
        self.assertEqual(None, actual)
    
    def test_add_keyword2(self):
        """
        self = strings.aho_corasick.Automaton
        keyword = 'abcdefghRijklmnopqrt'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 7], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'y', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': 'ö', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [], 'fail_state': 0, 'output': ['pythön'], }, {'value': 'a', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'b', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 'c', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'd', 'next_states': [11], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [12], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': 'g', 'next_states': [14], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [15], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [16], 'fail_state': 0, 'output': [], }, {'value': 'j', 'next_states': [17], 'fail_state': 0, 'output': [], }, {'value': 'k', 'next_states': [18], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [19], 'fail_state': 0, 'output': [], }, {'value': 'm', 'next_states': [20], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [21], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [22], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [23], 'fail_state': 1, 'output': [], }, {'value': 'q', 'next_states': [24], 'fail_state': 0, 'output': [], }, {'value': 'r', 'next_states': [25], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [26], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [], 'fail_state': 0, 'output': ['abcdefghijklmnopqrst'], }]
        
        actual = automaton.add_keyword('abcdefghRijklmnopqrt')
        
        self.assertEqual(None, actual)
    
    def test_add_keyword3(self):
        """
        self = strings.aho_corasick.Automaton
        keyword = ''
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 13, 14, 25], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [2, 11], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [7], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [], 'fail_state': 0, 'output': ['fail_state'], }, {'value': 'o', 'next_states': [12], 'fail_state': 25, 'output': [], }, {'value': 'o', 'next_states': [], 'fail_state': 25, 'output': ['foo'], }, {'value': '€', 'next_states': [], 'fail_state': 0, 'output': ['€'], }, {'value': 'n', 'next_states': [15], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [16], 'fail_state': 0, 'output': [], }, {'value': 'x', 'next_states': [17], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [18], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [19], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [20], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [21], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [22], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [23], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [24], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [], 'fail_state': 0, 'output': ['next_states'], }, {'value': 'o', 'next_states': [26], 'fail_state': 0, 'output': [], }, {'value': 'u', 'next_states': [27], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [28], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [29], 'fail_state': 0, 'output': [], }, {'value': 'u', 'next_states': [30], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [], 'fail_state': 0, 'output': ['output'], }]
        
        actual = automaton.add_keyword('')
        
        self.assertEqual(None, actual)
    
    def test_add_keyword_with_exception(self):
        """
        self = strings.aho_corasick.Automaton
        keyword = 'output'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{}, {}, {}, {}, {}]
        
        automaton.add_keyword('output')
        
        # raises builtins.KeyError
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.aho_corasick.set_fail_transitions
    
    # region FUZZER
    
    def test_set_fail_transitions(self):
        """
        self = strings.aho_corasick.Automaton
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 4, 9], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [3], 'fail_state': 9, 'output': [], }, {'value': 'o', 'next_states': [8, 12], 'fail_state': 10, 'output': ['foo'], }, {'value': '6', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [6], 'fail_state': 1, 'output': [], }, {'value': 'o', 'next_states': [7], 'fail_state': 2, 'output': [], }, {'value': 'o', 'next_states': [], 'fail_state': 3, 'output': ['6foo', 'foo'], }, {'value': 'ª', 'next_states': [], 'fail_state': 0, 'output': ['fooª'], }, {'value': 'o', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [11], 'fail_state': 9, 'output': [], }, {'value': 'z', 'next_states': [], 'fail_state': 0, 'output': ['ooz'], }, {'value': 'g', 'next_states': [], 'fail_state': 0, 'output': ['foog'], }]
        
        actual = automaton.set_fail_transitions()
        
        self.assertEqual(None, actual)
    
    def test_set_fail_transitions1(self):
        """
        self = strings.aho_corasick.Automaton
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 11, 22], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [7], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [], 'fail_state': 0, 'output': ['fail_state'], }, {'value': 'n', 'next_states': [12], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': 'x', 'next_states': [14], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [15], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [16], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [17], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [18], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [19], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [20], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [21], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [], 'fail_state': 0, 'output': ['next_states', 'next_states'], }, {'value': 'p', 'next_states': [23], 'fail_state': 0, 'output': [], }, {'value': 'y', 'next_states': [24], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [25], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [26], 'fail_state': 0, 'output': [], }, {'value': 'ö', 'next_states': [27], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [], 'fail_state': 11, 'output': ['pythön'], }]
        
        actual = automaton.set_fail_transitions()
        
        self.assertEqual(None, actual)
    
    def test_set_fail_transitions2(self):
        """
        self = strings.aho_corasick.Automaton
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [], 'fail_state': 0, 'output': [], }]
        
        actual = automaton.set_fail_transitions()
        
        self.assertEqual(None, actual)
    
    def test_set_fail_transitions_with_exception(self):
        """
        self = strings.aho_corasick.Automaton
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{}, {}, {}, {}, {}]
        
        automaton.set_fail_transitions()
        
        # raises builtins.KeyError
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.aho_corasick.search_in
    
    # region FUZZER
    
    def test_search_in(self):
        """
        self = strings.aho_corasick.Automaton
        string = '€'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 11], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [2, 12], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [7], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [], 'fail_state': 0, 'output': ['fail_state'], }, {'value': '€', 'next_states': [], 'fail_state': 0, 'output': ['€', '€'], }, {'value': 'o', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [], 'fail_state': 0, 'output': ['foo'], }]
        
        actual = automaton.search_in('€')
        
        self.assertEqual({'€': [0, 0], }, actual)
    
    def test_search_in1(self):
        """
        self = strings.aho_corasick.Automaton
        string = 'output'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 4, 19], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [2, 10], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [], 'fail_state': 0, 'output': ['foo'], }, {'value': 'p', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': 'y', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [7], 'fail_state': 0, 'output': [], }, {'value': 'h', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': 'ö', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 'n', 'next_states': [], 'fail_state': 0, 'output': ['pythön', 'pythön'], }, {'value': 'a', 'next_states': [11], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [12], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [14], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [15], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [16], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [17], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [18], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [], 'fail_state': 0, 'output': ['fail_state'], }, {'value': '€', 'next_states': [], 'fail_state': 0, 'output': ['€'], }]
        
        actual = automaton.search_in('output')
        
        self.assertEqual({}, actual)
    
    def test_search_in2(self):
        """
        self = strings.aho_corasick.Automaton
        string = '€'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'u', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'p', 'next_states': [5], 'fail_state': 0, 'output': [], }, {'value': 'u', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [], 'fail_state': 0, 'output': ['output'], }]
        
        actual = automaton.search_in('€')
        
        self.assertEqual({}, actual)
    
    def test_search_in3(self):
        """
        self = strings.aho_corasick.Automaton
        string = '₋€₿'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1, 2], 'fail_state': 0, 'output': [], }, {'value': '€', 'next_states': [], 'fail_state': 0, 'output': ['€', '€'], }, {'value': 'f', 'next_states': [3, 5], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [4], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [], 'fail_state': 0, 'output': ['foo'], }, {'value': 'a', 'next_states': [6], 'fail_state': 0, 'output': [], }, {'value': 'i', 'next_states': [7], 'fail_state': 0, 'output': [], }, {'value': 'l', 'next_states': [8], 'fail_state': 0, 'output': [], }, {'value': '_', 'next_states': [9], 'fail_state': 0, 'output': [], }, {'value': 's', 'next_states': [10], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [11], 'fail_state': 0, 'output': [], }, {'value': 'a', 'next_states': [12], 'fail_state': 0, 'output': [], }, {'value': 't', 'next_states': [13], 'fail_state': 0, 'output': [], }, {'value': 'e', 'next_states': [], 'fail_state': 0, 'output': ['fail_state'], }]
        
        actual = automaton.search_in('₋€₿')
        
        self.assertEqual({'€': [1, 1], }, actual)
    
    def test_search_in4(self):
        """
        self = strings.aho_corasick.Automaton
        string = ''
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{'value': '', 'next_states': [1], 'fail_state': 0, 'output': [], }, {'value': 'f', 'next_states': [2], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [3], 'fail_state': 0, 'output': [], }, {'value': 'o', 'next_states': [4], 'fail_state': 0, 'output': ['foo'], }, {'value': '\x7f', 'next_states': [], 'fail_state': 0, 'output': ['foo\x7f'], }]
        
        actual = automaton.search_in('')
        
        self.assertEqual({}, actual)
    
    def test_search_in_with_exception(self):
        """
        self = strings.aho_corasick.Automaton
        string = 'fail_state'
        """
        automaton = copyreg._reconstructor(strings.aho_corasick.Automaton, builtins.object, None)
        automaton.adlist = [{}]
        
        automaton.search_in('fail_state')
        
        # raises builtins.KeyError
    # endregion
    
    # endregion

