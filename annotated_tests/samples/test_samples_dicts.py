import sys
sys.path.append(r'../../..')
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
        
        self.assertEqual(word, word)
    # endregion
    
    # endregion
    
    # region Test suites for executable samples.dicts.translate
    
    # region FUZZER
    
    def test_translate(self):
        """
        self = samples.dicts.Dictionary
        word = 'foo'
        language = None
        """
        dictionary = samples.dicts.Dictionary(["abcdefghijklmnopqrst"], [{"foo": "foo", }, {"foo": "foo", }, {"foo": "foo", }, {"Sfo": "€", "foo": "foo", }, {"foo": "foo", }])
        
        actual = dictionary.translate("foo", None)
        
        expected = object.__new__(samples.dicts.Word)
        expected.translations = {'foo': 'foo', }
        actual_translations = actual.translations
        expected_translations = expected.translations
        
        self.assertEqual(expected_translations, actual_translations)
        
        self.assertEqual(dictionary, dictionary)
    
    def test_translate1(self):
        """
        self = samples.dicts.Dictionary
        word = 'abcdefghijklmnopqrst'
        language = 'foo'
        """
        dictionary = samples.dicts.Dictionary(["€"], [{"foo": "€", }, {"foo": "abcdefghijklmnopqrst", "abcdefghijklmnopqrst": "abcdefghijklmnopqrst", }, {"abcdefghijklmnopqrst": "€", }])
        
        actual = dictionary.translate("abcdefghijklmnopqrst", "foo")
        
        expected = object.__new__(samples.dicts.Word)
        expected.translations = {'foo': 'abcdefghijklmnopqrst', 'abcdefghijklmnopqrst': 'abcdefghijklmnopqrst', }
        actual_translations = actual.translations
        expected_translations = expected.translations
        
        self.assertEqual(expected_translations, actual_translations)
        
        self.assertEqual(dictionary, dictionary)
    
    def test_translate_with_exception(self):
        """
        self = samples.dicts.Dictionary
        word = 'pythn'
        language = 'foo'
        """
        dictionary = samples.dicts.Dictionary(["foo"], [{"abcdefghijklmnopqrst": "abcdefghijklmnopqrst", "pythön": "pythön", }, {"abcdefghijklmnopqrst": "£abcdefghijklmnopqrs", "pythön": "pythön", }])
        # This test fails because function [samples.dicts.translate] produces [KeyError]
        dictionary.translate("pythn", "foo")
        
        self.assertEqual(dictionary, dictionary)
    # endregion
    
    # endregion

