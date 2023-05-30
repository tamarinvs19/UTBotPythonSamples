import sys
sys.path.append(r'../../..')
import builtins
import types
import strings
import unittest
import strings.autocomplete_using_trie


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable strings.autocomplete_using_trie.autocomplete_using_trie
    
    # region FUZZER
    
    def test_autocomplete_using_trie(self):
        """
        string = '€'
        """
        actual = strings.autocomplete_using_trie.autocomplete_using_trie("€")
        
        self.assertEqual((), actual)
    # endregion
    
    # endregion
    
    # region Test suites for executable strings.autocomplete_using_trie.main
    
    # region FUZZER
    
    def test_main(self):
        actual = strings.autocomplete_using_trie.main()
        
        self.assertEqual(None, actual)
    # endregion
    
    # endregion

