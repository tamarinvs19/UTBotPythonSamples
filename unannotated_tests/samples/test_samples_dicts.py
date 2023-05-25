import sys
sys.path.append(r'../..')
import samples.dicts
import builtins
import types
import samples
import unittest


class TestTopLevelFunctions(unittest.TestCase):
    # region Test suites for executable samples.dicts.keys
    
    # region FUZZER
    
    def test_keys(self):
        """
        self = samples.dicts.Word
        """
        word = samples.dicts.Word({"foo": "abcdefghijklmnopqrst", })
        
        actual = word.keys()
        
        self.assertEqual(['foo'], actual)
        
        actual_translations = word.translations
        expected_translations = word.translations
        
        self.assertEqual(expected_translations, actual_translations)
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.dicts.translate
    
    # region FUZZER
    
    def test_translate(self):
        """
        self = samples.dicts.Dictionary
        word = 'pythön'
        language = None
        """
        dictionary = samples.dicts.Dictionary([], [{"€": "€", }, {"€": "€", }, {"€": "€", }, {"€": "€", }, {"€": "€", }])
        
        actual = dictionary.translate("pythön", None)
        
        self.assertEqual(None, actual)
        
        actual_languages = dictionary.languages
        expected_languages = dictionary.languages
        
        self.assertEqual(expected_languages, actual_languages)
        actual_words = dictionary.words
        expected_words = dictionary.words
        expected_list = expected_words
        expected_length = len(expected_list)
        actual_length = len(actual_words)
        
        self.assertEqual(expected_length, actual_length)
        
        index = None
        for index in range(0, expected_length, 1):
            expected_element = expected_list[index]
            actual_element = actual_words[index]
            actual_translations = actual_element.translations
            expected_translations = expected_element.translations
            
            self.assertEqual(expected_translations, actual_translations)
    
    def test_translate_with_exception(self):
        """
        self = samples.dicts.Dictionary
        word = 'pythn'
        language = 'foo'
        """
        dictionary = samples.dicts.Dictionary(["foo"], [{"abcdefghijklmnopqrst": "abcdefghijklmnopqrst", "pythön": "pythön", }, {"abcdefghijklmnopqrst": "£abcdefghijklmnopqrs", "pythön": "pythön", }])
        # This test fails because function [samples.dicts.translate] produces [KeyError]
        dictionary.translate("pythn", "foo")
        
        actual_languages = dictionary.languages
        expected_languages = dictionary.languages
        
        self.assertEqual(expected_languages, actual_languages)
        actual_words = dictionary.words
        expected_words = dictionary.words
        expected_list = expected_words
        expected_length = len(expected_list)
        actual_length = len(actual_words)
        
        self.assertEqual(expected_length, actual_length)
        
        index = None
        for index in range(0, expected_length, 1):
            expected_element = expected_list[index]
            actual_element = actual_words[index]
            actual_translations = actual_element.translations
            expected_translations = expected_element.translations
            
            self.assertEqual(expected_translations, actual_translations)
    # endregion
    
    # endregion

